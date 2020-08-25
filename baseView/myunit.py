# -*-coding:utf-8 -*-
"""
    封装unittest中的每个测试用例setUp()和tearDown()方法
    将driver封装在了初始的unittest.TestCase里面，功能可以自行添加完善
"""
import unittest
from common.get_driver import driver


class StartEnd(unittest.TestCase):
    """ 定义每个测试用例的初始化和结束"""

    def setUp(self):
        """
        初始化driver, 获取driver等操作、连接数据库
        :return:
        """
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        """
        每个测试方法结束后的设置，比如关闭数据库
        :return:
        """
        self.driver.refresh()
        # self.driver.close()

