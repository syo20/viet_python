# -*- coding: utf-8 -*-
"""
logserver.pyプログラム
データロガー　サーバプログラム
50000番ポートで接続を待ち受けて、データを受け取ります
受け取ったデータをファイルに保存します
Ctrl+Breakで終了します
使いかた　c:\>python logserver.py
"""

# モジュールのインポート
import socket
import  datetime

# グローバル変数
PORT = 50000      # ポート番号
BUFSIZE = 4096    # 受信バッファの大きさ

# メイン実行部
# ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# アドレスの設定
server.bind(("", PORT))
# 接続の待ち受け
server.listen()

# クライアントへの対応処理
while True:                                  # 対応の繰り返し
    client, addr = server.accept()           # 通信用ソケットの取得
    d = datetime.datetime.now()              # 現在時刻の取得
    fname = d.strftime("%m%d%H%M%S%f")       # 文字列へ変換
    print(fname, "接続要求あり")               # 接続先を端末に表示
    print(client)
    fout = open(fname + ".txt", "wt")        # 書き込みファイルオープン
    try:
        while True:
            data = client.recv(BUFSIZE)      # クライアントより受信 
            if not data:                     # 受信するものがないなら
                break ;                      # 受信終了
            print(data.decode("UTF-8"))      # 受信内容の出力
            print(data.decode("UTF-8"),
                  file = fout)               # ファイルへの書き込み
    except:                                  # エラーへの対応
        print("エラーが発生しました")
    client.close()                           # コネクションのクローズ
    fout.close()                             # ファイルのクローズ
    print("接続処理終了（", fname, ")")
# logserver.pyの終わり
