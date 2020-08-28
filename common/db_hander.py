# -*-coding:utf-8 -*-
"""
    mysql数据库连接组件
"""
import pymysql
from config_handler import config_data
from logging_handler import logger


class DbMySQL(object):
    """
        pymysql生产只读库 数据库连接
        注意:使用configparser解析出来的数据都是字符串，需要还原其类型（如数值、字典），使用eval()函数即可

    """

    def __init__(self, host=config_data['DB']['host'], user=config_data['DB']['user'], pwd=config_data['DB']['pwd'],
                 db=config_data['DB']['db'], port=config_data['DB']['port'],
                 ssl=config_data['DB']['ssl']):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.port = eval(port)
        self.ssl = eval(ssl)

    def __connect_db(self):
        if not self.db:
            logger.error("缺少数据库信息，请检查")
            raise (NameError, "没有设置数据库信息，请检查数据库是否正常")
        else:
            try:
                logger.info("************开始连接MySQL数据库*****************")
                logger.info("连接中.......")
                self.db = pymysql.connect(host=self.host, user=self.user, password=self.pwd, port=self.port,
                                          database=self.db, ssl=self.ssl)
                logger.info("************成功连接MySQL数据库*****************")
                self.cursor = self.db.cursor()
                return self.cursor
            except pymysql.err.OperationalError as e:
                logger.error("MySQL 连接失败，请检查是否连接VPN，错误信息{}".format(e))

    def select_data(self, sql, data=None):
        cursor = self.__connect_db()
        try:
            cursor.execute(sql)
            result = self.cursor.fetchone()
            print(result)
            return result
        except AttributeError:
            logger.error("************数据库未连接，请连接上数据库再查询************")


if __name__ == "__main__":
    db_uat = DbMySQL()
    # sql = "select sla_date,ata,pod_name,pod_code,pol_name,pol_code,atd,shipper_city,cargo_received_time from t_shipment_house where house_no='LAXTS01551';"
    sql = "select DATE_FORMAT(sla_date,'%b %d, %Y %I:%i %p') from t_shipment_house where house_no='LAXTS01551';"
    result = db_uat.select_data(sql)
    print(type(result[0]))


