# -*- coding: utf-8 -*-
"""
minihttpd.pyプログラム
最低限の動作をするWebサーバプログラム
8080番ポートでクライアントからの接続を待ち受けます
クライアントから接続を受け付けたら、特定のhtmlファイルを送ります
Ctrl+Breakで終了します
使いかた　c:\>python minihttpd.py
"""

# モジュールのインポート
import socket

# グローバル変数
PORT = 8080               # ポート番号
BUFSIZE = 4096            # 受信バッファの大きさ
INDEX_HTML = "index.html" # HTMLファイル

# メイン実行部
#　htmlレスポンスの設定
fin = open(INDEX_HTML, "rt") 
msg = fin.read()
fin.close()
msg = "HTTP/1.0 200 OK\n\n" + msg              # ステータスラインの付加

# ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# アドレスの設定
server.bind(("",PORT))
# 接続の待ち受け
server.listen()

# クライアントへの対応処理
while True:                                    # 対応の繰り返し
    client, addr = server.accept()             # 通信用ソケットの取得
    data = client.recv(BUFSIZE)                # クライアントより受信 
    print(data.decode("UTF-8"))                # 受信内容の出力
    client.sendall(msg.encode("cp932"))        # レスポンスの送信
    client.close()                             # コネクションのクローズ
# minihttpd.pyの終わり
