# -*-coding:utf-8 -*-

"""
    PO基类
        功能封装
        1. open() 打开网页
        2. find_element()  元素定位

"""
from time import sleep
from logging_handler import logging
from config_handler import config_data


class Page(object):
    """
    页面基础类
    """

    url = ""

    def __init__(self, driver):
        """
        Page类的属性
        self.base_url: 根url 页面基类的url
        :param driver: 浏览器驱动,在页面类中不需要打开浏览器，在测试用例中才需要打开
        """
        self.base_url = config_data['Server']['base_url']
        self.driver = driver
        self.timeout = 10

    def _open(self, url):
        """
        _var:project variable / __var: private variable
        var_ to avoid conflict with keyword variant
        :param url: 子页面的对应路由 在各个继承基类的子类中定义
        :return:
        """
        url_ = self.base_url + url
        logging.info("=====Now test url is {}=====".format(url_))
        print("Test page is: %s" % url_)
        self.driver.maximize_window()
        logging.info("=====Now try to maxsize page and url is {}=====".format(url_))
        self.driver.get(url_)
        sleep(2)
        try:
            assert self.driver.current_url == url_, 'Did not land on {}，Please Check'.format(url_)
        except AssertionError:
            logging.info("=====Did not land on the {}".format(url_))

    def open(self):
        """
        定义公有方法调用保护方法 打开页面
        self.url 对应页面的尾缀url链接，类属性
        :return:
        """
        self._open(self.url)

    def find_element(self, *loc):
        """
        定位器
        :param *loc:之所以使用*args传参，方便driver.find_element()进行解包
        :return:
        """
        return self.driver.find_element(*loc)
