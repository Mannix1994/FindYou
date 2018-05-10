# -*- coding: utf-8 -*-

# 具体解析在这


class Fan(object):
    def __init__(self, person_tag=None):
        self.name = None
        self.sex = None
        self.url = None
        self.id = None
        self.address = None
        self.followNumber = None
        self.fansNumber = None
        self.assay = None
        self.introduce = None
        self.fromInfo = None
        self.analysis(person_tag)

    def analysis(self, person_tag):
        self.analysis_name(person_tag)
        self.analysis_sex(person_tag)
        self.analysis_follow_and_fans_number(person_tag)
        self.analysis_city(person_tag)
        self.analysis_introduce(person_tag)
        self.analysis_follow_way(person_tag)
        self.analysis_id(person_tag)

    def analysis_name(self, person_tag):
        self.name = person_tag.div.a.string

    def analysis_sex(self, person_tag):
        for div_tag in person_tag.find_all('div'):
            if div_tag['class'] == ["info_name", "W_fb", "W_f14"]:
                info_tag = div_tag
        if locals().get("info_tag"):
            for item in info_tag.find_all('a'):
                # print(item)
                if item.i:
                    if item.i['class'] == ["W_icon", "icon_female"]:
                        self.sex = 'female'
                        return
                    elif item.i['class'] == ["W_icon", "icon_male"]:
                        self.sex = 'male'
                        return
                elif item.get('class', None):
                    if item['class'] == ['S_txt1']:
                        self.url = "https://weibo.com" + item['href']
                    pass

    def analysis_id(self, person_tag):
        person_rel = person_tag.dt.a['href']
        self.id = person_rel[person_rel.find('=') + 1:-5] + person_rel[3:person_rel.find('?')]

    def analysis_city(self, person_tag):
        for div_tag in person_tag.find_all('div'):
            if div_tag['class'] == ['info_add']:
                address_tag = div_tag
                self.address = address_tag.span.string

    def analysis_follow_and_fans_number(self, person_tag):
        for div_tag in person_tag.find_all('div'):
            if div_tag['class'] == ["info_connect"]:
                info_tag = div_tag
                self.followNumber = info_tag.find_all('span')[0].em.string
                self.fansNumber = info_tag.find_all('span')[1].em.a.string
                self.assay = info_tag.find_all('span')[2].em.a.string

    def analysis_introduce(self, person_tag):
        for div_tag in person_tag.find_all('div'):
            if div_tag['class'] == ['info_intro']:
                introduce_tag = div_tag
                self.introduce = introduce_tag.span.string

    def analysis_follow_way(self, person_tag):
        for div_tag in person_tag.find_all('div'):
            if div_tag['class'] == ['info_from']:
                from_tag = div_tag
                self.fromInfo = from_tag.a.string

    def __str__(self):
        return "{sex: %s,address: %s,name: %s,id: %s, follow&fan: %s&%s,introduce: %s}" % \
              (self.sex, self.address, self.name, self.id, self.followNumber, self.fansNumber, self.introduce)
