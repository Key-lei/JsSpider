# -*- coding: utf-8 -*-#
# FileName:         hongshuwang
# Description:  
# Author:       Thor
# Date:         2020/5/25 22:45

import requests
from parsel import Selector
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
#
# url = 'https://g.hongshu.com/content/93416/13877912.html'
#
# response = requests.get(url)
# selector = Selector(response.text)
#
# content = selector.css('div.rdtext')
# for i in content:
#     content_slice =

url = 'https://wall.alphacoders.com/by_sub_category.php?id=312213&name=%E9%AC%BC%E7%81%AD%E4%B9%8B%E5%88%83+%E5%A3%81%E7%BA%B8&lang=Chinese'

res = requests.get(url)
res.encoding = res.apparent_encoding
select = Selector(res.text)
# 还是css靠谱
# img_list = select.css("#page_container > div:nth-child(8)>div")
img_list = select.xpath("//div[@class='custom-navigation']//following-sibling::div[3]/div")
# 很久没用xpath 有点生疏了
print(img_list)
print(len(img_list))
for i in img_list:
    # src = i.css("div.boxgrid a img::attr(data-src)").get()
    src = i.xpath("./div/div[@class='boxgrid']/a/img/@data-src").get()
    print(src)