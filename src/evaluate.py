# -*- coding: utf-8 -*-
import json
import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup


# 评估这个人是她的可能性有多大
def evaluate(info):
    probability = 0

    # sex
    if info['sex'] == 'female':
        probability += 1
    else:
        return 0

    # address
    address = info['address']
    if address == '四川 成都' or address == '四川 自贡':
        probability += 1
    else:
        return 0

    # follow number and fans number
    if int(info['followNumber']) < 200 and int(info['fansNumber']) < 200:
        probability += 1

    if int(info['followNumber']) > 5 and int(info['fansNumber']) > 5:
        probability += 1

    # name
    name = info['name']
    if name.find('许') or name.find('珊') or name.find('珊儿'):
        probability += 1

    return probability
