# -*- coding: utf-8 -*-
# @Time : 2022/1/5 10:11
# @Author : zengxiaoyan
# @File : run.py
import pytest
import os
import time

from params.yaml_util import read_testcase_yaml

if __name__ == '__main__':
    pytest.main()
    # read_testcase_yaml('anonymousLogin.yml')
    # time.sleep(1)
    # os.system('allure generate ./temp -o ./report --clearn')