# -*- coding: utf-8 -*-
"""
server2.pyプログラム
Pythonによるサーバソケットの利用法を示す例題プログラム(2)
50000番ポートで接続を待ち受けます
クライアントからの入力後、時刻を返します
接続時にコンソールにメッセージを出力します
Ctrl+Breakで終了します
使いかた　c:\>python server2.py
"""

# モジュールのインポート
import socket
import datetime 

# グローバル変数
PORT = 50000      # ポート番号
BUFSIZE = 4096    # 受信バッファの大きさ

# メイン実行部
# ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# アドレスの設定
server.bind(("",PORT))
# 接続の待ち受け
server.listen()

# クライアントへの対応処理
while True:                                    # 対応の繰り返し
    client, addr = server.accept()             # 通信用ソケットの取得
    msg = str(datetime.datetime.now())         # メッセージの作成
    print(msg,"接続要求あり")
    print(client)
    data = client.recv(BUFSIZE)                # クライアントより受信 
    print(data.decode("UTF-8"))                # 受信内容の出力
    client.sendall(msg.encode("utf-8"))        # メッセージの送信
    client.close()                             # コネクションのクローズ
# server2.pyの終わり