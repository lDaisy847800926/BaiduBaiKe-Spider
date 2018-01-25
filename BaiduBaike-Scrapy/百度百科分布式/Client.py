#  -*- coding: utf-8 -*-
#  @IDE :  PyCharm
#  @Time : 2017/11/4 11:33
#  @Author ： Daisy
#  @ProjectNmae : Client

'''
What about:分布式爬虫客户端

'''
import multiprocessing.managers

# 继承multiprocessing.managers，进程管理共享数据
import re
import requests
import time
from bs4 import BeautifulSoup


class QueueManger(multiprocessing.managers.BaseManager):
    pass


# 获取网页数据
def getData(url):
    url = "https://baike.baidu.com/item/Python/407313"
    # 伪装浏览器
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  # 模拟浏览器
    headers = {'User-Agent': user_agent}
    response = requests.get(url , headers=headers)

    if response.status_code == 200:
        response.encoding = "utf-8"  # 设置编码
        return response.text
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
    # 注册函数调用服务器
    QueueManger.register("get_task")
    QueueManger.register("get_result")

    # 连接服务器
    manger = QueueManger(address=("127.0.0.1" , 8848) , authkey=123456)
    manger.connect()

    # 任务，结果
    task = manger.get_task()
    result = manger.get_result()

    for i in range(100):
        time.sleep(1)
        try:
            url = task.get()
            print("client get" , url)
            datalist = getUrlList(url)
            for line in datalist:
                result.put(line)
        except:
            pass
