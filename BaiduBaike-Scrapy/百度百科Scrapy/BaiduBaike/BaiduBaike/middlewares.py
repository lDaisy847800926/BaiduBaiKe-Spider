
# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy import signals
import random
import base64 #编码
from .settings import USER_AGENTS #导入浏览器模拟，导入代理
from .settings import PROXIES

'''
#随机浏览器
class  RandomUserAgent:
    def process_request(self,request,spider):
        useragent=random.choice(USER_AGENTS)#随机选择一个代理
        request.headers.setdefault("User-Agent",useragent) #代理
#随机代理
class  RandomProxy:
    def process_request(self,request,spider):
        proxy=random.choice(PROXIES)
        if proxy["user_passwd"] is None:
            request.meta["proxy"]="http://"+proxy["ip_port"] #没有代理密码就直接登陆
        else:
            #账户密码进程编码
            base64_userpassword=base64.b64encode(proxy["user_passwd"].encode("utf-8") )
            request.headers["Proxy-Authorization"]="Basic "+ base64_userpassword.decode("utf-8")
            request.meta["proxy"]="http://"+proxy["ip_port"]
'''


class BaidubaikeSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
