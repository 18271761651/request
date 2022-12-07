# -*- coding:utf-8 -*-
# user:Liukang
from request.config.config import Enviroment
from request.common.yaml_util import YamlUtil
def requests_enviroment_info():
    try:
        env_inf=YamlUtil.read_config_yaml()
        requests_info=env_inf[Enviroment]
        return {'ip':requests_info['http']+requests_info['domain_name'],'headers':requests_info['headers']}
    except Exception as e:
        print(f'读取配置文件出错,{e}')

if __name__ == '__main__':
    print(requests_enviroment_info())