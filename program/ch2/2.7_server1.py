# -*- coding: utf-8 -*-
"""
server1.pyプログラム
Pythonによるサーバソケットの利用法を示す例題プログラム(1)
50000番ポートで接続を待ち受けて、時刻を返します
接続時にコンソールにメッセージを出力します
Ctrl+Breakで終了します
使いかた　c:\>python server1.py
"""

# モジュールのインポート
import socket
import datetime 

# グローバル変数
PORT = 50000      # ポート番号

# メイン実行部
# ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# アドレスの設定
server.bind(("" PORT))
# 接続の待ち受け
server.listen()

# クライアントへの対応処理
while True:                                    # 対応の繰り返し
    client, addr = server.accept()             # 通信用ソケットの取得 
    msg = str(datetime.datetime.now())         # メッセージの作成
    client.sendall(msg.encode("UTF-8"))        # メッセージの送信
    print(msg, "接続要求あり")
    print(client)
    client.close()                             # コネクションのクローズ
# server1.pyの終わり