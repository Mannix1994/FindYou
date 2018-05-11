# -*- coding: utf-8 -*-

import time
import random
import traceback
import requests.exceptions as re
import urllib3.exceptions as ue
import src.evaluate as analyse
import src.util as util
import src.fans as fans
import src.DBManager as DBManager
import src.mail as mail
import src.config as config


def analyse_fans(header, the_url, her_info, db):
    """
    获取博主粉丝列表首页的粉丝,并进行分析判断是不是我想找的人
    :param header: 浏览器头,包含Cookie
    :param the_url: 博主的粉丝列表链接
    :param her_info: 她的信息
    :param db: 数据库管理
    :return: 无
    """
    # 获取博主粉丝页的html文件
    html_str = util.get_html(header=header, the_url=the_url)
    # 获取粉丝列表
    fan_list = fans.get_fans_list(html_str)
    # print("找到粉丝%s个" % len(fan_list))
    # 目前只截取一个
    first_fan = [fan_list[0], ]
    print('找到粉丝:%s' % first_fan.__str__())
    for fan in first_fan:
        # 评估这个人的是我要找的人的可能性
        chance = analyse.evaluate(fan.__dict__, her_info)
        # print(fan)
        if chance > 0:
            # 定义搜索关键词,越详细越准确越好
            key_words = her_info['key_words']
            # print(key_words)
            # 获取该粉丝的更多信息
            print('分析粉丝"%s"中...' % fan.name)
            match_school, count = search_more_info_of_fan(header, fan.url, key_words, '成都医学院')
            # print(match_school, count)
            if count == -1 and not match_school:  # 因为搜索太频繁返回,转向搜索用户的所有微博
                print('搜索用户的所有微博中...')
                match_school, count = find_more_info_in_fan_assays(header, fan, key_words, '成都医学院')
            if match_school or count > 0:
                print('找到符合条件的粉丝', fan)
                db.add_a_fan(fan, match_school, count)
                mail.send_email(fan.__str__())
            else:
                print('分析完成,该粉丝不是我要找的')

    # get_more_info_of_fan(header, 'https://weibo.com/u/3840029822?refer_flag=1005050008_', ['成都医学院', '毕业'])


def search_more_info_of_fan(header, user_url, key_words, school_name):
    """
    到粉丝的主页里,找到是不是school_name制定的学校毕业;找到符合key_words指定的
    关键词的微博数量,越多说明越有可能是我要找的人.
    :param header: html头
    :param user_url: 粉丝主页链接
    :param key_words: 关键词组
    :param school_name: 学校名字
    :return: match_school,True为学校匹配,False为学校不匹配或者没有学校信息
    match_assay_count是找到符合关键词组的微博总数量.
    """
    match_assay_count = 0
    match_school = False
    for key_word in key_words:
        # 根据关键词生成搜索的url
        search_url = user_url + '&is_all=1&is_search=1&key_word=' + key_word + '#_0'
        # 获取搜索结果页
        search_result_page = util.get_html(header=header, the_url=search_url)
        # 对结果页进行分析,获取学校是否匹配和符合关键词的微博数量
        result = fans.match_school_and_assay_count(search_result_page, school_name=school_name)
        #
        if result[1] == -1:
            print('微博提示我搜索太频繁了,停止搜索')
            if match_assay_count == 0:
                return match_school, -1
            else:
                return match_school, match_assay_count
        """
        for i in range(0, 4):
            if result[1] != -1:  # 没有提示搜索太频繁
                break
            if i == 3:
                # 都重复第三次了,不搜索了,直接返回-1
                return match_school, -1
            print('微博提示我搜索太频繁了,休眠5s以上的随机再继续搜')
            # 获取一个随机等待时间
            wait_time = random.randint(5, 10)
            # 等一等再继续搜索
            time.sleep(wait_time)
            # 获取搜索结果页
            search_result_page = util.get_html(header=header, the_url=search_url)
            # 对结果页进行分析,获取学校是否匹配和符合关键词的微博数量
            result = fans.match_school_and_assay_count(search_result_page, school_name=school_name)
        """
        # 整合结果
        match_school = match_school or result[0]
        match_assay_count += result[1]
    return match_school, match_assay_count


def find_more_info_in_fan_assays(header, fan, key_words, school_name):
    """
    去粉丝主页,查找学校是否匹配和符合关键词数量的微博数量
    :param header: 头
    :param fan: 粉丝
    :param key_words: 关键词list
    :param school_name: 学校名字
    :return: match_school,True为学校匹配,False为学校不匹配或者没有学校信息
    match_assay_count是找到符合关键词组的微博总数量.
    """
    match_assay_count = 0
    match_school = False

    # 计算微博页数
    page_count = int(fan.assay) // 40 + 1
    for page_index in range(1, page_count + 1):
        assay_url = fan.url + "&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=%d#feedtop" % page_index
        print(assay_url)
        assay_result_page = util.get_html(header, assay_url)
        result = fans.find_school_and_search_key_words_in_assays(assay_result_page, school_name, key_words)
        # 整合结果
        match_school = match_school or result[0]
        match_assay_count += result[1]
    return match_school, match_assay_count
    pass


if __name__ == '__main__':

    # 初始化数据库
    db = DBManager.DBManager(host='localhost', port=3306, user='root',
                             password='lazy1994', db_name='her_info')
    try:
        # 分析粉丝
        i = 1
        while True:
            try:
                print('第%d次尝试' % i)
                for index in range(1, 2):
                    # 生成url
                    fans_list_url = "https://weibo.com/p/%s/follow?relate=fans&page=%d#Pl_Official_HisRelation__59" % \
                                    (config.bozhu_id, index)
                    # print(fans_list_url)
                    analyse_fans(config.myHeader, fans_list_url, config.my_angel_info, db)
                    time.sleep(random.randint(1, 5))
                time.sleep(random.randint(10, 15))
                i += 1
            # 如果是网络异常,停止执行
            except re.ConnectionError:
                traceback.print_exc()
                break
            # 如果是其他异常,继续执行
            except Exception:
                traceback.print_exc()
    except KeyboardInterrupt as e:
        print('用户选择退出...')
    finally:
        print('关闭数据库连接中...')
        db.close()
