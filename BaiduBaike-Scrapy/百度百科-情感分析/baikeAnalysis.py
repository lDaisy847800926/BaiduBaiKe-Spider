#  -*- coding: utf-8 -*-
#  @IDE :  PyCharm
#  @Time : 2017/11/5 17:39
#  @Author ： Daisy
#  @ProjectNmae : test

'''
What about:

'''
# 获取网页数据
import requests
from bs4 import BeautifulSoup
from aip import AipNlp


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


if __name__ == '__main__':
    pagedata = getData("https://baike.baidu.com/item/Python/407313")
    title = getTitle(pagedata)
    print(title[0] , title[1])
    print("--------------------------------------")



    # 情感分析：语言处理基础技术
    """ 你的 APPID AK SK """
    APP_ID = '10315972'
    API_KEY = 'RKgKNYi8rYGkntz0GgFNuOvg'
    SECRET_KEY = 'fyrbZBzIwfLhehw1dohcW3o7ti2lMA2a '
    aipNlp = AipNlp(APP_ID , API_KEY , SECRET_KEY)

    # 词法分析接口包含了中文分词和词性标注的功能
    result = aipNlp.lexer(title)
    # for key in result:
    #     print(key , result[key])
    print(result)

    # 中文词向量表示
    result = aipNlp.wordEmbedding(title[1])
    print(result)

    # 传入两个词计算两者相似度
    result = aipNlp.wordSimEmbedding('漂亮' , '美丽')
    print(result)

    # 情感倾向分析
    result = aipNlp.sentimentClassify('Python具有丰富和强大的库')
    # +sentiment表示情感极性分类结果, 0:负向，1:中性，2:正向
    print(result)

    # 传入短语，计算中文DNN语言模型，语法结构分析
    result = aipNlp.dnnlm('python是程序设计语言')
    print(result)

    # 传入两个短文本，计算相似度
    result = aipNlp.simnet('python是程序设计语言' , 'c是程序设计语言')
    # score两个文本相似度得分
    print(result)

    # 传入评论文本，获取情感属性
    result = aipNlp.commentTag('面包很好吃')
    print(result)

    # 依存句法分析
    result = aipNlp.depParser('python是最好的语言')
    print(result)
