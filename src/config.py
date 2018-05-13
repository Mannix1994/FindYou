# -*- coding: utf-8 -*-

# 请求头
myHeader = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    , "Accept-Encoding": "gzip, deflate, br"
    , "Accept-Language": "en-US,en;q=0.9"
    , "Connection": "keep-alive"
    , "Cookie":
        "YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; login_sid_t=ebbac7aa2632d8b9af2c73b48a46e341; cross_origin_proto=SSL; YF-V5-G0=572595c78566a84019ac3c65c1e95574; WBStorage=5548c0baa42e6f3d|undefined; _s_tentry=passport.weibo.com; wb_view_log=1680*10501; Apache=7413002826311.49.1526176052742; SINAGLOBAL=7413002826311.49.1526176052742; ULV=1526176052751:1:1:1:7413002826311.49.1526176052742:; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCn3AwfiBJQKEIXpN.PXZB5JpX5K2hUgL.Foq01K-41hz4e0M2dJLoIpHSwHSaUgphqg4XHsHjd8SXdNiD9Pet; ALF=1557712085; SSOLoginState=1526176086; SCF=ApTvMbD348JpEGqD2arduFaKNx5llw4f6OGa6CDgOw2Wf0qAlZzLGHVAEP9j1c_w5syi98Ln5T3rzKaAZYC5HA4.; SUB=_2A2538-kHDeRhGeBN4lcY-CzFyDuIHXVUiV3PrDV8PUNbmtBeLRTikW9NRASQnD9LgZV2Xv0GNC78BT3Rsr3H67Az; SUHB=0ebt5D0j1JLAhj; un=13281286897; wvr=6; YF-Page-G0=27b9c6f0942dad1bd65a7d61efdfa013"

    , "Host": "weibo.com"
    , "Referer":
        "https://weibo.com/6395982937/follow?rightmod=1&wvr=6"

    , "Upgrade-Insecure-Requests": "1"
    ,
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36"
}

# 要爬去的账号的粉丝列表页面的地址
fans_url = 'https://weibo.com/p/1005052970452952/follow?relate=fans&from=100505&wvr=6&mod=headfans&current=fans#place'

# "李子柒"的id，可从粉丝业的网址里面找到
bozhu_id = '1005052970452952'

# 我朋友的信息
my_angel_info = {'name_key_words': ['许', '珊', '许珊', '珊儿', '许珊儿'],
                 'gender': 'female',
                 'address': ['四川 成都', '四川 自贡'],
                 'follow_max': 300,
                 'follow_min': 5,
                 'fans_max': 300,
                 'fans_min': 5,
                 'key_words': ['成都医学院', '成医'],  # 定义搜索关键词,越详细越准确越好
                 }

# 数据库配置
my_db_config = {'host': '118.126.117.238',
                'port': 3306,
                'user': 'root',
                'password': 'lazy1994',
                'db_name': 'her_info',}
