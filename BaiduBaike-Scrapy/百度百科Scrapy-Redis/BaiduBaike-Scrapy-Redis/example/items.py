# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item , Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose , TakeFirst , Join
import scrapy


class BaikeItem(scrapy.Item):
    # 标题
    title = Field()
    # 内容
    content = Field()
    # 链接
    url = Field()
    # 爬取时间
    crawled = Field()
    # 谁爬取
    spider = Field()


class ExampleItem(Item):
    name = Field()
    description = Field()
    link = Field()
    crawled = Field()
    spider = Field()
    url = Field()


class ExampleLoader(ItemLoader):
    default_item_class = ExampleItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
