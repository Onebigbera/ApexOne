# -*-coding:utf-8 -*-
"""
    获取driver
"""
from selenium import webdriver
import os
from time import sleep

root_path = os.path.dirname(os.path.dirname(__file__))
driver_dir = '/'.join((root_path, 'driver'))
driver_path = '/'.join((driver_dir, 'chromedriver.exe'))


class GetDriver(object):
    # def __init__(self, driver_path=r'E:/Auto_Test/Apex_One/driver/chromedriver.exe'):
    def __init__(self, driver_path=driver_path):
        self.driver_path = driver_path

    def get_driver(self):
        chrome_driver = webdriver.Chrome(executable_path=self.driver_path)
        return chrome_driver


driver = GetDriver().get_driver()

if __name__ == "__main__":
    print(driver_path)
    driver_hander = GetDriver()
    driver = driver_hander.get_driver()
    driver.get("https://www.baidu.com")
    sleep(3)
    driver.close()
    driver.quit()


