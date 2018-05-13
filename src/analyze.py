# -*- coding: utf-8 -*-

# 一个粉丝的html源码,对应着fan_dl，这里的源码和后面的解析是对应起来的
"""
 <dl class="clearfix">
  <dt class="mod_pic">
   <a href="/u/6360029229?refer_flag=1005050008_" target="_blank" title="等的我都下雪了">
    <img alt="等的我都下雪了" height="50" src="...jpg" usercard="id=6360029229&amp;refer_flag=1005050008_" width="50"/>
   </a>
  </dt>
  <dd class="mod_info S_line1">
   <div class="info_name W_fb W_f14">
    <a class="S_txt1" href="/u/6360029229?refer_flag=1005050008_" target="_blank" usercard="id=6360029229&amp; ...">
     等的我都下雪了
    </a>
    <a>
     <i class="W_icon icon_female">
     </i>
    </a>
   </div>
   <div class="info_connect">
    <span class="conn_type">
     关注
     <em class="count">
      <a href="/6360029229/follow" target="_blank">
       16
      </a>
     </em>
    </span>
    <span class="conn_type W_vline S_line1">
     粉丝
     <em class="count">
      <a href="/6360029229/fans?current=fans" target="_blank">
       4
      </a>
     </em>
    </span>
    <span class="conn_type W_vline S_line1">
     微博
     <em class="count">
      <a href="/u/6360029229" target="_blank">
       2
      </a>
     </em>
    </span>
   </div>
   <div class="PCD_user_b S_bg1" node-type="follow_recommend_box" style="display:none">
   </div>
   <div class="info_add">
    <em class="tit S_txt2">
     地址
    </em>
    <span>
     北京
    </span>
   </div>
   <div class="info_from">
    通过
    <a class="from" href="http://app.weibo.com/t/feed/4JpANe">
     微博搜索
    </a>
    关注
   </div>
  </dd>
  <dd class="...">其他不解析的数据，我在这里删除了</dd>
 </dl>
"""


class Fan(object):
    def __init__(self, fan_dl=None):
        """
        解析一个粉丝的信息
        :param fan_dl: 包含一个粉丝信息的<dl>标签的网页源码
        """
        self.name = None
        self.gender = None
        self.url = None
        self.id = None
        self.address = None
        self.followNumber = None
        self.fansNumber = None
        self.assay = None
        self.introduce = None
        self.fromInfo = None
        self.analysis(fan_dl)

    def analysis(self, fan_dl):
        self.analysis_name(fan_dl)
        self.analysis_gender(fan_dl)
        self.analysis_follow_and_fans_number(fan_dl)
        self.analysis_city(fan_dl)
        self.analysis_introduce(fan_dl)
        # self.analysis_follow_way(fan_dl)
        self.analysis_id(fan_dl)

    def analysis_name(self, fan_dl):
        # 获取fan_dl第一个<div>的第一个<a>里面的字符串，也就是粉丝的id
        self.name = fan_dl.div.a.string

    def analysis_gender(self, fan_dl):
        info_tag = None
        # 找到所有的<div ...>
        for div_tag in fan_dl.find_all('div'):
            # 如果<div>的class属性为'info_name W_fb W_f14'，就是
            # 性别信息所在<div>(<div class="info_name W_fb W_f14">)
            if div_tag['class'] == ["info_name", "W_fb", "W_f14"]:
                info_tag = div_tag
        if info_tag:
            # 在info_tag中找到所有的<a ...>...</a>
            for tag_a in info_tag.find_all('a'):
                # 如果标签a包含<i ...>...<./i>这个标签，就是包含性别信息的标签a。
                if tag_a.i:
                    # 如果<i ...>的class属性等于'W_icon icon_female'，就是女性
                    if tag_a.i['class'] == ["W_icon", "icon_female"]:
                        self.gender = 'female'
                        return
                    # 如果<i ...>的class属性等于'W_icon icon_male'，就是男性
                    elif tag_a.i['class'] == ["W_icon", "icon_male"]:
                        self.gender = 'male'
                        return
                elif tag_a.get('class', None):
                    # 如果标签<a>的class属性为'S_txt1'，就是包含了粉丝url信息的标签
                    if tag_a['class'] == ['S_txt1']:
                        # 获取href属性，得到粉丝的主页地址
                        self.url = "https://weibo.com" + tag_a['href']
                    pass

    def analysis_id(self, fan_dl):
        # 获取粉丝的id
        # 第一个<dt>的第一个<a>的href属性
        person_rel = fan_dl.dt.a['href']
        self.id = person_rel[person_rel.find('=') + 1:-5] + person_rel[3:person_rel.find('?')]

    def analysis_city(self, fan_dl):
        # 后面的我就不写注释了，和前面的同理
        for div_tag in fan_dl.find_all('div'):
            if div_tag['class'] == ['info_add']:
                address_tag = div_tag
                self.address = address_tag.span.string

    def analysis_follow_and_fans_number(self, fan_dl):
        for div_tag in fan_dl.find_all('div'):
            if div_tag['class'] == ["info_connect"]:
                info_tag = div_tag
                self.followNumber = info_tag.find_all('span')[0].em.string
                self.fansNumber = info_tag.find_all('span')[1].em.a.string
                self.assay = info_tag.find_all('span')[2].em.a.string

    def analysis_introduce(self, fan_dl):
        for div_tag in fan_dl.find_all('div'):
            if div_tag['class'] == ['info_intro']:
                introduce_tag = div_tag
                self.introduce = introduce_tag.span.string

    def analysis_follow_way(self, fan_dl):
        for div_tag in fan_dl.find_all('div'):
            if div_tag['class'] == ['info_from']:
                from_tag = div_tag
                self.fromInfo = from_tag.a.string

    def __str__(self):
        return "{name: %s, gender: %s,address: %s,id: %s, follow&fan: %s&%s,introduce: %s, url: %s}" % \
              (self.name, self.gender, self.address, self.id, self.followNumber,
               self.fansNumber, self.introduce, self.url)
