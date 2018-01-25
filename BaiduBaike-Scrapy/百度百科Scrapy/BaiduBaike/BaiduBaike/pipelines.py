# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql

class BaidubaikePipeline(object):

    def __init__(self):
        client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
        self.db = client
        # 新建一个数据库
        self.users = self.db["baike"]

    # 插入数据标题，内容，链接到数据库中
    def process_item(self , item , spider):
        self.users["baike"].insert({
            "title": item["title"] ,
            "content": item["content"] ,
            "url": item["url"]
        })
        return item

    def __del__(self):
        self.db.close()


    '''
    def __init__(self):
        self.mysql = pymysql.connect(
            host="127.0.0.1" ,
            port=3306 ,
            user="root" ,
            password="root" ,
            db="project" ,
            charset="utf8"
        )

    def __del__(self):
        self.mysql.close()

    def process_item(self , item , spider):
        sql = """insert into  caijingblogx(title,content,url) VALUES ('%s','%s','%s')""" \
              % (item["title"] , item["content"] , item["url"])
        self.mysql.query(sql)
        self.mysql.commit()

        return item
'''

'''
    def __init__(self):
        self.file = open("baike.txt" , "w")

    def __del__(self):
        self.file.close()

    def process_item(self , item , spider):
        self.file.write(str(item))
        self.file.flush()
        return item
'''
