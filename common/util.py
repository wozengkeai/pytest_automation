# -*- coding: utf-8 -*-
# @Time : 2022/1/21 13:54
# @Author : zengxiaoyan
# @File : util.py

#获取secret用于子系统单点登录
from urllib import parse


def get_secret(url):
    urllist = url.split('code=',1)
    code = urllist[1]
    de_code = parse.unquote(code)
    return de_code

if __name__ == '__main__':
    code = "url=https://value-test.fjmaimaimai.com/#/auth?code=GS4peC7YS%2BgyZR90hp61bCOs7aJPjV4nBkgkP9QRm2jCSbJKe5rskR9gAV20D3uXxCOG8sOajhTYpUMODnSyoHDDpiOIwYcRYaejgOQuIZuYiHElFtZXpwJEN5RcNrk0V%2F4KEW4YWkaEK%2FiQON9ocAZrllgEW%2Bs0l9lutEyRv3g%3D"
    print(get_secret(code))