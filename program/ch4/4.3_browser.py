# -*- coding: utf-8 -*-
"""
browser.pyプログラム
webbrowserのサンプルプログラム
指定したURLを、ブラウザを使って開きます
使いかた　c:\>python browser.py
"""

# モジュールのインポート
import webbrowser

# グローバル変数
DURL = "http://localhost:8080/"   # デフォルトの取得先URL

# メイン実行部
# 取得先URLの設定
url = input("取得先URL：")
if url == "":                     # デフォルトのURLを設定
    url = DURL
# URLを開く
webbrowser.open(url)
# browser.pyの終わり
