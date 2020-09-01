# -*-coding:utf-8 -*-

"""
    测试登陆的类 测试对象就是继承BasePage的Loginpage的类,依照参照元素结合断言进行判断
    PO 将元素定位和页面操作对象分层封装，解耦便于操作和维护
    如果是测试登陆 就在写一个 test_register用例
"""
import time

from baseView.myunit import StartEnd
from functionG import insert_img
from businessView.IndexPage import IndexPage
from time import sleep
import unittest
from logging_handler import logging
import os
import ddt
from data.Index import shipment_not_exist, shipment_no_logistic, shipment_exist
from common.get_driver import driver
from common.config_handler import config_data
from pageLocator.indexPage_Locators import IndexPageLocator
from common.logging_handler import logger
import requests, json
from common.db_hander import DbMySQL

root_dir = os.path.dirname(os.path.dirname(__file__))
screenshots_dir = '/'.join((root_dir, 'reports', 'screenShots'))


@ddt.ddt
class IndexTest(unittest.TestCase):
    """
    在setUp()和tearDown()方法中设置打开和关闭浏览器（进程）能够实现测试用例之间的隔离性
    """

    @classmethod
    def setUpClass(cls):
        """
        类方法需要在方法前面加上@classmethod装饰器说明，要不然会报错
        可以实现功能如下: 通过excel读取本功能中需要的所有的测试数据

        :return:
        """
        logger.info("====**********************======TestCase Begin分隔符======*********************************====")
        logger.info("==========测试用例执行之前，setUpClass,整个测试类只执行一次==========")
        cls.driver = driver
        cls.driver.get(config_data['Server']['base_url'])
        cls.index_page = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        """
        在测试类执行完毕后，关掉浏览器进程
        :return:
        """
        logger.info("==========测试用例执行之前，tearDownClass,整个测试类只执行一次==========")
        logger.info("====********************************======TestCase End分隔符======**************************====")
        cls.driver.quit()

    def setUp(self):
        """
        每个测试用例的前置条件
        :return:
        """
        pass

    def tearDown(self):
        """
        每个测试用例的后置条件
        :return:
        """
        self.driver.refresh()

    @ddt.data(*shipment_not_exist)
    def test_search_hawb_not_exist(self, index_data):
        """
        分单不存在的数据都放执行此测试用例
        :return:
        """
        self.index_page.search_shipment(index_data['hawb'])
        self.assertEqual(self.index_page.get_tip_mes_not_exist(), index_data['tip'])
        time.sleep(3)

    @ddt.data(*shipment_no_logistic)
    def test_search_hawb_no_logistic(self, index_data):
        """
        分单不存在的数据都放执行此测试用例
        :return:
        """
        self.index_page.search_shipment(index_data['hawb'])
        self.assertEqual(self.index_page.get_tip_mes_no_logistic(), index_data['tip'])
        time.sleep(3)





if __name__ == "__main__":
    unittest.main()
