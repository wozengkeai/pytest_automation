# -*- coding: utf-8 -*-
# @Time : 2022/1/6 15:57
# @Author : zengxiaoyan
# @File : debugtalk.py

"""
自定义方法，yaml里调用的额外函数
"""
import hashlib
import random
import string
from pathlib import Path

import yaml
# from params.yaml_util import *


#从params.yaml_util导入造成循环
def read_yaml(yaml_name,key):
    with open(str(Path.cwd())+'\\'+yaml_name,mode='r',encoding='utf-8') as f:
        value = yaml.load(f,Loader=yaml.FullLoader)
        print(value)
        return value[key]
# #
# if __name__ == '__main__':
#     print(read_yaml('extract.yaml','token'))