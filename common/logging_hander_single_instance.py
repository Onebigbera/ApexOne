# -*-coding:utf-8 -*-
"""
    logging模块
"""
import logging
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
log_dir = '/'.join((root_dir, 'logs'))
logger_path = '/'.join((log_dir, 'logger.log'))


class Log(object):
    __flag = None

    def __new__(cls, *args, **kwargs):
        if not cls.__flag:
            cls.__flag = super().__new__(cls)
            # 新创建后__flag就不为None
            # a = "Not None" if cls.__flag != None else "None"
            # print(a)
        return cls.__flag

    def __init__(self):
        if 'logger' not in self.__dict__:
            logger = logging.getLogger()
            logger.setLevel(level=logging.DEBUG)
            filehandle = logging.FileHandler(logger_path, encoding='utf-8')
            streamhandle = logging.StreamHandler()
            logger.addHandler(filehandle)
            logger.addHandler(streamhandle)
            format = logging.Formatter('%(asctime)s:%(levelname)s:%(lineno)s %(message)s')
            filehandle.setFormatter(format)
            streamhandle.setFormatter(format)

            self.logger = logger

    def return_logger(self):
        return self.logger


def get_logger():
    return Log().return_logger()


# 返回单例logger
logger = get_logger()

if __name__ == '__main__':
    logger = get_logger()
    logger.error('Oh,My God,there is a problem!')
