from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider , RedisMixin

# from example import items
import example.items


class BaikeSpider(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'baikeCrawler_redis'
    redis_key = 'baikeCrawler:start_urls'


    # 根据规则提取链接，follow是否一直循环
    rules = (
        # follow all links
        Rule(LinkExtractor("/item/.*") , callback='parse_item' , follow=True) ,
    )

    # 设置默认爬取链接
    def set_crawler(self , crawler):
        CrawlSpider.set_crawler(self , crawler)
        RedisMixin.setup_redis(self)


    # 提取链接
    def parse_item(self , response):
        # body代表网页数据，url代表当前链接
        pagedata = response.body
        url = response.url
        # 导入items中的类
        baikeItem = example.items.BaikeItem()
        baikeItem["title"] = str(self.getTitle(pagedata))
        baikeItem["content"] = str(self.getContent(pagedata))
        baikeItem["url"] = response.url
        yield baikeItem


    # 获取网页标题
    def getTitle(self , pagedata):
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
    def getContent(self , pageData):
        soup = BeautifulSoup(pageData , "html.parser")  # 解析
        summary = soup.find_all("div" , class_="lemma-summary")
        if len(summary) != 0:
            return summary[0].get_text()
        else:
            return None
