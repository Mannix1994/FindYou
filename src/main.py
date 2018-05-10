# -*- coding: utf-8 -*-

import src.evaluate as analyse
import src.util as util
import src.fans as fans


def analyse_fans(header, the_url, her_info):
    """
    获取博主粉丝列表首页的粉丝,并进行分析判断是不是我想找的人
    :param header: 浏览器头,包含Cookie
    :param the_url: 博主的粉丝列表链接
    :return: 无
    """
    # 获取博主粉丝页的html文件
    html_str = util.get_html(header=header, the_url=the_url)
    # 获取粉丝列表
    fan_list = fans.get_fans_list(html_str)
    print("找到粉丝%s个" % len(fan_list))
    for fan in fan_list:
        # 评估这个人的是我要找的人的可能性
        chance = analyse.evaluate(fan.__dict__, her_info)
        # print(fan.__dict__)
        if chance > 0:
            # 定义搜索关键词,越详细越准确越好
            key_words = ['成都医学院', '成医', '毕业']
            # 获取该粉丝的更多信息
            match_school, count=get_more_info_of_fan(header, fan.url, key_words, '成都医学院')
            print(match_school, count)

    # get_more_info_of_fan(header, 'https://weibo.com/u/3840029822?refer_flag=1005050008_', ['成都医学院', '毕业'])


def get_more_info_of_fan(header, user_url, key_words, school_name):
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
        # 整合结果
        match_school = match_school or result[0]
        match_assay_count += result[1]
    return match_school, match_assay_count


if __name__ == '__main__':
    # 获取的cookie值存放在这
    myHeader = {"Cookie":
                "SINAGLOBAL=2299334805014.0996.1525746172263; un=13281286897; YF-Page-G0=8fee13afa53da91ff99fc89cc7829b07; _s_tentry=login.sina.com.cn; UOR=www.php100.com,widget.weibo.com,login.sina.com.cn; Apache=8137578982260.887.1525847206335; ULV=1525847206359:2:2:2:8137578982260.887.1525847206335:1525746172283; YF-V5-G0=1312426fba7c62175794755e73312c7d; YF-Ugrow-G0=ad83bc19c1269e709f753b172bddb094; login_sid_t=2096f487fd973fb1a02be2350041eef6; cross_origin_proto=SSL; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCn3AwfiBJQKEIXpN.PXZB5JpX5K2hUgL.Foq01K-41hz4e0M2dJLoIpHSwHSaUgphqg4XHsHjd8SXdNiD9Pet; SSOLoginState=1525849379; ALF=1557385399; SCF=Ai-tW_4F5-J1Vz96_4-ZtLh_vlIxnApKRPrQHXsNjlnok_io-cSMIr1B98__xcrD0CZK-D_adFXfJ9cFcwB0_pU.; SUB=_2A2539u1pDeRhGeBN4lcY-CzFyDuIHXVUglmhrDV8PUNbmtBeLRPGkW9NRASQnDF7MQTa_in7THzyZPPKB9MfO9K9; SUHB=0JvgNStksdcg3R; wvr=6"
                }
    # exit(0)
    # 要爬去的账号的粉丝列表页面的地址
    fans_url = 'https://weibo.com/p/1005052970452952/follow?relate=fans&from=100505&wvr=6&mod=headfans&current=fans#place'

    # 她的信息
    her_info = {'name_key_words': ['许', '珊', '许珊', '珊儿', '许珊儿'],
                'sex': 'female',
                'address': ['四川 成都', '四川 自贡'],
                'follow_max': 300,
                'follow_min': 5,
                'fans_max': 300,
                'fans_min': 5,
                }
    analyse_fans(myHeader, fans_url, her_info)
