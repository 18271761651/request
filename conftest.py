# -*- coding:utf-8 -*-
# user:Liukang
import pytest
from request.common.yaml_util import YamlUtil

'''autouse 自动执行，scope 作用域'''

@pytest.fixture(scope='function')
def conn_database():
    print('连接数据库')
    yield
    print('\n关闭数据库')

@pytest.fixture(scope='session',autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()