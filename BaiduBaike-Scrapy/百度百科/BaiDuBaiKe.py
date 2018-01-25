#  -*- coding: utf-8 -*-
#  @IDE :  PyCharm
#  @Time : 2017/11/2 0:13
#  @Author ： Daisy
#  @ProjectNmae : BaiDuBaiKe

'''
What about:BS抓取百度百科信息


'''

import requests
import re
# import urlparse
from bs4 import BeautifulSoup


# 获取网页数据
def getData(url):
    # 伪装浏览器
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  # 模拟浏览器
    headers = {'User-Agent': user_agent}
    response = requests.get(url , headers=headers)

    if response.status_code == 200:
        response.encoding = "utf-8"  # 设置编码
        return response.text
    else:
        return None


# 获取网页标题
def getTitle(pagedata):
    soup = BeautifulSoup(pagedata , "html.parser")  # 解析
    list1 = soup.find_all("h1")
    list2 = soup.find_all("h2")
    if len(list1) != 0 and len(list2) != 0:
        return (list1[0].text , list2[0].text)
    elif len(list1) != 0 and len(list2) == 0:
        return list1[0].text
    else:
        return None


# 获取网页
def getContent(pageData):
    soup = BeautifulSoup(pageData , "html.parser")  # 解析
    summary = soup.find_all("div" , class_="lemma-summary")
    if len(summary) != 0:
        return summary[0].get_text()
    else:
        return None


# 获取网页url列表
def getUrlList(pageData):
    urllist = set()  # 集合，去掉皮重复的url
    soup = BeautifulSoup(pageData , "html.parser")  # 解析
    links = soup.find_all("a" , href=re.compile(r"/item/.*"))
    for link in links:
        url = "https://baike.baidu.com"
        url += link["href"]
        urllist.add(url)  # 加入集合

    return urllist


if __name__ == '__main__':
    pageData=getData("https://baike.baidu.com/item/%E5%B0%86%E5%86%9B%E5%9C%A8%E4%B8%8A/19724170?fr=aladdin")
    # pageData = getData("https://baike.baidu.com/item/Python/407313")
    soup = BeautifulSoup(pageData , "html.parser")
    print(getTitle(pageData)[0] , getTitle(pageData)[1] , getContent(pageData) , getUrlList(pageData))
