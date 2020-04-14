import requests
import re
import execjs
import json
"""

"""


def get_js_function(js_path, func_name, func_args1, func_args2, func_args3,func_args4,func_args5):
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
        return ctx.call(func_name, func_args1, func_args2, func_args3,func_args4,func_args5)


if __name__ == '__main__':
    # 第一步 请求扽到变换的加密的eval的url网址
    url = 'https://www.aqistudy.cn/html/city_realtime.php?v=2.3'
    resp = requests.get(url)
    script_url = re.findall('<script type="text/javascript" src="(.*?)"></script>', resp.text, re.S)
    print(script_url[1])
    urljoin = script_url[1].replace('../js', 'https://www.aqistudy.cn/js')
    print(urljoin)
    #########################

    ########################
    # 得到拼接好的网址 然后发送请求 请求eval的js文件 并且写入js文件
    response = requests.get(urljoin)
    test = response.text
    print(test)
    test_done = re.sub('eval\(', 'eval(a=', test)
    print(test_done)
    #### 这一步写入操作
    dd = """
    function te (){
     % s
    return a

    }
    """ % test_done
    # #
    with open('test1.js', encoding='gbk', mode='w') as f:
        f.write(dd)
    # 先请求test1.js文件进行eval解密  然后得到各个参数
    c = get_js_function('test1.js', 'te', '', '', '', '', '')
    print(c)
    #####################################
    # 对eval后的响应进行正则表达提取我们要的参数 就是const定义的那几个
    ac_list = re.findall('ac.*?="(.*?)"', c)
    print('ac_list', ac_list)
    if len(ac_list) > 2:
        del ac_list[0]
    dc_list = re.findall('dc.*?="(.*?)"', c)
    print('dc_list', dc_list)
    if len(dc_list) > 2:
        del dc_list[0]
    as_list = re.findall('as.*?="(.*?)"', c)
    print('as_list', as_list)
    if len(as_list) > 2:
        del as_list[0]
    ds_list = re.findall('ds.*?="(.*?)"', c)
    print('ds_list', ds_list)
    if len(ds_list) > 2:
        del ds_list[0]
    aes_list_key = re.findall("aes_local_key='(.*?)'", c)
    aes_list_iv = re.findall("aes_local_iv='(.*?)'", c)
    print('aes_list_key', aes_list_key)
    print('aes_list_iv', aes_list_iv)
    appId = re.findall("{var appId='(.*?)';", c)
    print('appId', appId)
    params = re.findall("data:{(.*?):param}", c)
    print('params', params)
    #################################
    # 为了构成一个列表传入进js
    as_list.append(ac_list[0])
    as_list.append(ac_list[1])
    as_list.append(ds_list[0])
    as_list.append(ds_list[1])
    as_list.append(dc_list[0])
    as_list.append(dc_list[1])
    as_list.append(aes_list_key[0])
    as_list.append(aes_list_iv[0])
    ###########################
    ###########################
    print(as_list)
    # 传入参数 利用js生成form表单的参数
    parm1 = get_js_function('zqEvalNew.js', 'aqistudyencryptAES', appId[0] , '{"city":"北京"}', as_list,'','')
    parm2 = get_js_function('zqEvalNew.js', 'aqistudyencryptDES', appId[0], '{"city":"北京"}', as_list,'','')
    parm3 = get_js_function('zqEvalNew.js', 'aqistudyencryptBASE', appId[0], '{"city":"北京"}', as_list,'','')
    print(parm1)
    print(parm2)
    print(parm3)
    ####################################
    ####################################
    # 请求得到响应
    headers = {
        'Host': 'www.aqistudy.cn',
        'Cookie': 'UM_distinctid=16dc368ef0faa7-0d2de38f8dbeff-67e1b3f-144000-16dc368ef10b64; CNZZDATA1254317176=2143406767-1570941482-%7C1570984834',
        # 'Cookie': 'UM_distinctid=16dc368ef0faa7-0d2de38f8dbeff-67e1b3f-144000-16dc368ef10b64; CNZZDATA1254317176=2143406767-1570941482-%7C1570984834',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    url_real = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
    data1 = {
        params[0]: parm1,
    }
    data2 = {
        params[0]: parm2,
    }
    data3 = {
        params[0]: parm3,
    }
    print(data1)
    print(data2)
    print(data3)

    result1 = requests.post(url_real, data=data1, headers=headers)
    result2 = requests.post(url_real, data=data2, headers=headers)
    result3 = requests.post(url_real, data=data3, headers=headers)

    print(result1.text)
    print(result2.text)
    print(result3.text)
    #################################
    ## 针对返回的响应进行解密操作
    if len(result1.text) > 300:
        res1 = get_js_function('zqEvalNew.js', 'aqistudydecrypt', result1.text, as_list[0], as_list[1], ds_list[0], ds_list[1])
    else:
        res1 = '改内容不符合'
    if len(result2.text) > 300:
        res2 = get_js_function('zqEvalNew.js', 'aqistudydecrypt', result2.text, as_list[0], as_list[1], ds_list[0], ds_list[1])
    else:
        res2 = '改内容不符合'
    if len(result3.text) > 300:
        res3 = get_js_function('zqEvalNew.js', 'aqistudydecrypt', result3.text, as_list[0], as_list[1], ds_list[0], ds_list[1])
    else:
        res3 = '改内容不符合'
    #####################  返回的内容
    print('*'*50)
    #########################
    # print('result1--------------->', res1)
    # # 如果发现有不显示中文的话 就json.loads一下
    # print('res1',type(res1))
    # print('result2--------------->', res2)
    # print('result3--------------->', res3)
    if res1 != '改内容不符合':
        res1_json = json.loads(res1)
        print('--------------->',res1_json)
        print('-->', res1_json['result'])
    if res2 != '改内容不符合':
        res2_json = json.loads(res2)
        print('--------------->', res2_json)
        print('-->',res2_json['result'])
    if res3 != '改内容不符合':
        res3_json = json.loads(res3)
        print('--------------->',res3_json)
        print('-->', res3_json['result'])


