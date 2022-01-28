# -*- coding: utf-8 -*-
# @Time : 2022/1/6 15:57
# @Author : zengxiaoyan
# @File : debugtalk.py

"""
自定义方法，yaml里调用的额外函数
"""
import csv
from pathlib import Path
from typing import Text, List
import yaml


#从params.yaml_util导入造成循环
def read_yaml(yaml_name,key):
    with open(str(Path.cwd())+'\\'+yaml_name,mode='r',encoding='utf-8') as f:
        value = yaml.load(f,Loader=yaml.FullLoader)
        print(value)
        return value[key]

#读取csv文件内容
def read_csv_file(csv_file: Text) -> List:
    csv_content_list = []

    with open(str(Path.cwd())+'\\params\\csvdata\\'+ csv_file, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_content_list.append(row)

    return csv_content_list

# if __name__ == '__main__':
#     print(read_yaml('extract.yaml','token'))