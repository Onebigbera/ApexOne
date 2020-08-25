# -*-coding:utf-8 -*-

"""
    管理其他的测试用例
"""
import unittest
from BSTestRunner import BSTestRunner
import time
from functionG import latest_report, send_mail
import os
from common.logging_handler import logging

root_dir = os.path.dirname(os.path.dirname(__file__))
reports_dir = '/'.join((root_dir, 'reports'))
test_dir = '/'.join((root_dir, 'testCase'))


def run_test():
    logging.info("======Start to test=====")
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_index.py")

    # 字符串化时间
    now = time.strftime("%Y-%m-%d_%H_%M_%S")

    # 拼接生成测试汇报的路径
    report_name = reports_dir + '/' + now + "result.html"

    with open(report_name, 'wb') as fw:
        runner = BSTestRunner(stream=fw, title="ApexOne_Index_report", description="Index_Test")
        runner.run(discover)
        fw.close()
    print("End test...")

    # 查找最新报告,获取到最新报告路径
    print("查找最新报告...")
    latest_report_file = latest_report(reports_dir)

    # 邮件发送报告
    print("邮件发送测试报告...")
    send_mail(latest_report_file)
    print("邮件发送完成...")


if __name__ == "__main__":
    run_test()
