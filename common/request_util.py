# -*- coding: utf-8 -*-
# @Time : 2022/1/6 14:16
# @Author : zengxiaoyan
# @File : request_util.py
"""
封装request
"""

import json

import requests

from common import log


class RequestUtil:
    #类变量，通过类名访问
    session = requests.Session()
    session.trust_env = False    #跳过代理

    def __init__(self):
        self.log = log.MyLog()

    def send_request(self,method,url,data,**kwargs):
        method = str(method).lower()
        # rep = None
        if method == 'get':
            rep = RequestUtil.session.request(method,url=url,params=data,**kwargs)
        elif method == 'post':
            #无论传的是data还是json，全部转化为data格式
            data = json.dumps(data)
            self.log.info("请求参数：%s"%(data))
            rep = RequestUtil.session.request(method, url=url, data=data, **kwargs)

        else:
            rep = RequestUtil.session.request(method, url=url, **kwargs)
        return rep.text