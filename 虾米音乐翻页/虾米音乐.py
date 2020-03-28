# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 18:32
# @Author  : Key-lei
# @File    : 虾米音乐.py
import hashlib
import re
import requests
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

# 发出请求 得到数据
def get_html(a, b, headers):
    # url 为你采集的网址 不要带后面的查询参数
    url = 'https://www.xiami.com/api/list/collect'
    params = {
        '_q': a,
        "_s": b,
    }
    response = requests.get(url, params=params, headers=headers)
    print(response.json())


# 获得MD5加密 并且发出请求
def encrypt_page(page):
    # cookie 在这里加
    cookie = 'xmgid=454a3c99-4c2e-4a9e-8ac0-6f69f5f8123b; _uab_collina=157073247284927025486246; cna=euTeFX+q8RQCAXAvcDfgwV2F; gid=157075810645268; _unsign_token=3781baa673c05c6d3e66c49955efe78f; xm_sg_tk=ff456dd4e44b5f9c2dabfdaa1cf6ef26_1585392712572; xm_sg_tk.sig=VA8pepAUOyIr4ExyPedH4eTHVK_cwD0KyQ6A1OzIVeo; xm_traceid=0b51055915853927434487560e0325; xm_oauth_state=69bc37bb58290726188b073ac420b745; _xm_umtoken=T7DF82C8979E810DF0F688F0E1FF3CF085314ED8C3245F3BCFACA9B5053; _xm_cf_=cAwgwv5QOrcfKw59T0OOVR5L; l=dBTxXbkHq2qSysPhBOfiSJv_LxbtwQObzsPr-1AGCICP911eE-8VWZ43368wCnGVn67kR3Wm0ejuBjYGZyC4JNN0bd6FWFpxedTh.; isg=BF1da28034MmXbhP9mgSiW8UbDlXepHMdR8pNB8hrLQg1n8I58ndnEoAAMpQFqmE'

    headers = {
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    # 分析得出的MD5加密
    a = '{"pagingVO":{"page":%s},"pageSize":60},"dataType":"system"}' % page
    b = re.findall('; xm_sg_tk=(.*?); ', cookie)
    b_str = b[0].split('_')[0]
    page_api = b_str + '_xmMain_/api/list/collect_' + a
    page_2_bytes = page_api.encode()
    # 实例化MD5
    m = hashlib.md5()
    # 转换成b字节
    m.update(page_2_bytes)
    encode_md5 = m.hexdigest()
    print(encode_md5)
    get_html(a, encode_md5,headers)


if __name__ == '__main__':
    encrypt_page(1)
