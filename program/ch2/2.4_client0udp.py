# -*- coding: utf-8 -*-
"""
client0udp.pyプログラム
Pythonによるクライアントソケットの利用法を示す例題プログラム(0)UDP版
50000番ポートでUDPでサーバからデータを取得します
使いかた　c:\>python client0udp.py
"""

# モジュールのインポート
import socket

# グローバル変数
HOST = "localhost"  # 接続先ホストの名前
#HOST = "127.0.0.1" # 接続先ホストの名前
PORT = 50000        # ポート番号
BUFSIZE = 4096      # 受信バッファの大きさ

# メイン実行部
# ソケットの作成
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# サーバへの情報の要求
client.sendto(b"Hi!", (HOST, PORT))
# サーバからのメッセージの受信
data = client.recv(BUFSIZE)
print(data.decode("UTF-8"))
# ソケットのクローズ
client.close()                             
# client0udp.pyの終わり