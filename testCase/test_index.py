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
from ddt import ddt, data, unpack
from data.Index import Tip_Shipment

root_dir = os.path.dirname(os.path.dirname(__file__))
screenshots_dir = '/'.join((root_dir, 'reports', 'screenShots'))


class IndexTest(StartEnd):
    """
    页面登陆
    """

    @data(*Tip_Shipment)
    def test_search_shipment(self,ship):
        """search shipment"""
        logging.info("---------------------------test Index Page begin------------------------------------")
        # print("test_login1_normal is start run...")
        po = IndexPage(self.driver)
        po.search_shipment(ship['hawb'])
        sleep(2)
        self.driver.get_screenshot_as_file(screenshots_dir + "\\test1.png")

        # 断言与截屏
        self.assertEqual(po.get_tip_msg(), ship['tip'])
        # 截图失败
        # insert_img(self.driver, "login_normal.png")
        logging.info("=====test hawb {}' tip is {}=====".format(ship['hawb'], ship['tip']))
        time.sleep(2)

    # @unittest.skip("Just skip...")
    # def test_01_search_shipment_not_exist(self):
    #     """hwab shipment doesn't exist"""
    #     logging.info("---------------------------test Index Page begin------------------------------------")
    #     # print("test_login1_normal is start run...")
    #     po = IndexPage(self.driver)
    #     po.search_shipment("dasd23213124543")
    #     sleep(2)
    #     self.driver.get_screenshot_as_file(screenshots_dir + "\\test1.png")
    #
    #     # 断言与截屏
    #     self.assertEqual(po.get_tip_msg(), "This shipment doesn’t exist")
    #     # 截图失败
    #     # insert_img(self.driver, "login_normal.png")
    #     logging.info("=====test hawb {hawb} not exist end=====".format(hawb="dasd23213124543"))
    #     time.sleep(2)

    # def test_02_search_shipment__no_logistics(self):
    #     """hwab shipment doesn't exist"""
    #     logging.info("=====test Index Page begin=====")
    #     # print("test_login1_normal is start run...")
    #     po = IndexPage(self.driver)
    #     po.search_shipment("SZXTS2008022")
    #     sleep(2)
    #     self.driver.get_screenshot_as_file(screenshots_dir + "\\test2.png")
    #
    #     # 断言与截屏
    #     self.assertEqual(po.get_tip_msg(), "No logistics information for this shipment yet")
    #     time.sleep(2)
    #     # 截图失败
    #     # insert_img(self.driver, "login_normal.png")
    #     logging.info(
    #         "=====test hawb {hawb} exist but does not have logistics information=====".format(hawb="SZXTS2008022"))


if __name__ == "__main__":
    unittest.main()
