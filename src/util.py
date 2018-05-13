# -*- coding: utf-8 -*-
import requests
from html.parser import HTMLParser


def get_html(header, the_url):
    """
    获取the_url指定的网页
    :param header: 网页的请求头信息,包含Cookie啊什么的，Cookie就是你登录之后
    的凭证，其他的信息也照抄，伪装成浏览器访问微博，减少封号风险。
    :param the_url: 网页网址
    :return: 返回下载到的网页
    """
    r = requests.get(url=the_url, headers=header)
    parser = HTMLParser()
    parser.feed(r.text)
    html_str = r.text
    return html_str

