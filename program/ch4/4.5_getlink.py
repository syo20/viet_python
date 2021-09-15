# -*- coding: utf-8 -*-
"""
getlink.pyプログラム
urllibとHTMLParserのサンプルプログラム
指定したURLからHTMLファイルを取得し、リンク情報を取り出します
使いかた　c:\>python getlink.py
"""

# モジュールのインポート
import urllib.request
from html.parser import HTMLParser

# グローバル変数
DURL = "http://localhost:8080/"   # デフォルトの取得先URL

# 下請け関数の定義
# HTMLParserの利用
class MyHTMLParser(HTMLParser):
    # タグの開始に関する処理
    def handle_starttag(self, tag, attrs):
        #リンクを探す
        if tag == "a": # <a>タグを見つける
            print(attrs)
    # タグの終了に関する処理
    def handle_endtag(self, tag):
        pass  # 何もしない
    # データに関する処理
    def handle_data(self, data):
        pass # 何もしない

# メイン実行部
# 取得先URLの設定
url = input("取得先URL：")
if url == "":#デフォルトのURLを設定
    url = DURL
# 文字コードの設定
chcode = input("文字コード：")
if chcode == "":#デフォルトの文字コードを設定
    chcode = "UTF-8"
# URLを開く
urlinfo = urllib.request.urlopen(url)
# HTMLファイルを取得する
html = urlinfo.read()
# リンク先の出力
parser = MyHTMLParser()
parser.feed(html.decode(chcode))
# getlink.pyの終わり
