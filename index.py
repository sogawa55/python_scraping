# -*- coding: utf-8 -*-

from bottle import route, run
from bottle import TEMPLATE_PATH, jinja2_template as template
import os
import feedparser
import time
import sys

# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/views")
# テスト
@route('/')
def top():

    # 配列を渡すための準備


    lists =[]

#対象のRSS
    lists.append("https://www.gisa-japan.org/news/rss.xml")
    lists.append("http://www.gsi.go.jp/index.rdf")
    lists.append("http://www.esrij.com/feed/")
    lists.append("http://www.jodc.go.jp/jodcweb/cgi-bin/public/newsrss1.cgi?lang=ja")
    lists.append("http://www.npo-zgis.or.jp/rss.xml")
    lists.append("http://www.uqwimax.jp/annai/news_release/index.xml")



    titleList = []

    for l in lists:
         rss = feedparser.parse(l)
         titleList.append([rss.feed.title])
         #RSS情報をリストに格納
         for entry in rss.entries:
             #RSS情報をリストに格納
             titleList.append([entry.title])

    kaisuu = len(titleList)
    kazu = int(kaisuu)

    linkList = []

    for l2 in lists:
        rss2 = feedparser.parse(l2)
        linkList.append([rss2.feed.link])

        for entry2 in rss2.entries:

            linkList.append(entry2.link)

    timeList = []

    for l3 in lists:
        rss3 = feedparser.parse(l3)

        for entry in rss3.entries:
            timeList.append(entry.updated)


    #コメントでーーーーーーーーーーす
    List = zip(titleList,linkList,timeList)

    rssuq = feedparser.parse("http://www.mitsubishi-motors.co.jp/component/documents/news_message.xml")
    #コメントでーーーーーーーーーーす3

    #コメントでーーーーーーーーーーす2
    uqlinkList = []
    uqlinkList.append(rssuq.feed.link)
    for entryuq in rssuq.entries:
        uqlinkList.append(entryuq.link)

    rssuq2 = feedparser.parse("http://www.mitsubishi-motors.co.jp/component/documents/news_message.xml")
    uqtitleList = []
    uqtitleList.append(rssuq2.feed.title)
    for entryuq2 in rssuq2.entries:
        uqtitleList.append(entryuq2.title)

    uqtimeList = []
    rssuq3 = feedparser.parse("http://www.mitsubishi-motors.co.jp/component/documents/news_message.xml")
    for entryuq3 in rssuq3.entries:
        uqtimeList.append(entryuq3.updated)

    uqList = zip(uqtitleList,uqlinkList,uqtimeList)


    fizzbuzz = []
    for i in range(1, 100):

        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz.append(str(i) + ": fizzbuzz")
        elif i % 3 == 0:
            fizzbuzz.append(str(i) + ": fizz")
        elif i % 5 == 0:
            fizzbuzz.append(str(i) + ": buzz")
        else:
            fizzbuzz.append(str(i))

    return template('top', name="umentu", fizzbuzz=fizzbuzz, List=List,uqList=uqList)

if __name__ == "__main__":
    run(host="localhost", port=8081, debug=True, reloader=True)
