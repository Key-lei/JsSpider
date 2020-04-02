# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 11:47
# @Author  : Key-lei
# @File    : 电信.py
import execjs


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



if __name__ == '__main__':
    # url
    # url1 = 'https://login.189.cn/web/login'
    passwd = get_js_function('encript.js', 'aesEncrypt', '密码')
    print(passwd)
