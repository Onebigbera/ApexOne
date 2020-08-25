# -*-coding:utf-8 -*-
"""
    logging 模块
"""

import logging.config
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
config_path = '/'.join((root_dir, 'config', 'log.conf'))

# 实例化 logging
CON_LOG = config_path
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()
