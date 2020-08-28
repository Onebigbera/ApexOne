# -*- coding:utf-8 -*-
"""
    页面基类  所有业务页面的父类，封装一些页面的公用方法包含但是不仅限于:
        日志记录、异常处理、截图、元素定位、元素文本获取、元素属性获取、点击元素等
        优化调整：可以将函数中用到的重复部分使用装饰器进行优化
"""
import time
# from common.logging_hander_single_instance import logger
# from common.Logging_Optimiser import logger
from common.logging_handler import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
report_dir = '/'.join((root_dir, 'reports'))
screen_shot_dir = '/'.join((report_dir, 'screenShots'))


class BasePage(object):
    """
    页面基类，将日志和异常捕捉封装在页面基类自带的方法中，避免在测试用例类中重复造轮子
    """

    def __init__(self, driver):
        self.driver = driver

    def wait_eleVisible(self, locator, time=30, poll_frequency=0.5, exp=""):
        """
        等待元素页面可见
        :param locator:元素定位器
        :param time:等待总周期
        :param poll_frequency:检查频率，没0.5s检查一次
        :param exp:文档说明，方便记录
        :return:
        """
        logger.info("等待元素{}可见".format(locator))
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, time, poll_frequency).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            during_period = end - start
            logger.info("等待时长为:{}".format(during_period))
        except BaseException as e:
            # logger.info("The exception is {}".format(e))
            logger.exception(e)
            self.save_screenshot(exp)
            raise e

    def wait_elePresent(self, locator, time=30, poll_frequency=0.5, exp=""):
        """
        等待元素页面呈现
        :param locator:元素定位器
        :param time:等待总周期
        :param poll_frequency:检查频率，没0.5s检查一次
        :param exp:文档说明，方便记录
        :return:
        """
        logger.info("等待元素{}可见".format(locator))
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, time, poll_frequency).until(EC.presence_of_element_located(locator))
            end = datetime.datetime.now()
            during_period = end - start
            logger.info("等待时长为:{}".format(during_period))
        except BaseException as e:
            # logger.info("The exception is {}".format(e))
            logger.exception(e)
            self.save_screenshot(exp)
            raise e

    def get_element(self, locator, exp=''):
        """
            元素获取
            在参数中使用args,在函数中使用*args，会将args进行解包，比如如果args为(By.ID, 'searchInput')，那么使用*args就会将元组解包,脱掉外衣
        """
        logger.info("查找元素：{}".format(locator))
        try:
            self.driver.find_element(*locator)
            return self.driver.find_element(*locator)
        except BaseException as e:
            self.save_screenshot(exp)
            logger.exception(e)
            raise e

    def click_element(self, locator, exp):
        """点击元素
        点击元素的前提是定位元素，先定位元素再点击元素
        """
        ele = self.get_element(locator, exp='')
        logger.info("{0}点击元素:{1}".format(exp, locator))
        # 元素操作
        try:
            ele.click()
        except BaseException as e:
            self.save_screenshot(exp)
            logger.exception(e)
            raise e

    def clear_input(self, locator, exp):
        """清除输入框内容"""
        ele = self.get_element(locator, exp)
        try:
            ele.clear()
        except BaseException as e:
            logger.exception(e)
            self.save_screenshot(exp)
            raise e

    def input_text(self, locator, text, exp):
        """文本输入"""
        ele = self.get_element(locator, exp)
        try:
            ele.send_keys(text)
        except BaseException as e:
            logger.excption(e)
            self.save_screenshot(exp)
            raise e

    def get_text(self, locator, exp=''):
        """文本获取"""
        ele = self.get_element(locator, exp)
        try:
            return ele.text
        except BaseException as e:
            logger.excption("获取元素{}文本失败".format(locator))
            self.save_screenshot(exp)
            raise e

    def get_eleAttribute(self, locator, attr, exp):
        """获取属性"""
        ele = self.get_element(locator, exp)
        try:
            return ele.get_attribute(attr)
        except BaseException as e:
            logger.excption("获取元素{}属性失败".format(attr))
            self.save_screenshot(exp)
            raise e

    def alert_handle(self, action="accept"):
        """弹出框处理"""
        pass

    def switch_iframe(self):
        """iframe切换"""
        pass

    def upload_file(self):
        """文件上传"""
        pass

    def windows_switch(self):
        """窗口切换"""
        pass

    def scroll_bar_handle(self):
        """滚动条处理"""
        pass

    def save_screenshot(self, name):
        """截图操作
        图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png,将截图路径配置到配置文件中 todo: 优化截图配置文件写法

        """
        file_name = screen_shot_dir + '/' + "{0} {1}.png".format(name,
                                                                 time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
        try:
            self.driver.save_screenshot(file_name)
            logger.info("截取网页成功，截取文件路径为{}".format(file_name))
        except BaseException as e:
            logger.excption("截图失败，失败原因为{}".format(e))
            raise e
