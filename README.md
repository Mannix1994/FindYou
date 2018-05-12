# 项目说明文档 #

## 一、做这个项目的原因 ##
在一次和朋友聊天的时候，给我推荐了“李子柒”这个微博，有九百多万粉丝，我说“我
能不能在这九百多万粉丝里面找到你呢？”“我觉得是不可能的”。何尝不试一试？于是
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
  程序思路：爬取“李子柒”的粉丝页，获得一个粉丝，如果粉丝的地址和性别满足条件，
就进入粉丝主页，获取学校信息和搜索指定关键词(有助于确定是朋友的关键词)，如果学
校匹配或者指定关键词的微博数量大于0，这个粉丝就极有可能是我要找的人；如果微博
提示搜索太频繁，就抓取粉丝的所有微博，从这些微博中搜索关键词。

## 三、程序 ##
  Python版本为3.5；在我程序中使用到的包：requests、lxml、BeautifulSoup4、json等。
```
pip install requests  # 获取网页
pip install lxml  # 解析引擎，在BeautifulSoup4中被使用
pip install BeautifulSoup4  # 解析HTML文件，从其中提取信息
```
  1. 爬取“李子柒”的粉丝页
  * 分析粉丝主页HTML的结构
```html
1  <!doctype html>
2  <html>
3  <head>
4  其他头部信息。。。。
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
35     var FM=js脚本
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
  观察该HTML源码
  