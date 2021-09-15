# -*- coding: utf-8 -*-
"""
simplehttpd.pyプログラム
Webサーバプログラム
8080番ポートでHTTP接続を待ち受けます
Ctrl+Cで終了します
使いかた　c:\>python simplehttpd.py
"""

# モジュールのインポート
import http.server

# グローバル変数
PORT = 8080      # ポート番号

# メイン実行部
# 事前設定
handlerclass = http.server.SimpleHTTPRequestHandler
simpled = http.server.HTTPServer(("",PORT), handlerclass)
# サーバの実行
simpled.serve_forever()
# simplehttpd.pyの終わり
