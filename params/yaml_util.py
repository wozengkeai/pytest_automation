# -*- coding: utf-8 -*-
# @Time : 2022/1/5 11:30
# @Author : zengxiaoyan
# @File : yaml_util.py
"""
封装传递yaml文件的方法
"""

# import os
import json

import yaml
from pathlib import Path
# from ReadYamlRender import ReadYamlRender
from parse import ReadYamlRender
from common import log

log = log.MyLog()



    #读取yml用例文件
def read_testcase_yaml(yaml_name):
    """
    读取yml文件，对yaml反序列化，就是把yaml格式转化为dict格式
    :return:
    """
    with open(str(Path.cwd())+'\\params\\login\\'+yaml_name,mode='r',encoding='utf-8') as f:
        # value = yaml.load(f,Loader=yaml.FullLoader)
        value = f.read()
        value = ReadYamlRender().content_function(value)

        # value = yaml.load(value, Loader=yaml.FullLoader)
        # print(type(value))
        return value

#写入yml文件
def write_yaml(data,yaml_name):
    with open( str(Path.cwd()) +'\\'+ yaml_name,mode='a',encoding='utf-8') as f:
        log.info("写入文件%s"%(data))
        yaml.dump(data=data,stream=f,allow_unicode=True)

#读取yaml文件
def read_yaml(yaml_name,key):
    with open(str(Path.cwd())+'\\'+yaml_name,mode='r',encoding='utf-8') as f:
        value = yaml.load(f,Loader=yaml.FullLoader)
        log.info("读取yml文件 %s"%(value))
        return value[key]

#清空yml文件
def clear_yaml(yaml_name):
    with open( str(Path.cwd()) + yaml_name,mode='w',encoding='utf-8') as f:
        # f.seek(0)
        log.info("清空yml文件")
        f.truncate()

# 读取配置文件
def read_config():
    with open(str(Path.cwd()) +'\\config.yaml', mode='r', encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        log.info("配置信息: %s"%(value))
        return value



if __name__ == '__main__':
    read_testcase_yaml('anonymousLogin.yml')
    # read_yaml('\\extract.yaml','token')