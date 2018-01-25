#  -*- coding: utf-8 -*-
#  @IDE :  PyCharm
#  @Time : 2017/12/5 11:40
#  @Author ： Daisy
#  @ProjectNmae : test

'''
What about:

'''
import urllib
import urllib.request

import lxml
import lxml.etree
import re
import requests

# headers={
#     "User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
# }
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

url="http://blog.jobbole.com/110287/"
# page=requests.get(url,headers=headers)
# content=page.text

# 伪装浏览器
reps=urllib.request.Request(url=url,headers=headers)
data=urllib.request.urlopen(reps).read().decode("utf-8")
# print(data)
mytree=lxml.etree.HTML(data)
# print(mytree)

# 标题
title=mytree.xpath(".//*[@id='post-110287']/div[1]/h1/text()")
# print(title)

# 日期
create_data=mytree.xpath("//p[@class='entry-meta-hide-on-mobile']/text()")
for create in create_data:
    # print(create.strip().replace("·",""))
    pass

# praise_num=mytree.xpath(("//span[contains(@class, 'vote-post-up')]/h10/text()"))
praise_num=mytree.xpath("//*[@id=\"110287votetotal\"]/text()")
# print(praise_num)

# fav_nums=mytree.xpath("//span[contains(@class, 'bookmark-btn')]/text()")
fav_nums=mytree.xpath("//*[@id=\"post-110287\"]/div[3]/div[9]/span[2]/text()")[0]
# print(fav_nums)
match_re = re.findall(r'(\d+)',fav_nums)
# print(match_re)


comment_nums=mytree.xpath("//*[@id=\"post-110287\"]/div[3]/div[9]/a/span/text()")[0]
# print(comment_nums)
findall_re = re.findall(r'(\d+)',comment_nums)
# print(findall_re)

# contents=mytree.xpath("//div[@class='entry']/text()")[0]
# content = mytree.css("div.entry").extract()[0]

content=mytree.xpath("//*[@id=\"post-110287\"]/div[3]/blockquote/text()")
# content=mytree.xpath("//*[@id=\"post-110287\"]/div[3]/h1[1]/text()")
for con in content:
    print(con.strip())



# tag_list=mytree.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()")
# print(tag_list)