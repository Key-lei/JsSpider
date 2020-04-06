# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 17:57
# @Author  : Key-lei
# @File    : music163.py
import execjs
import requests
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

def get_js_function(js_path, func_name, func_args1, func_args2):
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
        return ctx.call(func_name, func_args1, func_args2)


def get_content(jsonDate, rid):
    data = {
        'params': jsonDate.get('encText'),
        'encSecKey': jsonDate.get('encSecKey')

    }

    url = 'https://music.163.com/weapi/v1/resource/comments/A_PL_0_%s?csrf_token=' % rid
    # print(url)
    response = requests.post(url=url, data=data)
    print(response.json())


if __name__ == '__main__':
    # rid 歌曲得id
    # offset 每一页递加20
    rid = '3209089379'
    offset = '20'
    jsonDate = get_js_function('music163.js', 'musicEncrpty', rid, offset)
    get_content(jsonDate, rid=rid)
