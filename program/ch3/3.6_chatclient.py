# -*- coding: utf-8 -*-
"""
chatclient.pyプログラム
Pythonによるチャットプログラム(1)　UDP版クライアント
50000番ポートで接続を待ち受けてます
クライアントとメッセージを交換します
Ctrl+Breakで終了します
使いかた　c:\>python chatclient.py
"""

# モジュールのインポート
import socket
import threading
import sys

# グローバル変数
PORT = 50000     # ポート番号
BUFSIZE = 4096   # 受信バッファの大きさ

#下請け関数の定義
#server_handler()関数
def server_handler(client):
    """
    サーバとの接続処理スレッド
    """
    while True:
        try:
            data = client.recv(BUFSIZE)   # サーバより受信 
            print(data.decode("UTF-8"))   # 受信内容の出力
        except:                           # エラー対応
            sys.exit()
    client.close()                        # コネクションのクローズ
#server_handler()関数の終わり

# メイン実行部
# ソケットの作成
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# サーバの設定
host = input("接続先サーバ：")
if host == "":        # デフォルト設定
    host = "localhost" 
# 送受信処理
# スレッドの設定
p = threading.Thread(target = server_handler,
                     args = (client,))
p.setDaemon(True)
#メッセージの送信
while True:
    msg = input("")
    client.sendto(msg.encode("UTF-8"), (host, PORT))
    if msg == "q":    # quit
        break         # 接続終了
    # スレッドの起動
    if not p.is_alive():
        p.start()     # 未起動の場合、一回だけ起動する
client.close()      
# chatclient.pyの終わり