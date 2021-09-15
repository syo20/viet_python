# -*- coding: utf-8 -*-
"""
server0.pyプログラム
Pythonによるサーバソケットの利用法を示す例題プログラム(0)
50000番ポートで接続を待ち受けて、メッセージを返します
1回だけ接続し、その後プログラムを終了します
使いかた　c:\>python server0.py
"""

# モジュールのインポート
import socket

# グローバル変数
PORT = 50000      # ポート番号

# メイン実行部
# ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# アドレスの設定
server.bind(("",PORT))
# 接続の待ち受け
server.listen()

# クライアントへの対応処理
client, addr = server.accept()             # 通信用ソケットの取得 
client.sendall(b"Hi, nice to meet you!\n") # メッセージの送信
client.close()                             # コネクションのクローズ
server.close()                             # サーバソケットのクローズ
# server0.pyの終わり
