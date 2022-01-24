# -*- coding: utf-8 -*-
# @Time : 2022/1/19 10:21
# @Author : zengxiaoyan
# @File : parse.py
import re
from typing import Text
from pathlib import Path
from debugtalk import *
class ReadYamlRender:
    #$var
    variable_regexp = r"\$([\w_]+)"  # 变量
    #${func()}
    function_regexp = "\$\{([\w_]+\([\$\w\.\-_ =,']*\))\}"
    # function_regexp = "\$\{.*\(.*\)\}"
    #${${}}
    function_regexp_compile = re.compile(r"^([\w_]+)\(([\$\w\.\-_ =,]*)\)$")
    functions = {}

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
        # ymlcontent = self.get_data('\\pwdLogin.yml')

        #获取函数变量 ['gen_random_string(1)', 'gen_random_string(2)']
        funcnames = self.extract_functions(ymlcontent)
        for func in funcnames:
            # print(func)
            # self.functions = func
            try:
                value = eval(func)   #将字符串转为python的表达式，并输出结果
                print(value)
                if value == None:
                    print('do not find this value')
            except Exception:
                continue

            func = "${" + func + "}"
            if func == ymlcontent:
                ymlcontent = value
            else:
                ymlcontent = ymlcontent.replace(func,str(value),1)


        #获取变量名
        varnames = self.extract_variables(ymlcontent)
        for var in varnames:
            value = eval(var)
            strvalue = str(value)
            if strvalue.startswith('<') and strvalue.endswith('>'):
                strvalue = 'do not find this varname'
            var = "$" + var
            # print(var)
            if var == ymlcontent:
                ymlcontent = strvalue
            else:
                ymlcontent = ymlcontent.replace(var,strvalue,1)
        print('ymlcontent')
        print(ymlcontent)
        return ymlcontent




if __name__ == '__main__':
    # value = ReadYamlRender().get_data('\\anonymousLogin.yml')
    # content = ReadYamlRender().extract_functions(value)
    # print(content)
    # for func in content:
    #     print(func)
    #     print(ReadYamlRender().parse_function(func))
    # print(ReadYamlRender()._eval_content_functions(value))
    ReadYamlRender().content_function()