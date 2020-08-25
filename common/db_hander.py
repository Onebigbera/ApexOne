# -*-coding:utf-8 -*-
"""
    mysql数据库连接组件
"""
import pymysql
from config_handler import config_data


class DbMySQL(object):
    """pymysql数据库连接
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
            raise (NameError, "没有设置数据库信息，请检查数据库是否正常")
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.pwd, port=self.port,
                                  database=self.db, ssl=self.ssl)
        self.cursor = self.db.cursor()
        return self.cursor

    '''
        def insert_data(self, sql, data=None):
            self.cursor.execute(sql)
            self.db.commit()
    '''

    def select_data(self, sql, data=None):
        cursor = self.__connect_db()
        cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result[0])
        return result[0]


if __name__ == "__main__":
    db_uat = DbMySQL()
    sql = "select max(id) from t_export_flight_space_info"
    db_uat.select_data(sql)
