import scrapy
from  scrapy import cmdline

# pycharm执行风格
cmdline.execute(["scrapy" , "runspider" , "./example/spiders/baikeCrawler_redis.py"])
