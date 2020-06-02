# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 11:04
# @Author  : Key-lei
# @File    : 全国公共资源平台.py
import requests
from parsel import Selector
import json
from urllib import parse
url = 'Z5QkM+mN91uprunwKAwLRA.jhtml'
first_decode = parse.quote(url)
print(first_decode)

# url = 'http://www.bjmtg.gov.cn:80/ggzy/jyxxzccg/2445.jhtml'
# real_url = requests.post('http://localhost:8000/post', data={'href': url}).json()
# real_url_done = str(real_url).replace(r'^','')
    # print(real_url)

# url = 'http://www.bjmtg.gov.cn/ggzy/jyxxzc/index.jhtml'
# response = requests.get(url)
# selector = Selector(response.text)
# tltle_list = selector.css('ul.article-list li')


def get_html(title_url):
    result = requests.get(title_url)
    se = Selector(result.text)
    title = se.css('div.content-title p::text').get()
    content =se.css('div.content-title ul span::text').getall()
    view_num = se.css('#views::text').get()
    print(title)
    print(content)
    print(view_num)


# get_html('http://www.bjmtg.gov.cn:80/ggzy/jyxxzccg/YqWJgF1CkdMMwx5PvNZGpQ.jhtml')
# for dd in tltle_list:
#     title = dd.css('a::text').get()
#     title_url = dd.css('a::attr(href)').get()
#     print(title, title_url)
#     real_url = requests.post('http://localhost:8000/post', data={'href': title_url}).json()
#     if r'^' in str(real_url):
#         print('real_url------------->', str(real_url).replace(r'^', '%5e'))
#     else:
#         print('real_url------------->', real_url)



