# -*- coding: utf-8 -*-
"""
server3.pyプログラム
Pythonによるサーバソケットの利用法を示す例題プログラム(3)
50000番ポートで接続を待ち受けてます
クライアントからの入力後、時刻を返します
接続時にコンソールにメッセージを出力します
スレッドを用いて並行処理を行います
Ctrl+Breakで終了します
使いかた　c:\>python server3.py
"""

# モジュールのインポート
import socket
import datetime 
import threading

# グローバル変数
PORT = 50000     # ポート番号
BUFSIZE = 4096   # 受信バッファの大きさ

#下請け関数の定義
#client_handler()関数
def client_handler(client, clientno, msg):
    """
    クライアントとの接続処理スレッド
    """
    data = client.recv(BUFSIZE)          # クライアントより受信 
    print("(", clientno, ")",           
          data.decode("UTF-8"))          # 受信内容の出力
    client.sendall(msg.encode("utf-8"))  # メッセージの送信
    client.close()                       # コネクションのクローズ
#client_handler()関数の終わり

# メイン実行部
# ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# アドレスの設定
server.bind(("", PORT))
# 接続の待ち受け
server.listen()
#　クライアントの受付番号の初期化
clientno = 0

# クライアントへの対応処理
while True:                                 # 対応の繰り返し
    client, addr = server.accept()          # 通信用ソケットの取得
    clientno += 1                           # 受付番号のカウントアップ 
    msg = str(datetime.datetime.now())      # メッセージの作成
    print(msg,"接続要求あり(",clientno,")")
    print(client)
    # スレッドの設定と起動
    p = threading.Thread(target = client_handler,
                         args = (client, clientno, msg))
    p.start()  
# server3.pyの終わり