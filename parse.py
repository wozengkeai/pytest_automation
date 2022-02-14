# -*- coding: utf-8 -*-
# @Time : 2022/1/19 10:21
# @Author : zengxiaoyan
# @File : parse.py
import re
from pprint import pprint
from typing import Text
from pathlib import Path
from common import log
from debugtalk import *
class ReadYamlRender:
    #$var
    variable_regexp = r"\$([\w_]+)"  # 变量
    #${func()}
    function_regexp = "\$\{([\w_]+\([\$\w\.\-_ =,']*\))\}"
    # function_regexp = "\$\{.*\(.*\)\}"

    functions = {}
    def __init__(self):
        self.log = log.MyLog()

    def get_data(self,yaml_name):
        """
        获取yaml内容
        :return:
        """
        with open(str(Path.cwd())+'\\params\\'+yaml_name,mode='r',encoding='utf-8') as f:
            # value = yaml.load(f,Loader=yaml.FullLoader)
            value = f.read()
            return value

    def extract_functions(self,content: Text):
        """
        获取函数${}中的值-函数名
        :param content:
        :return:
        """
        try:
            result = re.findall(self.function_regexp, content)
            return result
        except TypeError:
            return []

    def extract_variables(self,content: Text):
        """
        提取变量$var的值
        :param content:
        :return:
        """
        try:
            return re.findall(self.variable_regexp, content)
        except TypeError:
            return []


    def content_function(self,ymlcontent):
        """
        渲染变量,输出转化后的值
        :return:
        """
        #获取yml文件内容
        # ymlcontent = self.get_data('login\\pwdLogin.yml')
        # self.log.info('yml文件内容' + ymlcontent)
        #获取函数变量 ['gen_random_string(1)', 'gen_random_string(2)']
        funcnames = self.extract_functions(ymlcontent)
        csv_varname = []
        csv_value = []
        for func in funcnames:
            funcname = func.split('(', 1)
            # 判断是否有参数化
            if funcname[0] in ["parameterize", "P"]:
                path = funcname[1].split(')')[0]
                csv_content_list = read_csv_file(path)
                # 获取第一行字段名称，第二行开始是值
                csv_varname = csv_content_list[0]
                csv_value = csv_content_list[1:]
            else:
                try:
                    value = eval(func)   #将字符串转为python的表达式，并输出结果
                except Exception as error:
                    self.log.error('查不到有效函数: %s'%(error))
                    continue

                func = "${" + func + "}"
                if func == ymlcontent:
                    ymlcontent = value
                else:
                    ymlcontent = ymlcontent.replace(func,str(value),1)


        #获取变量名
        varnames = self.extract_variables(ymlcontent)
        for var in varnames:
            try:
                value = eval(var)
                strvalue = str(value)
            except Exception as error:
                self.log.error('查不到有效变量: %s' % (error))
                continue

            var = "$" + var
            if var == ymlcontent:
                ymlcontent = strvalue
            else:
                ymlcontent = ymlcontent.replace(var,strvalue,1)

        # 转为yml格式
        list2yml = yaml.load(ymlcontent, Loader=yaml.FullLoader)
        csv_varlen = len(csv_value)
        if csv_varlen > 0:
            for i in range(0, csv_varlen):
                # 备份yml内容进行内容替换
                changecontent = ymlcontent
                for csv_var in varnames:
                    value_index = csv_varname.index(csv_var)
                    csv_var = "$" + csv_var
                    changecontent = changecontent.replace(csv_var, csv_value[i][value_index], 1)
                if i == 0:
                    # 第一次参数化不需要新增，而是覆盖之前的用例
                    list2yml = []
                changecontentlist = yaml.load(changecontent, Loader=yaml.FullLoader)
                list2yml.extend(changecontentlist)
        return list2yml




if __name__ == '__main__':
    # value = ReadYamlRender().get_data('\\anonymousLogin.yml')

    ReadYamlRender().content_function()