# 项目说明文档 #

## 一、做这个项目的原因 ##
在一次和朋友聊天的时候，给我推荐了"李子柒"这个微博，有九百多万粉丝，我说"我
能不能在这九百多万粉丝里面找到你呢？""我觉得是不可能的"。何尝不试一试？于是
我就想用Python爬虫来抓取每一个粉丝的信息，根据我已知的姓名、城市、性别、本科学
校名字、本科学校所在城市和家乡等信息作为匹配条件，看看能不能从这九百多万粉丝里
面找出这个朋友的账号（我觉得是不可能的）。

## 二、思路 ##
   首先讨论我的想法，微博一般不会把自己的名字作为微博昵称，城市和性别倒是有可能
是真的，所以我假设朋友的城市和性别分别设置为：学校所在城市或者家乡所在城市、真
实的性别；匹配这两个条件之后的才进如粉丝主页搜索她的学校信息(如果有)和搜索指定
的关键词(学校全称、学校简称等准确信息)，如果搜索到到这两个信息，就极有可能是我
要找的人。为什么要假设朋友的城市和性别是准确的(不是乱设置的)？因为粉丝数量太多
了，必须假设这两个条件满足，不然不知道到筛选到何年何月，但是这样一假设，找到朋
友的概率就变小了。
  程序思路：爬取"李子柒"的粉丝页，获得一个粉丝，如果粉丝的地址和性别满足条件，
就进入粉丝主页，获取学校信息和搜索指定关键词(有助于确定是朋友的关键词)，如果学
校匹配或者指定关键词的微博数量大于0，这个粉丝就极有可能是我要找的人；如果微博
提示搜索太频繁，就抓取粉丝的所有微博，从这些微博中搜索关键词。

## 三、解析"李子柒"的粉丝页 ##
  Python版本为3.5；在我程序中使用到的包：requests、lxml、BeautifulSoup4、json等。
```
pip install requests  # 获取网页
pip install lxml  # 解析引擎，在BeautifulSoup4中被使用
pip install BeautifulSoup4  # 解析HTML文件，从其中提取信息
pip install mysqlclient  #MySQL数据库驱动
```
  1. 获取"李子柒"的粉丝页  
  
  爬取微博数据的时候，很多页面需要登录自己的微博才能看到，那么，有木有简单的办法
不用再代码中实现登录的功能，就能获取自己想要的页面？答案是有的，如下代码就可以：
```python
import requests
from html.parser import HTMLParser

def get_html(header, the_url):
    """
    获取the_url指定的网页
    :param header: 网页的请求头信息,包含Cookie啊什么的，Cookie就是你登录之后
    的凭证，其他的信息也照抄，伪装成浏览器访问微博，减少封号风险。
    :param the_url: 网页网址
    :return: 返回下载到的网页
    """
    r = requests.get(url=the_url, headers=header)
    parser = HTMLParser()
    parser.feed(r.text)
    html_str = r.text
    return html_str
```
其中的header就是网页的请求头(Request Headers)信息。可使用Chrome、Chromium、
Firefox浏览器来获取请求头信息。获取这个请求头部的步骤为：1.登录微博，进入
你要下载的页面； 2、按F12进入开发模式；3. 点击"网络(Network)"选项卡；4. F5
刷新当前页面；5. 在"网络(或Network)"选项卡中点击"HTML(或Doc)"；6. 点击一下
你要下载的页面的网址；7. 点击"消息头(或Headers)"选项卡；8. 在该选项卡中的
"请求头(或Request Headers)"就是header里面需要的信息。header的格式在config
.py中有例子。

  2. 解析"李子柒"的粉丝页  
  * 分析粉丝主页HTML的结构
```html
1  <!doctype html>
2  <html>
3  <head>
4  <!---其他头部信息。。。。-->
5  <title>李子柒的微博_微博</title>
6
7  <!-- $CONFIG -->
8  <script type="text/javascript">
9  var $CONFIG = {};
10 $CONFIG['islogin']='1'; 
11 //配置信息.....
12 </script>
13 <!-- / $CONFIG -->
14 
15 </head>
16 <body class="B_page S_page">
17  <div class="WB_miniblog">
18    <div class="WB_miniblog_fb">
19      <div id="pl_common_top">
29      </div>
21            <div class="WB_main clearfix" id="plc_frame">
22      </div>
23            <div class="WB_footer S_bg2" id="pl_common_footer">
24      </div>
25    </div>
26  </div>
27 <div id="pl_common_base"></div>
28 <div id="pl_common_forword"></div>
29 <div id="pl_common_dynamicskin"></div>
30 <div id="pl_lib"></div>
31 <div id="pl_common_webim"></div>
32 </body>
33
34 <script>
35     var FM='js脚本'
36 </script>
37 <script>FM.view({"domid":"pl_lib",内容...});</script>
38 <script>FM.view({"ns":"pl.common.webim","domid":"pl_common_webim",内容...})</script>
39 <script>FM.view({"ns":"pl.top.index","domid":"pl_common_top",内容...})</script>
40 <script>FM.view({"ns":"page.pl.content.changeLanguage.index","domid":"pl_common_footer","css":[],内容...})</script>
41 <script>FM.view({"ns":"pl.base.index","domid":"pl_common_base",内容...)</script>
42 <script>FM.view({"ns":"page.pl.frame.index","domid":"plc_frame",内容...})</script>
43 <script>FM.view({"ns":"pl.header.head.index","domid":"Pl_Official_Headerv6__1",内容...})</script>
44 <script>FM.view({"ns":"pl.nav.index","domid":"Pl_Official_Nav__2",内容...})</script>
45 <script>FM.view({"ns":"","domid":"plc_main","css":[],"html":"内容...",内容...})</script>
46 <script>FM.view({"ns":"pl.thirdVip.liveSkins.index","domid":"pl_common_dynamicskin",内容...)</script>
47 <script>FM.view({"ns":"pl.content.navList.index","domid":"Pl_Official_HisRelationNav__58",内容...})</script>
48 <script>FM.view({"ns":"pl.content.followTab.index","domid":"Pl_Official_HisRelation__59","html":"内容...",内容...})</script>
49 </html>
```
  观察该HTML源码，可以发现，页面里的内容是通过js脚本载入进去的，从37到48行，每
