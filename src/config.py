# -*- coding: utf-8 -*-

# 请求头，util.get_html(header, the_url)()的第一个参数
myHeader = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    , "Accept-Encoding": "gzip, deflate, br"
    , "Accept-Language": "en-US,en;q=0.9"
    , "Connection": "keep-alive"
    , "Cookie":
        "your cookie"
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
my_angel_info = {'name_key_words': ['徐', '娇', '徐娇', '娇娇'],  # 假如名字交徐娇，则组合出一些关键词
                 'gender': 'female',  # 性别，男是'male'，女是'female'
                 'address': ['四川 成都', '四川 自贡'],  # 分别是家乡地址和学校地址
                 'follow_max': 300,     # 最大关注数量
                 'follow_min': 5,       # 最小关注数量
                 'fans_max': 300,       # 最大粉丝数量
                 'fans_min': 5,         # 最小粉丝数量
                 'key_words': ['北京大学', '北大'],  # 定义搜索关键词,越详细越准确越好
                 }

# 数据库配置
my_db_config = {'host': '你的数据库服务器ip',
                'port': 3306,
                'user': '用户',
                'password': '密码',
                'db_name': '数据库名',
                }

# 邮箱配置
my_email_config = {'host': 'smtp.163.com',              # 设置服务器，可换成其他服务器
                   'sender': 'you_email@163.com',       # 发件人
                   'password': 'auth_path',             # 163邮箱的客户端授权密码，不是邮箱密码，怎么设置可自行百度
                   'receiver': 'receiver@qq.com',       # 收件人
                   }
