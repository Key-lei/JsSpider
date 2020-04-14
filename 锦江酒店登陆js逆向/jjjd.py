# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 19:45
# @Author  : Key-lei
# @File    : jjjd.py
import execjs
import requests
import json


def get_js_function(js_path, func_name, func_args1):
    '''
    获取指定目录下的js代码, 并且指定js代码中函数的名字以及函数的参数。
    :param js_path: js代码的位置
    :param func_name: js代码中函数的名字
    :param func_args: js代码中函数的参数
    :return: 返回调用js函数的结果
    '''

    with open(js_path, encoding='GBK') as fp:
        js = fp.read()
        ctx = execjs.compile(js)
        return ctx.call(func_name, func_args1)


def get_html(data_dict):
    login_url = 'https://hotel.bestwehotel.com/api/member/login'
    data = {"groupTypeId": 2,
            "type": 1,
            "mobile": "你的账号",
            "password": data_dict['password'],
            "rememberMe": 'false',
            "verifyCode": "",
            "black_box": data_dict['black_box'],
            }

    response = requests.post(url=login_url, json=data)
    print(response.json())
    print(response.text)


if __name__ == '__main__':
    password = get_js_function('jjjdpassword.js', 'encrapyAES', '你的密码')
    black_box = get_js_function('jjjd.js', 'get_box', '')
    data_dict = {'password': password, 'black_box': black_box, }
    get_html(data_dict)

