# -*- coding: utf-8 -*-
import feedparser
import time
import pandas as pd

def main():

    #RSSデータ取得
    pds = getRss()

    html_body = u"""<html>
                    <head><meta http-equiv="content-type" content="text/html;charset=utf-8">
                    <link href="../css/sample.css" rel="stylesheet" type="text/css"/>
                    <title>GISアンテナ</title>
                    </head>
                    <body>
                    <div id="pagebody">
                    	<!-- ヘッダ -->
                    	<div id="header"><h1>GISアンテナ</h1></div>
                    	<!-- メインメニュー -->
                    	<ul id="menu">
                    		<li id="menu01"><a href="https://www.google.co.jp/maps" target="_blank">GoogleMap</a></li>
                    		<li id="menu02"><a href="https://www.google.co.jp/intl/ja/earth/" target="_blank">GoogleEarth</a></li>
                    		<li id="menu03"><a href="http://user.numazu-ct.ac.jp/~tsato/webmap/map/gmap.html?data=history" target="_blank">地理院地図</a></li>
                    		<li id="menu04"><a href="http://www.mapion.co.jp/route/" target="_blank">距離測</a></li>
                    		<li id="menu05"><a href="http://www.its-mo.com/" target="_blank">いつもNAVI</a></li>
                    	</ul>
                        <div id="news"><h2>最新記事一覧</h2>
                        <div id="scr"><ul id>
                        """
    cnt = 0
    #最新記事一覧を作成
    for i,row in pds.sort("time",ascending=False).iterrows():
        #表示件数を絞る
        if cnt == 10:
            break
        if row.flg == "0":
            html_body += "<li id =" + "inline" + ">" + row.time + "   " + "<a href=" + row.link + " target" + "=_blank>" + row.title + "</a></li>"
        cnt += 1
    html_body += "</div></div></ul><div id=" + "content" + "><ul id=" + "list" + ">"

    for i,row in pds.iterrows():
        if row.flg == "1":
            html_body += u"<h2><a class=" + "feed-link href=" + row.link + " target" + "=_blank>"  + row.title + "</a></h2>"

        elif row.flg == "0":
            html_body += u"<li id= " + "inline" + "><a href=" + row.link + " target" + "=_blank>"  + row.title + "</a></li>"

    html_body += u"""</ul></div><div id="footer">
                     <address>Copyright (c) GISアンテナ All Rights Reserved.</address></div></div></body></html>
                     """
    print('Content-type: text/html')
    print(html_body.encode('utf-8'))

def getRss():
    lists =[]

    #対象のRSS
    lists.append("https://www.gisa-japan.org/news/rss.xml")
    lists.append("http://www.gsi.go.jp/index.rdf")
    lists.append("http://www.esrij.com/feed/")
    lists.append("http://www.jodc.go.jp/jodcweb/cgi-bin/public/newsrss1.cgi?lang=ja")
    lists.append("http://www.npo-zgis.or.jp/rss.xml")

    rssList = []
    for i,l in enumerate(lists):
        rss = feedparser.parse(l)
        rssList.append([rss.feed.title,rss.feed.link,"",i,"1"])
        #RSS情報をリストに格納
        for entry in rss.entries:
            #RSS情報をリストに格納
            rssList.append([entry.title,entry.link,time.strftime('%Y/%m/%d %X',entry.updated_parsed),i,"0"])

    #RSS情報をデータフレームに格納
    pds = pd.DataFrame(rssList)
    pds.columns = ["title","link","time","category","flg"]
    return pds

if __name__ == '__main__':
    main()
