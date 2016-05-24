# -*-coding:utf-8-*-
__author__ = 'howie'
import time
import toutiao.touTiaoSpider as ts
import sina.sinaSpider as ss

ss.cate = ["news_world", "news_sports", "news_finance", "news_society", "news_entertainment", "news_military",
           "news_tech"]


# ss.getSinaNews(5000,2,type=ss.cate)

def touTiao(category, page, num, time):
    # 爬取今日头条
    for cate in category:
        ts.getToutiaoNews(cate, page, num, time)


def sina(num=5000, page=1, type=ss.cate):
    # 爬取新浪新闻
    ss.getSinaNews(num, page, type)


touTiao(category=ts.category, page=10, num=20, time=time.time())
sina()