
# -*- coding: utf-8 -*-
import scrapy

# 提取超链接
from bs4 import BeautifulSoup
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
# 提取链接的规则
from scrapy.spiders import Rule

from 百度百科Scrapy.BaiduBaike.BaiduBaike import items
from 百度百科Scrapy.BaiduBaike import BaiduBaike

class BaikespiderSpider(CrawlSpider):
    name = 'BaikeSpider'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/Python/407313']
    # start_urls=['https://baike.baidu.com/item/%E5%B0%86%E5%86%9B%E5%9C%A8%E4%B8%8A/19724170?fr=aladdin']

    # 网页超链接
    pageLikns = LinkExtractor(allow=("/item/.*"))
    # 根据规则提取的链接，用一个函数处理，follow是否一直循环下去
    # 返回的是urllist
    rules = [Rule(pageLikns , callback="parse_item" , follow=True)]


    # 获取网页标题
    def getTitle(self,pagedata):
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
    def getContent(self,pageData):
        soup = BeautifulSoup(pageData , "html.parser")  # 解析
        summary = soup.find_all("div" , class_="lemma-summary")
        if len(summary) != 0:
            return summary[0].get_text()
        else:
            return None

    # 提取链接
    def parse_item(self , response):
        # body代表网页数据，url代表当前链接
        pagedata = response.body
        url = response.url

        # 导入items中的类BaidubaikeItem
        baikeItem = BaiduBaike.items.BaidubaikeItem()
        baikeItem["title"] = str(self.getTitle(pagedata))
        baikeItem["content"] = str(self.getContent(pagedata))
        baikeItem["url"]=response.url
        yield baikeItem