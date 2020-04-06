# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 11:47
# @Author  : Key-lei
# @File    : 电信.py
import execjs
import requests
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

def get_js_function(js_path, func_name, func_args1):
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
        return ctx.call(func_name, func_args1)


def get_html(cookie):
    url = 'https://www.guazi.com/quanzhou/dazhong/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'cookie': cookie,
    }
    response = requests.get(url, headers=headers, verify=False)
    print(response.text)


if __name__ == '__main__':
    cookie = get_js_function('guazi.js', 'xredirect', '')
    get_html(cookie)
