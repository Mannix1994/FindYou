# -*- coding: utf-8 -*-

# 请求头
myHeader = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    , "Accept-Encoding": "gzip, deflate, br"
    , "Accept-Language": "en-US,en;q=0.9"
    , "Connection": "keep-alive"
    , "Cookie":
        "SINAGLOBAL=2299334805014.0996.1525746172263; un=13281286897; UOR=www.php100.com,widget.weibo.com,login.sina.com.cn; YF-Page-G0=7b9ec0e98d1ec5668c6906382e96b5db; login_sid_t=af32c6d65eca4922920d49bdc64b4690; cross_origin_proto=SSL; YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; YF-V5-G0=24e0459613d3bbdec61239bc81c89e13; WBStorage=5548c0baa42e6f3d|undefined; _s_tentry=passport.weibo.com; wb_view_log=1680*10501; Apache=922084010361.9832.1526002684335; ULV=1526002684344:3:3:3:922084010361.9832.1526002684335:1525847206359; SSOLoginState=1526002696; ALF=1557538698; SCF=Ai-tW_4F5-J1Vz96_4-ZtLh_vlIxnApKRPrQHXsNjlnolce-mPROcZn-QagoRYIJzh8WfA8bD8AMfq7xSTfeKLY.; SUB=_2A2538IRcDeRhGeBN4lcY-CzFyDuIHXVUh_KUrDV8PUNbmtBeLUP5kW9NRASQnIw2GvRtmDej2tlDVQPMGV-CwsyP; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCn3AwfiBJQKEIXpN.PXZB5JpX5KzhUgL.Foq01K-41hz4e0M2dJLoIpHSwHSaUgphqg4XHsHjd8SXdNiD9Pet; SUHB=0idrtUaWx0zene"
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
                 'sex': 'female',
                 'address': ['四川 成都', '四川 自贡'],
                 'follow_max': 300,
                 'follow_min': 5,
                 'fans_max': 300,
                 'fans_min': 5,
                 'key_words': ['成都医学院', '成医', '毕业'],  # 定义搜索关键词,越详细越准确越好
                 }