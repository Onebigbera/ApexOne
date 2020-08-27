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


class IndexPage(BasePage):
    """
    首页登陆页面相关的类-继承页面基类
    """
    url = ''

    """
        定位器 元祖形式封装,这是按照页面上元素定位封装的这里为登陆输入定位器，当页面上元素改变时，只需要修改定位器即可 
    """
    hawb_input_loc = (By.ID, 'searchInput')
    search_btn = (By.XPATH, "//div[@class='btn']")
    not_exist_tip = (By.XPATH, '//div/p')
    no_logistics_tip = (By.XPATH, '//div/p')

    def search_shipment(self, hawb):
        self.open()
        self.find_element(*self.hawb_input_loc).clear()
        self.find_element(*self.hawb_input_loc).send_keys(hawb)
        self.find_element(*self.search_btn).click()
        self.find_element(*self.not_exist_tip)

    def get_tip_msg(self):
        """
        返回分单不存在或者没有物流消息的页面提示信息
        :return:
        """
        return self.find_element(*self.not_exist_tip).text

    """
        定义所有类型查找结果
    """
    loginPass_loc = (By.ID, "AHome")
    loginFail_loc = (By.CLASS_NAME, 'field-validation-error')

    def type_loginPass_hint(self):
        """
        检查用户是否登陆成功，照样在参数中可以使用 *self.loginPass_loc定位器
        :return: 获取到定位器元素的文本, 用于断言判断，主要是用来做断言判断
        """
        return self.find_element(*self.loginPass_loc).text

    def type_loginFail_hint(self):
        """
        根据已经设定了的登陆失败的定位器属性-文本做登陆失败判断断言，如果登陆失败，就会重新回到登陆页面 根据定位器得到的值
        :return:
        """
        return self.find_element(*self.loginFail_loc).text


# ---------------------------------------------------------使用继承的方式------------------------------------------------
class IndexPage1(BasePage):

    def search_shipment(self, hwab):
        """
        搜寻分单功能
        :param hwab:
        :return:
        """
        exp = "Index界面中未登录状态下搜索分单功能"
        self.wait_eleVisible(IndexPageLocator.hawb_input_loc)
        self.clear_input(IndexPageLocator.hawb_input_loc,exp=None)
        self.input_text(IndexPageLocator.hawb_input_loc, hwab, exp='search hawb')
        self.click_element(IndexPageLocator.search_btn, exp='locate search button')

    def get_tip_mes_not_exist(self):
        """
        当输入航班信息不存在或者航班物流信息不存在时，系统会给出对应的提示信息
        :return:
        """
        # WebDriverWait(self.driver, 20).until(
        #     EC.visibility_of_element_located((By.XPATH, '//div[@class="form-error-info"]')))
        # return self.driver.find_element_by_xpath('//div[@class="form-error-info"]')

        # 此处要求传入的就是元组，不需要解包，所以不需要使用*
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(IndexPageLocator.not_exist_tip))
        # 此处中要求传入值为元组中的元素，需要使用*进行解包
        return self.get_text(IndexPageLocator.not_exist_tip)

    def get_tip_mes_no_logistic(self):
        """
        当输入航班信息不存在或者航班物流信息不存在时，系统会给出对应的提示信息
        :return:
        """
        # WebDriverWait(self.driver, 20).until(
        #     EC.visibility_of_element_located((By.XPATH, '//div[@class="form-error-info"]')))
        # return self.driver.find_element_by_xpath('//div[@class="form-error-info"]')

        # 此处要求传入的就是元组，不需要解包，所以不需要使用*
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(IndexPageLocator.no_logistics_tip))
        # 此处中要求传入值为元组中的元素，需要使用*进行解包
        return self.get_text(IndexPageLocator.no_logistics_tip)
