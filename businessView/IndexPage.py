# -*-coding:utf-8 -*-

"""
    封装继承Page类的页面类
    定位器封装
"""
import time

from baseView.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageLocator.indexPage_Locators import IndexPageLocator
import requests, json


class IndexPage(BasePage):

    def search_shipment(self, hwab):
        """
        搜寻分单功能
        :param hwab:分单号
        :return:
        """
        exp = "Index界面中未登录状态下搜索分单功能"
        self.wait_eleVisible(IndexPageLocator.hawb_input_loc)
        self.clear_input(IndexPageLocator.hawb_input_loc, exp=None)
        self.input_text(IndexPageLocator.hawb_input_loc, hwab, exp='search hawb')
        self.click_element(IndexPageLocator.search_btn, exp='locate search button')

    def get_tip_mes_not_exist(self):
        """
        当分单对应的航班信息不存在时系统会给出对应的提示信息
        :return:
        """
        # 此处要求传入的就是元组，不需要解包，所以不需要使用*
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(IndexPageLocator.not_exist_tip))
        return self.get_text(IndexPageLocator.not_exist_tip)

    def get_tip_mes_no_logistic(self):
        """
        当分单对应的航班存在但是不存在物流信息时系统会给出对应的提示信息
        :return:
        """
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(IndexPageLocator.no_logistics_tip))
        return self.get_text(IndexPageLocator.no_logistics_tip)

    def check_exist_data(self, hawb):
        """
        核对已经存在的
        :param hawb:
        :return:
        """
        exp = "核对已经存在的分单基本信息"
        self.search_shipment(hawb)


class GetDetail(object):
    """
    当分单存在物流信息时，使用request库解析得到Index界面中展示的数据
    """

    def __init__(self, hwab):
        """
            hawb:分单号
        """
        self.hawb = hwab

    def get_result(self):
        """
        获取接口信息
        """

