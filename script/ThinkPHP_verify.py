#coding: utf-8

"""
ThinkPHP 简单指纹识别脚本

需要requests库支持

by featherl
"""

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
        target = format_url(url) + '?c=4e5e5d7364f443e28fbf0d3ae744a59a'
        r = requests.get(target, headers={'User-Agent': chrome() })
        r.raise_for_status()

        if r.headers.get('Content-Type') == 'image/png':
            return True
    except:
        pass
    
    return False
    