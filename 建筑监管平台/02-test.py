# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 13:09
# @Author  : Key-lei
# @File    : 02-test.py
# from Crypto.Cipher import AES
#
# key = bytes('h5LoginKey123456', encoding='utf-8')
# iv = bytes('h5LoginIv1234567', encoding='utf-8')
#
# cipher = AES.new(key, AES.MODE_CBC, iv)
#
# message = "123123123"
# # message = hex(bytes(message, encoding='utf-8'))
# cipher_text = cipher.encrypt(bytes.fromhex(message))
# print(cipher_text)
# cipher_text = cipher.decrypt(bytes.fromhex(message))
# text = cipher_text.decode('utf-8')
# print(cipher_text.decode('utf-8'))
# print(text[:len(text) - 6])
# result = str(cipher_text, encoding='utf-8')
# result = pkcs7(result)
# print(result)
# decrypt_bytes = cipher.decrypt(message)
# print(decrypt_bytes.decode('utf-8'))


import base64
from Crypto.Cipher import AES


# 密钥（key）, 密斯偏移量（iv） CBC模式加密

def AES_Encrypt(key, data):
    vi = '0102030405060708'
    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    data = pad(data)
    # 字符串补位
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    encryptedbytes = cipher.encrypt(data.encode('utf8'))
    # 加密后得到的是bytes类型的数据
    encodestrs = base64.b64encode(encryptedbytes)
    # 使用Base64进行编码,返回byte字符串
    enctext = encodestrs.decode('utf8')
    # 对byte字符串按utf-8进行解码
    return enctext


key = '0CoJUm6Qyw8W8jud'
data = 'sdadsdsdsfd'
# AES_Encrypt(key, data)
enctext = AES_Encrypt(key, data)
print(enctext)
