# -*- coding: utf-8 -*-
# @Time : 2022/1/4 16:31
# @Author : zengxiaoyan
# @File : conftest.py
from urllib import parse

import pytest
from pytest import skip

from params.yaml_util import *



#在所有接口请求之前执行
@pytest.fixture(scope='session',autouse=True)
def clear_extract():
    clear_yaml('\\extract.yaml')

@pytest.fixture(autouse=True)
def des():
    print("test开始")

# empty_parameter_set_mark = skip

