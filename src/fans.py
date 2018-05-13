# -*- coding: utf-8 -*-
import time
from bs4 import BeautifulSoup
from .analyze import Fan
import json


def get_fans_list(html_str):
    """
    从博主的粉丝页html源码中解析出粉丝
    :param html_str: 含有粉丝的网页，模板在README.md文件中
    :return: 返回粉丝的一个list
    """
    # 分割html网页，得到一些包含json数据的字符串
    fans_json_list = html_str.split("</script>")

    # 找到包含粉丝信息的那个json字符串
    json_str = {}
    for item in fans_json_list:
        # 去除"FM.view"等其他字符，得到一个json格式的字符串
        item = get_pure_json(item)
        # 如果是空，则继续处理下一个数据
        if not item:
            continue
        # "domid":"Pl_Official_HisRelation__59"是一个粉丝信息页的
        # 那一行的一个独特的标识，其他行的都不同，如果一个json字符
        # 串包含这个字符串，那么这个json对象就包含粉丝信息。要获取
        # 其他信息，也可以通过该行的一个独特的标识来定位。
        if item.find('"domid":"Pl_Official_HisRelation__59"') > -1:
            json_str = item

    # 载入json格式字符串，得到一个dictionary
    json_data = json.loads(json_str)
    # print(fans_html)

    # 使用BeautifulSoup解析，json_data['html']是网页数据，'lxml'是
    # 解析html的引擎。关于BeautifulSoup的使用，大家可自行查看文档。
    soup = BeautifulSoup(json_data['html'], 'lxml')

    # 预处理，打印soup.prettify()的结果，就会看到一个格式化好的html文件
    soup.prettify()
    # print(soup.prettify())
    # 写入文件
    # f = open("html/test.html", "w", encoding="UTF-8")
    # f.write(soup.prettify())

    # 获取html文件里的粉丝
    fans = []
    for div_tag in soup.find_all('div'):
        # 找到包含粉丝列表的div，下面是包含粉丝信息的网页数据形式
        # <div class = 'follow_inner'>
        #   <ul><li><dl>第一个粉丝的信息</dl></li></ul>
        #   <ul><li><dl>第二个粉丝的信息</dl></li></ul>
        #   ...
        # </div>
        if div_tag['class'] == ["follow_inner"]:
            # 提取粉丝,<dl>标签里就是粉丝的信息
            for fan_dl in div_tag.find_all('dl'):
                p = Fan(fan_dl)
                # print(p.__dict__)
                fans.append(p)
            break

    return fans


def match_school_and_assay_count(search_result_page='', school_name='成都医学院'):
    """
    从搜索结果页中解析学校是否匹配和指定关键词的微博数量
    :param search_result_page: 指定关键词的搜索结果HTML文件
    :param school_name: 学校名字
    :return: 返回学校是佛匹配和符合关键词的数量
    """
    print('正在匹配学校和搜索关键词...')
    match_school = False  # 学校是否匹配
    assay_count = 0  # 符合关键词的微博的数量

    # 分割json脚本列表
    json_lists = search_result_page.split("</script>")

    for item in json_lists:
        # 去除多余的部分,得到json数据,不懂的把上下两部分打印出来就知道
        item = get_pure_json(item)
        if not item:
            continue

        # 基本信息栏
        if item.find('"domid":"Pl_Core_UserInfo__6"') > -1:
            loaded_html = json.loads(item)
            # 如果从个人信息栏里面找到学校名字,说明学校匹配了
            if loaded_html.get('html'):
                if loaded_html['html'].find(school_name) > -1:
                    match_school = True
        # 搜索微博列表块
        elif item.find('"domid":"Pl_Official_MyProfileFeed__20"') > -1:
            loaded_html = json.loads(item)
            # 如果从搜索到的微博列表中找到"找不到符合条件的微博",则说明该关键词搜索到的微博为0
            if loaded_html['html'].find('找不到符合条件的微博') > -1:
                assay_count = 0
            elif loaded_html['html'].find('你搜的太频繁了'):
                return match_school, -1
            else:  # 否则,可以从其中解析出符合关键词的微博数量
                # 通过美丽汤来解析
                soup = BeautifulSoup(loaded_html['html'], 'lxml')
                # 搜索到的微博数量在一个<em>标签里,因此找到所有的<em>标签
                for em in soup.find_all('em'):
                    # print(em)
                    if em.get('class', None):
                        # 找到class = 'W_fb S_spetxt'的那个标签,里面的数字就是通过该关键词搜索到的微博总数
                        if em['class'] == ['W_fb', 'S_spetxt']:
                            assay_count = int(em.string)
    return match_school, assay_count


