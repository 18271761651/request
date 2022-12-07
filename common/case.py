# -*- coding:utf-8 -*-
# user:Liukang

from request.common.request_util import ReuqestsUtil
from request.common.parameter_setting import ParametterSetting
from request.common.assert_ import Assert
from request.common.log import Logging
def case_assert_result(case_data):
    api_response=ReuqestsUtil.send_request(
        method=case_data['request']['method'],
        api=case_data['request']['api'],
        json=case_data['request']['data'])
    # print(api_response.request.body)
    extract_key=case_data['extract']
    Logging.loger().info(f"提取参数表达式{extract_key}")
    if extract_key:
        extract_value=ParametterSetting.extract_value(api_response.json(),extract_key)
        ParametterSetting.parameter_setting(extract_value,'save')
    return Assert.assert_response(case_data['assert_expression'],api_response.json())