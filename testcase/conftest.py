# -*- coding: utf-8 -*-
# @Time : 2022/1/4 16:31
# @Author : zengxiaoyan
# @File : conftest.py
from urllib import parse

import pytest
import requests

from common.request_util import RequestUtil
from common.util import get_secret
from params.yaml_util import *



#在所有接口请求之前执行
@pytest.fixture(scope='session',autouse=True)
# @pytest.mark.run(order=1)
def clear_extract():
    clear_yaml('\\extract.yaml')

@pytest.fixture(autouse=True)
def des():
    print("-----------------test开始")
    yield
    print("------------------test结束")

@pytest.fixture(scope='session',autouse=True)
def complete_login():
    session = requests.Session()
    session.trust_env = False

    baseinfo = read_config()
    print(baseinfo)
    base_url = baseinfo[0]['base']['base_url']
    business_url = baseinfo[0]['base']['business_url']
    username = baseinfo[0]['base']['username']
    pwd = baseinfo[0]['base']['password']

    #登陆企业平台
    pwdlogin_url =business_url + '/auth/pwdLogin'
    pwdlogin_headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"
    }
    pwdlogin_data = {
        "username": str(username),
        "password": pwd
    }
    pwdlogin_resp = RequestUtil.session.request('POST',url=pwdlogin_url,json=pwdlogin_data,headers=pwdlogin_headers)
    # print(pwdlogin_resp.text)
    token = pwdlogin_resp.json()['data']['access']['token']
    write_yaml({"token": 'Bearer ' + token}, 'extract.yaml')

    #登陆公司
    anonymousLogin_url = business_url + '/auth/anonymousLogin'
    anonymousLogin_headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
        "Authorization": read_yaml('extract.yaml','token')
    }
    anonymousLogin_data = {
        "companyId": 382
    }
    anonymousLogin_resp = RequestUtil.session.request('POST',url=anonymousLogin_url,json=anonymousLogin_data,headers=anonymousLogin_headers)
    # print(anonymousLogin_resp.text)
    anonymous_token = anonymousLogin_resp.json()['data']['access']['token']
    write_yaml({"anonymoustoken": 'Bearer ' + anonymous_token}, 'extract.yaml')

    #获取子系统
    menu_url = business_url + '/auth/getSingleLoginMenus'
    menu_headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
        "Authorization": read_yaml('extract.yaml', 'anonymoustoken')
    }
    menu_data = {}
    menu_resp = RequestUtil.session.request('POST',url=menu_url,headers=menu_headers,json=menu_data)
    # print(menu_resp.text)
    urllist = menu_resp.json()['data']['list']
    urlcode = ''
    for i in range(len(urllist)):
        if urllist[i]['name'] == '价值系统':
            urlcode = urllist[i]['url']
    singlecode = get_secret(urlcode)
    write_yaml({"singlecode": singlecode}, 'extract.yaml')

    #登录
    login_url = base_url + '/auth/login'
    login_headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
        "Authorization": read_yaml('extract.yaml', 'anonymoustoken')
    }
    login_data = {
        "code": read_yaml('extract.yaml','singlecode')
    }
    login_resp = RequestUtil.session.request('POST',url=login_url,headers=login_headers,json=login_data)
    # print(login_resp.text)
    accessToken = login_resp.json()['data']['access']['accessToken']
    write_yaml({"accessToken": accessToken}, 'extract.yaml')







