# -*- coding: utf-8 -*-

# 请求头
myHeader = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    , "Accept-Encoding": "gzip, deflate, br"
    , "Accept-Language": "en-US,en;q=0.9"
    , "Connection": "keep-alive"
    , "Cookie":
            "SINAGLOBAL=2459967737867.059.1525967400696; un=13281286897; wvr=6; YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; YF-V5-G0=69afb7c26160eb8b724e8855d7b705c6; YF-Page-G0=b9004652c3bb1711215bacc0d9b6f2b5; _s_tentry=login.sina.com.cn; UOR=,,login.sina.com.cn; Apache=3919331192483.5815.1525970690169; ULV=1525970690234:2:2:2:3919331192483.5815.1525970690169:1525967400723; login_sid_t=869c6aa728878a1570c08f32c4b9b19d; cross_origin_proto=SSL; WBStorage=5548c0baa42e6f3d|undefined; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCn3AwfiBJQKEIXpN.PXZB5JpX5K2hUgL.Foq01K-41hz4e0M2dJLoIpHSwHSaUgphqg4XHsHjd8SXdNiD9Pet; ALF=1557593883; SSOLoginState=1526057884; SCF=Akc_apJiengacfo4mLJKL6QOZF2oE7-iOix_G1kSoya2F3NHxuiBnUWNbc_oImLbIVRp4w7kgpcNCTsS8d49aiA.; SUB=_2A2538bvMDeRhGeBN4lcY-CzFyDuIHXVUhqoErDV8PUNbmtBeLVTDkW9NRASQnAemyKhGdIxNIxQ7OXuCV1URd5WW; SUHB=0pHxyLCZgbrpU6"
    , "Host": "weibo.com"
    , "Referer":
        "https://login.sina.com.cn/crossdomain2.php?action=login&entry=miniblog&r=https%3A%2F%2Fpassport.weibo.com%2Fwbsso%2Flogin%3Fssosavestate%3D1557483043%26url%3Dhttps%253A%252F%252Fweibo.com%252Fp%252F1005052970452952%252Ffollow%253Frelate%253Dfans%2526from%253D100505%2526wvr%253D6%2526mod%253Dheadfans%2526current%253Dfans%26display%3D0%26ticket%3DST-NjM5NTk4MjkzNw%3D%3D-1525947043-tc-8E15BE2BE58851E030308582AFE5E537-1%26retcode%3D0"
    , "Upgrade-Insecure-Requests": "1"
    ,
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36"
}

# 要爬去的账号的粉丝列表页面的地址
fans_url = 'https://weibo.com/p/1005052970452952/follow?relate=fans&from=100505&wvr=6&mod=headfans&current=fans#place'

#
bozhu_id = '1005052970452952'

# 她的信息
my_angel_info = {'name_key_words': ['许', '珊', '许珊', '珊儿', '许珊儿'],
                 'gender': 'female',
                 'address': ['四川 成都', '四川 自贡'],
                 'follow_max': 300,
                 'follow_min': 5,
                 'fans_max': 300,
                 'fans_min': 5,
                 'key_words': ['成都医学院', '成医'],  # 定义搜索关键词,越详细越准确越好
                 }