# -*-coding:utf-8 -*-
"""
    logging 模块
"""

import logging.config
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
print(root_dir)
# config_path = os.path.join(root_dir, 'config', 'log.conf')
config_path = '/'.join((root_dir, 'config', 'log.conf'))

# 实例化 logging
CON_LOG = config_path
logging.config.fileConfig(CON_LOG)
logger = logging.getLogger()
