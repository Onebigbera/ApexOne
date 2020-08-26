# -*- coding:utf-8 -*-
"""
    将元素定位和元素操作进行分离解耦，此文件只用来管理元素的定位，IndexPage页面管理元素定位操作
"""
from selenium.webdriver.common.by import By


class IndexPageLocator(object):
    """管理IndexPage需要用到的元素定位器"""
    hawb_input_loc = (By.ID, 'searchInput')
    search_btn = (By.XPATH, "//div[@class='btn']")
    not_exist_tip = (By.XPATH, '//div/p')
    no_logistics_tip = (By.XPATH, '//div/p')