def find_school_and_search_key_words_in_assays(assay_page, school_name, key_words):
    """
    在微博主页中获取学校是否匹配;搜索微博中符合关键词的微博数量
    :param assay_page: 粉丝主页
    :param school_name: 学校名字
    :param key_words: 关键词list
    :return: 学校是否匹配和关键词数量
    """
    print('正在匹配学校和在用户的微博中查找关键词...')
    match_school = False  # 学校是否匹配
    assay_count = 0  # 符合关键词的微博的数量

    # 分割json脚本列表
    json_lists = assay_page.split("</script>")

    for item in json_lists:
        # 去除多余的部分,得到json数据,不懂的把上下两部分打印出来就知道
        item = get_pure_json(item)
        if not item:
            continue

        # 基本信息栏
        if item.find('"domid":"Pl_Core_UserInfo__6"') > -1:
            loaded_html = json.loads(item)
            # 如果从个人信息栏里面找到学校名字,说明学校匹配了
            if loaded_html.get('html'):
                if loaded_html['html'].find(school_name) > -1:
                    match_school = True
        # 微博列表页
        elif item.find('"domid":"Pl_Official_MyProfileFeed__20') > -1:
            loaded_html = json.loads(item)
            html_str = loaded_html['html']
            for key_word in key_words:
                # 这里使用一个巧妙的方式来搜索指定关键词出现的数量
                # 以关键词分割字符串,得出的list长度再减一,就得到关键词出现的次数
                assay_count += len(html_str.split(key_word))-1

    return match_school, assay_count


def get_pure_json(json_draft):
    """
    去除多余的部分,得到json数据
    微博的网页一般是分块的,然后每一块都是用js来处理json数据来得到最后的HTML文本,
    因此这个函数的作用就是从分割后的网页部分字符串处理,得到json数据
    :param json_draft: 含有其他成分的json字符串
    :return: 处理完的字符串
    """
    tag = '<script>FM.view'
    index = json_draft.find(tag)
    if index > -1:
        item = json_draft[index + len(tag) + 1:len(json_draft) - 1]
        if item[-1] == ')':
            item = item[:len(item) - 1]
        return item
    else:
        return None


def save_html(file_name, html_str):
    """
    保存HTML文件
    :param file_name: 文件名
    :param html_str: 网页字符串
    :return: 不返回
    """
    soup = BeautifulSoup(html_str, 'lxml')
    f = open(file_name, "w", encoding="UTF-8")
    f.write(soup.prettify())
    f.close()


def get_all_json_and_save_html(html_str):
    """
    分割一个网页,保存其中每个人json数据代表的网页
    :param html_str: 粉丝的主页啊,粉丝页等
    :return: 空
    """
    # 分割json脚本列表
    json_lists = html_str.split("</script>")
    i = 0
    for item in json_lists:
        item = get_pure_json(item)
        if not item:
            continue

        html_content = json.loads(item)

        try:
            soup = BeautifulSoup(html_content['html'], 'lxml')
            soup.prettify()
        except KeyError:
            pass
        else:
            f = open("html/%s_%s.html" % (i, len(item)), "w", encoding="UTF-8")
            f.write(soup.prettify())
        pass
        i += 1
    pass
