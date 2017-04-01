# -*- coding: utf-8 -*-

from bottle import route, run
from bottle import TEMPLATE_PATH, jinja2_template as template
import os
import feedparser
import time
import sys

# index.pyのディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/views")

#ルーティング
@route('/')
def top():

    #techcrunch用の空のリストを作成
    techcrunch_List = []

    #techcrunch用のリンクをパースして配列に格納
    rss_techcrunch = feedparser.parse("http://jp.techcrunch.com/feed/")
    techcrunch_linkList = []
    techcrunch_linkList.append(rss_techcrunch.feed.link)
    for entry_techcrunch in rss_techcrunch.entries:
        techcrunch_linkList.append(entry_techcrunch.link)

    #techcrunch用のタイトルをパースして配列に格納
    rss_techcrunch2 = feedparser.parse("http://jp.techcrunch.com/feed/")
    techcrunch_titleList = []
    techcrunch_titleList.append(rss_techcrunch2.feed.title)
    for entry_techcrunch2 in rss_techcrunch2.entries:
        techcrunch_titleList.append(entry_techcrunch2.title)

    #techcrunch用の更新時間をパースして配列に格納
    rss_techcrunch3 = feedparser.parse("http://jp.techcrunch.com/feed/")
    techcrunch_timeList = []
    for entry_techcrunch3 in rss_techcrunch3.entries:
        techcrunch_timeList.append(entry_techcrunch3.updated)

    #techcrunch用のタイトル、リンク、更新時間の配列をZIP関数でマージ
    techcrunch_List = zip(techcrunch_titleList,techcrunch_linkList,techcrunch_timeList)

    #WIRED用の空のリストを作成
    wired_List = []

    #WIRED用のリンクをパースして配列に格納
    rss_wired = feedparser.parse("http://wired.jp/rssfeeder/")
    wired_linkList = []
    wired_linkList.append(rss_techcrunch.feed.link)
    for entry_wired in rss_wired.entries:
        wired_linkList.append(entry_wired.link)

    #WIRED用のタイトルをパースして配列に格納
    rss_wired2 = feedparser.parse("http://wired.jp/rssfeeder/")
    wired_titleList = []
    wired_titleList.append(rss_wired2.feed.title)
    for entry_wired2 in rss_wired2.entries:
        wired_titleList.append(entry_wired2.title)

    #WIRED用の更新時間をパースして配列に格納
    rss_wired3 = feedparser.parse("http://wired.jp/rssfeeder/")
    wired_timeList = []
    for entry_wired3 in rss_wired3.entries:
        wired_timeList.append(entry_wired3.updated)

    #WIRED用のタイトル、リンク、更新時間の配列をZIP関数でマージ
    wired_List = zip(wired_titleList,wired_linkList,wired_timeList)

    return template('top',wired_List=wired_List,techcrunch_List=techcrunch_List)

if __name__ == "__main__":
    run(host="localhost", port=8081, debug=True, reloader=True)
