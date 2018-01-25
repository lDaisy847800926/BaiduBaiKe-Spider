#  -*- coding: utf-8 -*-
#  @IDE :  PyCharm
#  @Time : 2017/11/4 11:33
#  @Author ： Daisy
#  @ProjectNmae : Server

'''
What about:分布式爬虫服务端

'''
import queue
import multiprocessing.managers

# 任务队列，结果队列
import re
import requests
from bs4 import BeautifulSoup

task_queue = queue.Queue()
result_queue = queue.Queue()


# 返回任务队列
def return_task():
    return task_queue


# 返回结果队列
def return_result():
    return result_queue


class QueueManger(multiprocessing.managers.BaseManager):
    pass


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
    url = "https://baike.baidu.com/item/Python/407313"
    pagedata = getData(url)
    urllist = getUrlList(pagedata)

    # 开启分布式支持
    multiprocessing.freeze_support()

    # 注册函数给客户端调用
    QueueManger.register("get_task" , callable=return_task)
    QueueManger.register("get_result" , callable=return_result)

    manger = QueueManger(address=("127.0.0.1" , 8848) , authkey=123456)
    # 开启
    manger.start()

    task , result = manger.get_task() , manger.get_result()

    for url in urllist:
        print("task add data" , url)
        task.put(url)
    print("waitting for -------------")
    savefile = open("data.txt" , "wb")
    while True:
        res = result.get(timeout=1000)
        print("get data" , res)
        savefile.write(res.encode("utf-8" , "ignore"))
        savefile.flush()
    savefile.close()

    # 关闭服务器
    manger.shutdown()
