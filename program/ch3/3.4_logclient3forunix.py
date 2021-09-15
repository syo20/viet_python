# -*- coding: utf-8 -*-
"""
logclient3forunix.pyプログラム
注意　このプログラムはunix系OSでのみ稼働します（Windwos不可）
データロガー　クライアントプログラム(3)
50000番ポートで、サーバに接続します
接続後、定期的にコンピュータの負荷の状況をサーバに送信します
使いかた　$python3 logclient3forunix.py
"""

# モジュールのインポート
import socket
import sys
import os
import time

# グローバル変数
PORT = 50000       # ポート番号
SLEEPTIME = 10     # 待ち合わせ時間

# メイン実行部
# unix系OSであることのチェック（Windowsでは稼働しない）
if os.name != "posix":
    print("本プログラムは、unix系OS以外では稼働しません")
    sys.exit()
# 接続先の設定
host = input("接続先サーバ：")
# サーバへのメッセージの送信
while True:  # 無限ループ
    # ソケットの作成
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    try:
        client.connect((host, PORT))
    except:
        print("接続できません")
        sys.exit()
    loadave = os.getloadavg()  # unix系OSにおける負荷測定
    print(loadave)
    client.sendall(str(loadave).encode('utf-8'))
    # コネクションのクローズ
    client.close()   
    # 一定時間待ち合わせる
    time.sleep(SLEEPTIME)                          
# logclient3forunix.pyの終わり
