# -*- coding:utf-8 -*-
# user:Liukang
import jsonpath
from jsonpath import jsonpath
class ParametterSetting:
    access_value={}

    @classmethod
    def data_is_replace(cls,data):
        '''
        :param data:请求参数data和提取参数extract_key
        :return: 返回参数是否被替换
        '''
        if not data:
            return False
        for k,v in data.items():
            if '$.' in v:
                return True
        return False

    @classmethod
    def parameter_setting(cls,data:dict,type='get'):
        '''
        :param data:返回结果提取和参数依赖使用dict例：{'bi11':'$.bi11'}
        :param type:save：把数据存到参数池里面无返回，get读取参数池数据并返回新值
        :return:
        '''
        if type == 'get':
            for k,v in data.items():
                if '$.' in v:
                    try:
                        v = jsonpath(cls.access_value,v)[0]
                        data[k]=v
                    except Exception:
                        print(f'jsonpath未读取到值，请检查')
                return data
        elif type == 'save':
            for k,v in data.items():
                cls.access_value[k] = v

    @classmethod
    def extract_value(cls,api_response:dict,extract_key:dict):
        '''
        :param api_response:
        :param extract_key:{'billCommonNo':'$.content.billCommonNo'}提取参数字典
        :return:
        '''
        extract_value={}
        for k,v in extract_key.items():
            extract_value[k]=jsonpath(api_response,v)
        # print(extract_value)
        return extract_value

if __name__ == '__main__':
    # a={'d':999}
    # ParametterSetting.parameter_setting(a,'save')
    # print(ParametterSetting.access_value)
    #
    # b={'dd':'$.d'}
    # print(ParametterSetting.parameter_setting(b))

    res={'businessStatus': 1, 'message': '', 'data': {'encryptedAccessToken': 'FvCDQ8Tzo'}}
    extract={"encryptedAccessToken":"$..encryptedAccessToken"}
    ParametterSetting.extract_value(res,extract)