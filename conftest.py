# -*- coding:utf-8 -*-
# user:Liukang
import pytest,pymysql
from request.common.yaml_util import YamlUtil

'''scope 作用域，autouse 自动执行，'''
@pytest.fixture(scope='function')
def conn_database():
    connect = pymysql.connect(host='localhost',
                              port=3306,
                              user='root',
                              password='123456',
                              charset='utf8',
                              database='demo')
    while True:
        try:
            cursor = connect.cursor()
            sql = "select * from admin"
            cursor.execute(sql)
            print(cursor.fetchall())
            break
        except Exception as error:
            print(error)
            connect.ping(True)
    yield
    connect.close()

@pytest.fixture(scope='session',autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()