一行的内容包含了在粉丝页面中显示的内容，在经过浏览器渲染(执行37到48的js脚本)以
后，会加载到16到31行。例如48行，就是包含了"李子柒"粉丝页的粉丝内容，经过浏览
器渲染以后，会加载到页面中指定的位置。那么，我是怎么确定我要找的粉丝内容在48行
的？答案就是打开粉丝页，查看网页源码，然后Ctrl+F查找一个粉丝的信息，比如id，就
能发现这个id出现在第48行，这样，我就知道粉丝的信息在48行的js脚本里了。观察48行
可以看出"domid":"Pl_Official_HisRelation__59"是该行特有的字符串，不管粉丝的信
息怎么变，这段字符串是不变的，因此可以通过find函数来确定是否是粉丝信息所在行。
可以看出，FM.view()是一个函数，参数是一个json数据(类似于python中的Dictionary，
也就是键值对)，包含粉丝信息的网页数据，就在这个json数据里(粉丝信息对应的key是
'html'),所以，在python中，我们可以提取出FM.view()的参数A，然后编写代码
```json_data = json.loads(A)```获得json对象```json_data```,获取```json_data```
里面的网页数据可通过如下代码获取```html_data = json_data['html']```，
```html_data```就是包含粉丝信息的网页。然后就可以使用BeautifulSoup来解析网页从
其中提取你想要的信息。微博的其他网页的结构和这个类似(当然，这里指的是电脑版的
微博，手机版的不知道是否相同)，具体的代码请看项目中函数的注释，都是非常详细的了。
  * 看懂以下两段代码，解析微博的页面就不成问题了  
  解析一页的粉丝
```python
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
                # 解析粉丝
                p = Fan(fan_dl)
                # print(p.__dict__)
                fans.append(p)
            break

    return fans
```
解析一个粉丝，首先给出一个粉丝的html源码，再给出解析这个html源码的代码。
```html
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
```
解析代码  
```python
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
                # 如果标签a包含<i ...>...</i>这个标签，就是包含性别信息的标签a。
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

```

## 三、整个项目的代码流程 ## 
  
  代码思路为：1.获取粉丝→2.判断粉丝的地址和学校是否匹配→{3.1若不匹配，立即
返回第1步，开始处理下一个粉丝；3.2 若匹配成功，则在粉丝的主页中搜索能帮助确定
是我要找的人的关键词和学校信息，进入第4步}→{4.1 如果微博提示搜索太过于频繁，
则进入粉丝主页，获取粉丝所有的微博，然后在微博中搜索满足关键词的微博数量和学
校信息，进入第5步；4.2 进入第5步}→{4.1 若学校匹配或者包含指定的关键词的微博
条数大于0，那么这个人很有可能是我要找的人，于是将这个粉丝放入数据库，并发邮件
通知我查看粉丝的信息，确定是否是要找的人，返回第1步；4.2 若学校不匹配和微博数
量等于0，说明这个人不是我要找的，返回第1步；}→{5.1 若学校匹配或者包含指定的
关键词的微博条数大于0，那么这个人很有可能是我要找的人，于是将这个粉丝放入数据
库，并发邮件通知我查看粉丝的信息，确定是否是要找的人，返回第1步；5.2 若学校不
匹配和微博数量等于0，说明这个人不是我要找的，返回第1步。}  
  入口函数为main.py的main函数，main函数包含了一个while循环，是个死循环，这个
循环的作用就是一直调用analyse_fans()函数来完成获取粉丝和匹配粉丝信息这个过程。

## 四、关于作者 ##

```javascript
  var whoAmI = {
    name   : "Mannix1994",
    gitee  : "https://gitee.com/Mannix1994",
    github : "https://github.com/Mannix1994"
  }
```