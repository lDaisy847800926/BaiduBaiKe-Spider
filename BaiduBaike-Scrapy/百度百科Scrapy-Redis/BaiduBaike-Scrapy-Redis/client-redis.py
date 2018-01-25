import redis

myredis = redis.Redis(host="127.0.0.1" , password="" , port=6379)
# print(myredis.info())
url = "https://baike.baidu.com/item/Python/407313"
myredis.lpush("baikeCrawler:start_urls" , url)
