# -*- coding: utf-8 -*-
# @Time : 2022/1/6 14:16
# @Author : zengxiaoyan
# @File : request_util.py
"""
封装request
"""

import json

import requests
class RequestUtil:
    #类变量，通过类名访问
    session = requests.Session()
    session.trust_env = False    #跳过代理

    def send_request(self,method,url,data,**kwargs):
        method = str(method).lower()
        # rep = None
        if method == 'get':
            rep = RequestUtil.session.request(method,url=url,params=data,**kwargs)
        elif method == 'post':
            #无论传的是data还是json，全部转化为data格式
            data = json.dumps(data)
            rep = RequestUtil.session.request(method, url=url, data=data, **kwargs)
            print(rep.request.body)
        else:
            rep = RequestUtil.session.request(method, url=url, **kwargs)
        return rep.text