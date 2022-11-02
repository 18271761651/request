# -*- coding:utf-8 -*-
# user:Liukang

import requests

class ReuqestsUtil:
    '''所有请求使用同一个会话'''
    session=requests.session()

    def send_request(self,method,url,**kwargs):
        method=str(method).lower()  # 转小写
        return self.session.request(method,url = url,**kwargs)
