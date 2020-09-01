# -*- coding:utf-8 -*-
import time

import unittest
import os
import ddt
from data.Index import shipment_exist
from common.config_handler import config_data
from common.logging_handler import logger
import requests, json
from common.db_hander import DbMySQL

root_dir = os.path.dirname(os.path.dirname(__file__))
screenshots_dir = '/'.join((root_dir, 'reports', 'screenShots'))


class IndexDetail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("===============使用接口做自动化测试的前提是页面展示数据和接口提供的数据核对无误为前提=================")
        cls.db = DbMySQL()

    def setUp(self):
        self.base_url = config_data['Server']['search_url']

    def test_ata(self):
        data = {'hawbNo': 'LAXTS01677'}
        result = requests.post(config_data['Server']['search_url'], data=data, verify=False)
        detail_info = json.loads(result.text)
        ata = detail_info['data']['ata']
        logger.info("===============从接口中查询得到的ata为{}=============".format(ata))
        sql = "select DATE_FORMAT(ata,'%b %d, %Y %I:%i %p') from t_shipment_house where house_no='LAXTS01677';"
        ata_sql_result = self.db.select_data(sql)[0]
        logger.info("===============从数据库中查询得到的ata为{}=============".format(ata))
        self.assertEqual(ata, ata_sql_result)
