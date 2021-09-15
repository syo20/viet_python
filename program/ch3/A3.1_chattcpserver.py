# -*- coding: utf-8 -*-
"""
chattcpserver.pyプログラム
Pythonによるチャットプログラム(1)　TCP版サーバ
50000番ポートで接続を待ち受けてます
クライアントとメッセージを交換します
Ctrl+Breakで終了します
使いかた　c:\>python chattcpserv.py
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
def client_handler(client, addr):
    """
    クライアントとの接続処理スレッド
    """
    while True:
        try:
            data = client.recv(BUFSIZE)   # クライアントより受信 
        except:                           # 受信できなければ
            clist.remove(client)          # リストから取り除く
            break                         # 終了
        if (not data) or (data.decode("UTF-8") == "q"):   # quit
            clist.remove(client)          # リストから取り除く
            break                         # 終了
        msg = str(addr) + ">" + data.decode("UTF-8")      # 発信元を付加  
        print(msg)                        # 受信内容の出力
        for c in clist:                   # クライアントに配信
            c.sendall(msg.encode("UTF-8"))
    client.close()                        # コネクションのクローズ
#client_handler()関数の終わり

# メイン実行部
# ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# アドレスの設定
server.bind(("", PORT))
# 接続の待ち受け
server.listen()

# クライアントへの対応処理
clist = []                               # クライアントのリスト
while True:                              # 対応の繰り返し
    client, addr = server.accept()       # 通信用ソケットの取得
    clist.append(client)                 # クライアントの追加
    # スレッドの設定と起動
    p = threading.Thread(target = client_handler,
                         args = (client, addr))
    p.start()   
# chattcpserv.pyの終わり
