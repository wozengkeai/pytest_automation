# -*- coding: utf-8 -*-
# @Time : 2022/1/4 16:31
# @Author : zengxiaoyan
# @File : conftest.py
from urllib import parse

import pytest

from common.request_util import RequestUtil
from common.util import get_secret
from params.yaml_util import *



#在所有接口请求之前执行
@pytest.fixture(scope='session',autouse=True)
@pytest.mark.run(order=1)
def clear_extract():
    clear_yaml('\\extract.yaml')

@pytest.fixture(autouse=True)
def des():
    print("-----------------test开始")
    yield
    print("------------------test结束")



