# -*- coding: utf-8 -*-
"""
chattcpclient.pyプログラム
Pythonによるチャットプログラム(1)　TCP版クライアント
50000番ポートで接続を待ち受けてます
クライアントとメッセージを交換します
Ctrl+Breakで終了します
使いかた　c:\>python chattcpclient.py
"""

# モジュールのインポート
import socket
import sys
import threading

# グローバル変数
PORT = 50000     # ポート番号
BUFSIZE = 4096   # 受信バッファの大きさ

# 下請け関数の定義
# server_handler()関数
def server_handler(client):
    """
    サーバとの接続処理スレッド
    """
    while True:
        try :
            data = client.recv(BUFSIZE)   # サーバより受信 
        except :                          # 受信できなければ
            break                         # 終了
        if (not data) or (data.decode("UTF-8") == "q"):
            break                         # 接続終了
        print(data.decode("UTF-8"))       # 受信内容の出力
    client.close()                        # コネクションのクローズ
#server_handler()関数の終わり

# メイン実行部
# ソケットの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# サーバとの接続
host = input("接続先サーバ：")
if host == "":        # デフォルト設定
    host = "localhost" 
try:
    client.connect((host, PORT))
except:
    print("接続できません")
    sys.exit()
# 送受信処理
# スレッドの設定と起動
p = threading.Thread(target = server_handler,
                     args = (client,))
p.start() 
# メッセージの送信
while True:
    msg = input("")
    client.sendall(msg.encode("utf-8"))
    if msg == "q":    # quit
        break         # 接続終了
client.close()      
# chattcpclient.pyの終わり
