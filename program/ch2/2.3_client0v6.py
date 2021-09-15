# -*- coding: utf-8 -*-
"""
client0v6.pyプログラム
Pythonによるクライアントソケットの利用法を示す例題プログラム(0)
IPv6による実装例
50000番ポートでサーバに接続します
使いかた　c:\>python client0v6.py
"""

# モジュールのインポート
import socket

# グローバル変数
HOST = "localhost" # 接続先ホストの名前
#HOST = "::1"      # 接続先ホストの名前
PORT = 50000       # ポート番号
BUFSIZE = 4096     # 受信バッファの大きさ

# メイン実行部
# ソケットの作成
client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
# サーバとの接続
client.connect((HOST, PORT))
# サーバからのメッセージの受信
data = client.recv(BUFSIZE)
print(data.decode("UTF-8"))
# コネクションのクローズ
client.close()                             
# client0v6.pyの終わり