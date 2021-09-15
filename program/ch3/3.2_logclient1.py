# -*- coding: utf-8 -*-
"""
logclient1.pyプログラム
データロガー　クライアントプログラム(1)
50000番ポートで、サーバに接続します
接続後、標準入力から読み込んだメッセージをサーバに送ります
"q"が入力されるまで繰り返します
使いかた　c:\>python logclient1.py
"""

# モジュールのインポート
import socket
import sys

# グローバル変数
HOST = "localhost" # 接続先ホストの名前
PORT = 50000       # ポート番号

# メイン実行部
# ソケットの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# サーバとの接続
try:
    client.connect((HOST, PORT))
except:
    print("接続できません")
    sys.exit()
# サーバへのメッセージの送信
while True:  # "q"が入力されるまで繰り返す
    msg = input()
    if msg == "q":   #終了
        break
    client.sendall(msg.encode("utf-8"))
# コネクションのクローズ
client.close()                             
# logclient1.pyの終わり