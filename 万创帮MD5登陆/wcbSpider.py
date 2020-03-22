# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 15:09
# @Author  : Key-lei
# @File    : wcbSpider.py
import execjs
import requests
import json


def get_js_function(js_path, func_name, func_args):
    '''
    获取指定目录下的js代码, 并且指定js代码中函数的名字以及函数的参数。
    :param js_path: js代码的位置
    :param func_name: js代码中函数的名字
    :param func_args: js代码中函数的参数
    :return: 返回调用js函数的结果
    '''

    with open(js_path, encoding='utf-8') as fp:
        js = fp.read()
        ctx = execjs.compile(js)
        return ctx.call(func_name, func_args)


def login(username, password):
    url = 'https://www.wcbchina.com/api/login/login'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    }
    data = {'username': username, 'password': password}
    # print(data)
    login_response = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(login_response.json())


if __name__ == '__main__':
    # 登陆密码
    username = '13636908252'
    passwd = get_js_function('wcb.js', 'MD5', '666666')
    login(username, passwd)
