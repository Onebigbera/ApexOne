# -*-coding:utf-8 -*-
"""
    获取config/
"""
import configparser
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
config_dir = '/'.join((root_dir, 'config'))
data_dir = '/'.join((config_dir, 'config_data.ini'))


def get_config_data():
    config = configparser.RawConfigParser()
    path = data_dir
    config.read(path)

    # 读取数据库信息
    host = config.get('dev_readonly_MySQL', 'host')
    user = config.get('dev_readonly_MySQL', 'user')
    pwd = config.get('dev_readonly_MySQL', 'pwd')
    db = config.get('dev_readonly_MySQL', 'db')
    port = config.get('dev_readonly_MySQL', 'port')
    ssl = config.get('dev_readonly_MySQL', 'ssl')

    # 读取邮件发送相关配置信息
    smtpServer = config.get('Email_Server', 'smtpServer')
    account_sender = config.get('Email_Server', 'account_sender')
    password_sender = config.get('Email_Server', 'password_sender')
    account_receiver = config.get('Email_Server', 'account_receiver')
    password_receiver = config.get('Email_Server', 'password_receiver')

    # 读取服务器信息
    base_url = config.get('server', 'url')

    config_db = {
        'host': host,
        'user': user,
        'pwd': pwd,
        'db': db,
        'port': port,
        'ssl': ssl
    }

    config_email = {
        'smtpServer': smtpServer,
        'account_sender': account_sender,
        'password_sender': password_sender,
        'account_receiver': account_receiver,
        'password_receiver': password_receiver
    }

    config_server = {
        'base_url': base_url
    }
    config_data_dict = {'DB': config_db, 'Email': config_email, 'Server': config_server}

    return config_data_dict


config_data = get_config_data()

if __name__ == "__main__":
    get_config_data()
