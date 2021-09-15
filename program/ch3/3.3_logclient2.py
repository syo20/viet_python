# -*- coding: utf-8 -*-
"""
logclient2.pyプログラム
データロガー　クライアントプログラム(2)
50000番ポートで、サーバに接続します
接続後、ファイルから読み込んだメッセージをサーバに送ります
使いかた　c:\>python logclient2.py
"""

# モジュールのインポート
import socket
import sys

# グローバル変数
HOST = "localhost"    # 接続先ホストの名前
PORT = 50000          # ポート番号
DATAFILE = "data.txt" # 転送ファイル名

# メイン実行部
# ファイルオープン
fin = open(DATAFILE, "rt")  
# ソケットの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# サーバとの接続
try:
    client.connect((HOST, PORT))
except:
    print("接続できません")
    sys.exit()
# サーバへのメッセージの送信
msg = fin.read()
client.sendall(msg.encode("utf-8"))
# コネクションのクローズ
client.close()                             
# logclient2.pyの終わり
