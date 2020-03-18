# @Time    : 2020/3/18 16:31
# @Author  : Key-lei
# @File    : 懒人听书.py

import execjs
import requests


def get_js_function(js_path, func_name, func_args1, func_args2):
    '''
    获取指定目录下的js代码, 并且指定js代码中函数的名字以及函数的参数。
    :param js_path: js代码的位置
    :param func_name: js代码中函数的名字
    :param func_args: js代码中函数的参数
    :return: 返回调用js函数的结果
    '''

    with open(js_path, encoding='gbk') as fp:
        js = fp.read()
        ctx = execjs.compile(js)
        return ctx.call(func_name, func_args1, func_args2)


def lanre_rq(password):
    url = 'http://www.lrts.me/user/login.do'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '123',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.lrts.me',
        'Origin': 'http://www.lrts.me',
        'Referer': 'http://www.lrts.me/login',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'accountName': '你的账号',
        'hashPass': password,
        'autoLogin': '1',
        'validateCode': '',
    }
    resp = requests.post(url, data=data, headers=headers)
    return resp.json()


if __name__ == '__main__':
    data = {
        'accountName': '你的账号'
    }
    url1 = 'http://www.lrts.me/user/login_token.do'
    res_token = requests.post(url1, data=data).json()
    token = res_token.get('data')
    print(token)
    passwd = get_js_function('懒人听书.js', 'lanren','你的密码', token)
    res = lanre_rq(password=passwd)
    print(res)
