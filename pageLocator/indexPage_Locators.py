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

    SLA_Date = (By.XPATH, "//div[@class='sla-date']/span")
    consignee = (By.XPATH, '//div[@class="result"]/div[@class="time-line"]/div[@class="step active"][1]/div[1]')
    podCode = (By.XPATH, '//div[@class="result"]/div[@class="time-line"]/div[@class="step active"][2]/div[1]')
    polCode = (By.XPATH, '//div[@class="result"]/div[@class="time-line"]/div[@class="step active"][3]/div[1]')
    shipper = (By.XPATH, '//div[@class="result"]/div[@class="time-line"]/div[@class="step"]/div[1]')
