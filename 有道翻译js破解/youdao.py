import execjs
import requests


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


def translation_result(e):
    data_dic = get_js_function('youdaojs.js', 'youdao', e)
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    cookie = get_cookie()
    cookies = 'OUTFOX_SEARCH_USER_ID=%s; OUTFOX_SEARCH_USER_ID_NCOO=524902467.324696; _ntes_nnid=3cde943d3ec747da98e503d6db0cd1fc,1581636380711; JSESSIONID=%s; ___rl__test__cookies=1584330329437' % (
        cookie['OUTFOX_SEARCH_USER_ID'], cookie['JSESSIONID'])
    headers = {
        'Cookie': cookies,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Host': 'fanyi.youdao.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://fanyi.youdao.com/',
        'Origin': 'http://fanyi.youdao.com'
    }
    data = {
        'i': e,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': data_dic['salt'],
        'sign': data_dic['sign'],
        'ts': data_dic['ts'],
        'bv': data_dic['bv'],
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
    }
    response = requests.post(url=url, data=data, headers=headers)
    fanyi_result = response.json()
    print(fanyi_result)
    print('翻译结果', fanyi_result['translateResult'][0][0]['tgt'])
    print('翻译结果', str(fanyi_result['smartResult']['entries']).strip(' ').strip('\r\n'))


def get_cookie():
    """
    :return:  返回cookie 的jar值
    """
    url_2 = 'http://fanyi.youdao.com/'
    session = requests.Session()
    resp = session.get(url=url_2)
    cookie = dict(session.cookies)
    return cookie


if __name__ == '__main__':
    while True:
        e = input('你想翻译的:')
        translation_result(e)
