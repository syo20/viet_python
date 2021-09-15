# -*- coding: utf-8 -*-
"""
chatserv.pyプログラム
Pythonによるチャットプログラム(1)　UDP版サーバ
50000番ポートで接続を待ち受けてます
クライアントとメッセージを交換します
Ctrl+Breakで終了します
使いかた　c:\>python chatserv.py
"""

# モジュールのインポート
import socket

# グローバル変数
PORT = 50000     # ポート番号
BUFSIZE = 4096   # 受信バッファの大きさ

# メイン実行部
# ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# アドレスの設定
server.bind(("", PORT))

# クライアントへの対応処理
clist = []       # クライアントのリスト
# 対応の繰り返し
while True:
    data, client = server.recvfrom(BUFSIZE) # 通信用ソケットの取得
    if not (client in clist):
        clist.append(client)                # クライアントの追加
    if data.decode("UTF-8") == 'q':         # quit
        clist.remove(client)                # リストから取り除く
    else :
        msg = str(client) + ">"             # 発信元を付加
        msg += data.decode("UTF-8")  
        print(msg)                          # 受信内容の出力
        for c in clist:                     # クライアントに配信
            server.sendto(msg.encode("UTF-8"),c)  
# chatserv.pyの終わり
