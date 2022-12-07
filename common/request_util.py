# -*- coding:utf-8 -*-
# user:Liukang

import requests
from request.common import requests_enviroment_info
class ReuqestsUtil:
    '''所有请求使用同一个会话'''
    session=requests.session()
    @classmethod
    def send_request(self,
                     method,
                     api,
                     headers=requests_enviroment_info()['headers'],
                     **kwargs):
        method=str(method).lower()  # 转小写
        url=requests_enviroment_info()['ip']+api
        # print(url,headers)
        return self.session.request(method=method,url = url,headers=headers,**kwargs)

if __name__ == '__main__':
    ReuqestsUtil().send_request('get','/login')