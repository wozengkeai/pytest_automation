# -*- coding: utf-8 -*-
# @Time : 2022/1/6 16:17
# @Author : zengxiaoyan
# @File : test_login.py
import json
import logging
from pprint import pprint

import pytest

# from common.config import Config
from common.request_util import RequestUtil
from common.util import get_secret
from params.yaml_util import *



class TestLogin:
    """
    登陆接口用例
    """
    @pytest.mark.parametrize('pwdinfo', read_testcase_yaml('pwdLogin.yml'))
    @pytest.mark.parametrize('confinfo', read_config())
    def test_login_pwdlogin(self,pwdinfo,confinfo):
        """
        登陆企业平台
        :param caseinfo:
        :param confinfo:
        :return:
        """
        host = confinfo['base']['business_url']
        url = host + pwdinfo['request']['url']
        headers = pwdinfo['request']['headers']
        data = pwdinfo['request']['json']
        method = pwdinfo['request']['method']

        req = RequestUtil().send_request(method, url, data, headers=headers)
        result = json.loads(req)
        pprint(result)
        # token = result['data']['access']['token']
        # write_yaml({"token": 'Bearer '+token},'extract.yaml')   #需要将token写入文件


    @pytest.mark.parametrize('confinfo',read_config())
    @pytest.mark.parametrize('anonymousinfo',read_testcase_yaml('anonymousLogin.yml'))
    def test_login_anonymousLogin(self,confinfo,anonymousinfo):
        """
        登录公司
        :return:
        """
        # anonymousinfo = read_testcase_yaml('anonymousLogin.yml')
        # print(anonymousinfo)
        host = confinfo['base']['business_url']
        url = host + anonymousinfo['request']['url']
        headers = anonymousinfo['request']['headers']
        pprint(headers)
        data = anonymousinfo['request']['json']
        method = anonymousinfo['request']['method']
        req = RequestUtil().send_request(method, url, data, headers=headers)
        result = json.loads(req)
        # pprint(result)
        # anonymous_token = result['data']['access']['token']
        # write_yaml({"anonymoustoken": 'Bearer ' + anonymous_token},'extract.yaml')


    @pytest.mark.parametrize('confinfo',read_config())
    @pytest.mark.parametrize('Menusinfo',read_testcase_yaml('Loginmenu.yml'))
    def test_login_getSingleLoginMenus(self,confinfo,Menusinfo):
        """
        获取子系统
        :return:
        """
        # Menusinfo = read_testcase_yaml('Loginmenu.yml')
        host = confinfo['base']['business_url']
        url = host + Menusinfo['request']['url']
        headers = Menusinfo['request']['headers']
        pprint(headers)
        data = Menusinfo['request']['json']
        method = Menusinfo['request']['method']
        req = RequestUtil().send_request(method, url, data, headers=headers)
        result = json.loads(req)
        # pprint(result)

        urllist = result['data']['list']
        urlcode = ''
        for i in range(len(urllist)):
            if urllist[i]['name'] == '价值系统':
                urlcode = urllist[i]['url']
        # print(urlcode)
        singlecode = get_secret(urlcode)
        # write_yaml({"singlecode":  singlecode}, 'extract.yaml')


    @pytest.mark.parametrize('logininfo',read_testcase_yaml('login.yml'))
    @pytest.mark.parametrize('confinfo',read_config())
    def test_login_01(self,confinfo,logininfo):
        host = confinfo['base']['base_url']
        url = host + logininfo['request']['url']
        headers = logininfo['request']['headers']
        data = logininfo['request']['json']
        method = logininfo['request']['method']
        req = RequestUtil().send_request(method,url,data,headers=headers)
        result = json.loads(req)
        # accessToken = result['data']['access']['accessToken']
        # write_yaml({"accessToken": accessToken},'extract.yaml')
