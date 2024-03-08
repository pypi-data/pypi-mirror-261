from datetime import datetime, timezone
import os
import queue
import threading
import time
import json
import requests
import signal
import sys
import traceback
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
import dbf
import argparse

try:
    import thread
except ImportError:
    import _thread as thread

from pymongo import MongoClient, ASCENDING, DESCENDING
from .logger import Logger
from .utils import decode_exchange_id
from .constants import DbfFiles

LL9 = 1000000000

class MongoClientTradeGateway(object):
    def __init__(self, config_filename, endtime, gateway_name):

        self.load_gateway_setting(config_filename)
        self.logger = Logger.get_logger(self.log_name, self.log_file_path)
        self.gen_local_id()
        self.endtime = endtime
        self.is_stopped = False
        self.start_mongodb()

        self.thread_pool = ThreadPoolExecutor(10)
        self.sell_orderlock = threading.Lock()
        self.cancel_orderlock = threading.Lock()
        self.order_db_ids = []
        self.sell_order_db_ids = []
        self.cancel_order_ids = []
        self.gateway_name = gateway_name
        self.date = self.get_date_today()

    def error_handler(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                return func(self,*args, **kwargs)
            except Exception as e:
                err = traceback.format_exc()
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)
                self.logger.error(f'[{wrapper}] (exception){err}')
                self.send_error_to_user(self.logger, self.error_url_list, err)
                return 'error'
        return wrapper
        
    def load_gateway_setting(self, config_filename):
        try:
            #固定配置文件的名字
            #config_filename = os.path.join(config_filename, 'atx_cicc_server_config.json')
            #f = open(config_filename, encoding="utf-8")
            f = open(config_filename, encoding='gbk')
            setting = json.load(f)
            
            log_path = setting['log_filepath']
            self.log_file_path = log_path.replace('/', '\\')
            self.url_list = setting.get('url_list')
            self.error_url_list = setting.get('error_url_list')

            self.log_name = setting['log_name']
            self.scan_interval = setting['scan_interval']
            self.order_scan_interval = setting['order_scan_interval']
            self.trade_scan_interval = setting['trade_scan_interval']
            self.pos_interval = setting['pos_interval']
            self.acc_interval = setting['acc_interval']
            
            self.accounts_config = setting['accounts']
            self.accounts_run = setting['run']
            
            self.config = {}
            self.account_id = {}
            self.account_id_to_acc = {}
            self.product_names = {}
            self.log_account_names = {}
            self.tgnames = {}
            self.mongo_host = {}
            self.mongo_port = {}
            self.tradingaccount_user = {}
            self.tradingaccount_pwd = {}
            self.tradinglog_user = {}
            self.tradinglog_pwd = {}
            self.target_account_names = {}
            self.target_account_names_to_acc = {}
            self.contract_type = {}
            for acc in self.accounts_run:
                self.config[acc] = setting['accounts'][acc]
                config = self.config[acc]
                self.account_id[acc] = config['account_id']
                self.account_id_to_acc[config['account_id']] = acc
                self.product_names[acc] = config['product_name']
                self.log_account_names[acc] = config['account_name']
                self.tgnames[acc] = config['equity_tg_name']
                self.target_account_names[acc] = config['equity_tg_name'] + "@" + config['account_name']
                self.target_account_names_to_acc[self.target_account_names[acc]] = acc
                self.mongo_host[acc] = config['mongoHost']
                self.mongo_port[acc] = config['mongoPort']
                datadbuser = config['databaseUser']
                self.tradingaccount_user[acc] = datadbuser['tradingAccount']['user']
                self.tradingaccount_pwd[acc] = datadbuser['tradingAccount']['password']
                self.tradinglog_user[acc] = datadbuser['tradingLog']['user']
                self.tradinglog_pwd[acc] = datadbuser['tradingLog']['password']
            
        except Exception as e:
            err = traceback.format_exc()
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)
            print(f"load config failed! (exception){err}")
            exit(0)
    
    def start_mongodb(self):
        try:
            self.db_client = {}
            self.order_info_db = {}
            self.tradelog_db = {}
            for acc in self.accounts_run:
                self.db_client[acc] = MongoClient(
                    self.mongo_host[acc], self.mongo_port[acc], connectTimeoutMS=10000)
                db_client = self.db_client[acc]
                if self.tradingaccount_user[acc] != '' and self.tradingaccount_pwd[acc] != '':
                    db_client["tradingAccount"].authenticate(
                        self.tradingaccount_user[acc], self.tradingaccount_pwd[acc], mechanism='SCRAM-SHA-1')
                self.order_info_db[acc] = db_client["tradingAccount"]
                
                if self.tradinglog_user[acc] != '' and self.tradinglog_pwd[acc] != '':
                    db_client["tradingLog"].authenticate(
                        self.tradinglog_user[acc], self.tradinglog_pwd[acc], mechanism='SCRAM-SHA-1')
                db_client.server_info()
                self.tradelog_db[acc] = db_client["tradingLog"] 
                
        except Exception as e:
            err = traceback.format_exc()
            self.send_error_to_user(self.error_url_list, err)
            self.logger.error(f'[init] DB_connect_failed! (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)
            exit()

    #通过tradingAccount.accountinfo表获取产品属性
    def get_account_info(self):
        for acc in self.accounts_run:
            product_name = self.product_names[acc]
            query = {"product_name": product_name}
            account_info_collection = self.order_info_db[acc]['account_info']
            account_info = account_info_collection.find_one(query)
            if account_info == None:
                self.logger.error(
                    f"[get_account_info] can't_find_account_info (product_name){product_name}")
                continue
            tgname = account_info['equity_tg_name']
            self.tgnames[acc] = tgname
            log_account_name = account_info['account_name']
            self.log_account_names[acc] = log_account_name
            target_account_name = tgname + '@' + log_account_name
            self.target_account_names[acc] = target_account_name # 下单时用self
            self.logger.info(
                f"[get_account_info] (tg_name){self.tgnames} (logacc_name){self.log_account_names} (target_accountnames){self.target_account_names}") 

    def send_to_user(self, logger, url_list, msg):
        try:
            if len(url_list) == 0:
                logger.info("[send_to_user] send_message_failed")
                return

            payload_message_feishu = {
                "msg_type": "text",
                "content": {
                    "text": msg
                }
            }

            headers = {
                'Content-Type': 'application/json'
            }

            payload_message_dingding = {
                "msgtype": "text",
                "text": {"content": msg},
                "at": {
                    "atMobiles": [""],
                    "isAtAll": "false"  # @所有人 时为true，上面的atMobiles就失效了
                }
            }
            response = requests.request("POST", url_list[0], headers=headers, data=json.dumps(payload_message_feishu))
            data = response.json()
            logger.info(f"[send_to_user] (response){response} (data){data}")
            if len(url_list) > 1:
                response_ding = requests.request("POST", url_list[1], headers=headers, data=json.dumps(payload_message_dingding))
                data_ding = response_ding.json()
                logger.info(f"[send_to_user] (response){response_ding} (data){data_ding}")
        except Exception as e:
            err = traceback.format_exc()
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)
            logger.error(f'[send_to_user] send_message_failed(exception){err}')
            
    def send_error_to_user(self, logger, url_list, msg):
        try:
            if len(url_list) == 0:
                logger.info("[send_error_to_user] send_message_failed")
                return

            payload_message_feishu = {
                "msg_type": "text",
                "content": {
                    "text": msg
                }
            }

            headers = {
                'Content-Type': 'application/json'
            }

            payload_message_dingding = {
                "msgtype": "text",
                "text": {"content": msg},
                "at": {
                    "atMobiles": [""],
                    "isAtAll": "false"  # @所有人 时为true，上面的atMobiles就失效了
                }
            }
            response = requests.request("POST", url_list[0], headers=headers, data=json.dumps(payload_message_feishu))
            data = response.json()
            logger.info(f"[send_error_to_user] (response){response} (data){data}")
            if len(url_list) > 1:
                response_ding = requests.request("POST", url_list[1], headers=headers, data=json.dumps(payload_message_dingding))
                data_ding = response_ding.json()
                logger.info(f"[send_error_to_user] (response){response_ding} (data){data_ding}")
        except Exception as e:
            err = traceback.format_exc()
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)
            logger.error(f'[send_error_to_user] send_message_failed(exception){err}')

    def signal_handler(self, signum=None, frame=None):
        self.is_stopped = True

    def gen_local_id(self):
        self.id_base = 1377779200 * LL9
        self.sp = time.time_ns()
        self.local_id = self.sp - self.id_base

    def gen_order_id(self):
        self.local_id += 1
        return self.local_id

    def get_date_today(self):
        dt = datetime.now()
        date = str(dt.strftime("%Y%m%d"))

        self.logger.info(f"[{self.gateway_name}_get_date_today] (date){date}")

        return date

    @error_handler
    def monitor_dbf_asset(self):
        print ("[monitor_dbf_asset]")
        while not self.is_stopped:
            order_filename = self.recv_msg_dir + '\\' + DbfFiles.ACCOUNTS + self.date + '.dbf'
            asset_table = dbf.Table(filename=order_filename,codepage='utf8', on_disk=True)
            with asset_table.open(mode=dbf.READ_WRITE):
                asset_index = -1
                while asset_table[asset_index+1] is not asset_table.last_record:
                    asset_index += 1
                    record = asset_table[asset_index]
                    self.update_dbf_asset(record)

                asset_index += 1
                self.update_dbf_asset(asset_table.last_record)
            time.sleep(self.acc_interval)

    def update_dbf_asset(self, record):
        trade_acc = str(record.ClientName).strip(' ')
        en_balance = record.EnBalance
        market_amt = record.MarketAmt

        if trade_acc not in self.account_id_to_acc:
            self.logger.warning(f"[update_dbf_asset] can't_parse_trade_acc {trade_acc}")
            return
        acc = self.account_id_to_acc[trade_acc]
        tg_name = self.tgnames[acc]
        account_name = self.log_account_names[acc]

        asset_collection = self.order_info_db[acc]['TestEquityAccount']
        query = {'_id':tg_name, 'accountName': account_name}
        asset_msg = {
            "_id": tg_name, # 对应之前的 TG 名称
            "accountName": account_name,  # 产品名称
            "avail_amt": en_balance,  # 可用资金（可现金买入的资金）
            "balance": en_balance + market_amt, # 净资产.  最好是由券商那边提供，通常普通账户是 可用资金(包含预扣费用) + 市值；信用账户是总资金 - 总负债
            "holding": market_amt, # 市值,
        }
        res = asset_collection.replace_one(query, asset_msg, True)
        self.logger.info(f"[update_dbf_asset] (res){res} (order_msg){asset_msg}")

    @error_handler
    def monitor_dbf_pos(self):
        print ("[monitor_dbf_pos]")
        while not self.is_stopped:
            order_filename = self.recv_msg_dir + '\\' + DbfFiles.POSITIONS + self.date + '.dbf'
            position_table = dbf.Table(filename=order_filename,codepage='utf8', on_disk=True)
            for acc in self.accounts_run:
                tg_position_collection = self.order_info_db[acc]['tg_equity_position']
                remove = tg_position_collection.delete_many({'account_name': self.log_account_names[acc], 'tg_name': self.target_account_names[acc]})
                self.logger.info(f"[monitor_dbf_pos] delete_old_position_info (remove){remove} ")
            with position_table.open(mode=dbf.READ_WRITE):
                pos_index = -1
                while position_table[pos_index+1] is not position_table.last_record:
                    pos_index += 1
                    record = position_table[pos_index]
                    self.update_dbf_position(record)

                pos_index += 1
                self.update_dbf_position(position_table.last_record)
            time.sleep(self.pos_interval)
        
        
    def update_dbf_position(self, record):
        trade_acc = str(record.ClientName).strip(' ')

        if trade_acc not in self.account_id_to_acc:
            self.logger.warning(f"[update_dbf_position] can't_parse_trade_acc {trade_acc}")
            return
        acc = self.account_id_to_acc[trade_acc]
        
        account_name = self.log_account_names[acc]
        tg_name = self.target_account_names[acc]
        ticker = record.Symbol.split('.')[0].strip(' ')
        exchange = decode_exchange_id(str(record.Symbol.split('.')[1]).strip(' '))
        td_pos = record.CurrentQ
        yd_pos = record.EnableQty
        #new_id = tg_name + '@' + account_name + '@' + ticker
        pos_collection = self.order_info_db[acc]['tg_equity_position']
        query = {'tg_name':tg_name, 'account_name': account_name, "ticker": ticker}
        pos_msg = {
              "account_name": account_name,
              "tg_name": tg_name,
              "ticker": ticker,
              "exchange": exchange,
              "direction": "long", # long/short，没有short部分就只存long部分
              "avail_pos": yd_pos, # 昨仓
              "total_pos": td_pos, # 今仓，TODO 需要统计下不同券商盘中，对于卖出的position 是直接从 yd_pos 上减，还是在 td_pos 增加一个负的值。
              "cost": 0, #没有
              "type": "stock",
              "updated_at": datetime.utcnow()
              
                        }
        update_msg = {'$set' : pos_msg}
        res = pos_collection.replace_one(query, pos_msg, True)
        self.logger.info(f"[update_dbf_position] (res){res.modified_count} (order_msg){pos_msg}")

    @error_handler
    def date_change(self):
        while not self.is_stopped:
                time_now = datetime.now()
                _dt_endtime = datetime.strptime(self.endtime, "%H:%M")
                dt_endtime = datetime.combine(time_now, _dt_endtime.time())
                if time_now > dt_endtime:
                    self.close()
                else:
                    self.logger.info(f"[{self.gateway_name}_date_change] not_closed (now){time_now}")

                time.sleep(60)

    def close(self):
        self.is_stopped = True

        msg = f"[{self.gateway_name}_close] (close_time){datetime.now()}"

        self.send_to_user(self.logger, self.url_list, msg)
        os._exit(0)
    
    def update_position_date_open(self):
        for acc in self.accounts_run:
            collection = self.order_info_db[acc]['EquityPosition']
            target_account_name = self.target_account_names[acc]
            targets_query = {'accountName' : target_account_name}
            targets = collection.find(targets_query)
            self.logger.info(f"now (target_account_name){target_account_name}")
            if targets.count() == 0:
                continue
            for position in targets:
                        self.logger.info(f"goes in (position){position}")
                        mid = position['mid']
                        query = {'mid' : mid, 'accountName' : target_account_name}
                        holdingdays = position['holding_days']
                        yd_pos = position['actual_td_pos_long'] + position['actual_yd_pos_long']
                        td_pos = 0
                        change = {
                                        'holding_days': holdingdays,
                                        'yd_pos_long': yd_pos,
                                        'td_pos_long': td_pos,
                                        'actual_yd_pos_long': yd_pos,
                                        'actual_td_pos_long': td_pos
                                    }
                        new_data = {"$set": change}
                        res = collection.update_one(
                                                query, new_data, True)
                        self.logger.info(f"[date_change_open] (res){res} (change){change}")

    def update_position_date_close(self):
        for acc in self.accounts_run:
            collection = self.order_info_db[acc]['EquityPosition']
            target_account_name = self.target_account_names[acc]
            targets_query = {'accountName' : target_account_name}
            targets = collection.find(targets_query)
            if targets.count() == 0:
                continue
            for position in targets:
                    mid = position['mid']
                    query = {'mid' : mid, 'accountName': target_account_name}
                    holding_days = position['holding_days'] + 1
                    yd_pos = position['actual_td_pos_long'] + position['actual_yd_pos_long']
                    td_pos = 0
                    change = {
                                        'holding_days': holding_days,
                                        'yd_pos_long': yd_pos,
                                        'td_pos_long': td_pos,
                                        'actual_yd_pos_long': yd_pos,
                                        'actual_td_pos_long': td_pos
                                    }
                    new_data = {"$set": change}
                    res = collection.update_one(
                                                query, new_data, True)
                    self.logger.info(f"[date_change_close] (res){res} (mid){mid} (change){change}")

    def update_atx_order(self, acc, query, update_msg):
        order_info_collection = self.order_info_db[acc]['atx_order']
        order_update_msg = {"$set" : update_msg}
        res = order_info_collection.update_one(query, order_update_msg)
        self.logger.info(f"[update_atx_order] update_atx_order")
        return res




