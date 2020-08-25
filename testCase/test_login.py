# -*-coding:utf-8 -*-

"""
    测试登陆的类 测试对象就是继承BasePage的Loginpage的类,依照参照元素结合断言进行判断
    PO 将元素定位和页面操作对象分层封装，解耦便于操作和维护
    如果是测试登陆 就在写一个 test_register用例
"""
from baseView.myunit import StartEnd
from functionG import insert_img
from businessView.LoginPage import LoginPage
from time import sleep
import unittest
from logging_handler import logging
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
screenshots_dir = '/'.join((root_dir, 'screenshots'))


class LoginTest(StartEnd):
    """
    页面登陆
    """

    # @unittest.skip("Just skip...")
    def test_login1_normal(self):
        """username password is normal"""
        logging.info("=====test login pxadmin begin=====")
        # print("test_login1_normal is start run...")
        po = LoginPage(self.driver)
        po.Login_action("pxadmin", "111111")
        sleep(5)
        self.driver.get_screenshot_as_file(screenshots_dir + "\\test.png")

        # 断言与截屏
        self.assertEqual(po.type_loginPass_hint(), "Home")
        # 截图失败
        # insert_img(self.driver, "login_normal.png")
        logging.info("=====test login {name} end=====".format(name="pxadmin"))

    # @unittest.skip("Just skip...")
    def test_login2_passwdError(self):
        """username is ok, passwd is error!"""
        logging.info("=====test login george end=====")
        print("test_login2_passwdError is start run...")
        po = LoginPage(self.driver)
        po.Login_action("george", "123456")
        sleep(5)

        # 断言与截图 登陆失败时按照定位器得到的值为""
        self.assertEqual(po.type_loginFail_hint(), '用户不存在！')
        insert_img(self.driver, "login2_fail.png")
        logging.info("=====test login {name} end=====".format(name="george"))

        print("test_login2_passwdError test end...")

    @unittest.skip("Just skip...")
    def test_login3_empty(self):
        """username and password are empty"""
        print("test_login3_empty is start run...")
        po = LoginPage(self.driver)
        po.Login_action("", "")
        sleep(4)

        # 断言与截图
        self.assertEqual(po.type_loginFail_hint(), '用户不存在！')
        insert_img(self.driver, "login3_empty.png")
        print("test_login3_empty test end...")


if __name__ == "__main__":
    unittest.main()
