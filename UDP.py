import RPi.GPIO as GPIO             #GPIO用のモジュールをインポート
import socket
import concurrent.futures

#ポート番号の定義
Servo_pin1 = 12                      #変数"Servo_pin"に18を格納
Servo_pin2 = 19
#GPIOの設定
GPIO.setmode(GPIO.BCM)              #GPIOのモードを"GPIO.BCM"に設定
GPIO.setup(Servo_pin1, GPIO.OUT)     #GPIO18を出力モードに設定
GPIO.setup(Servo_pin2, GPIO.OUT)     #GPIO18を出力モードに設定
Servo1 = GPIO.PWM(Servo_pin1, 50)     #GPIO.PWM(ポート番号, 周波数[Hz])
Servo2 = GPIO.PWM(Servo_pin2, 50)     #GPIO.PWM(ポート番号, 周波数[Hz])
Servo1.start(0)                      #Servo.start(デューティ比[0-100%])
Servo2.start(0)                      #Servo.start(デューティ比[0-100%])

class TcpServer:
    def __init__(self, address, port, recv_size=1024):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((address, port)) 
        self.socket.listen(5)

        print('クライアントデバイスからの接続待ち....')
        self.client_socket, self.client_info = self.socket.accept()
        print("接続完了")

        self.recv_func = lambda: self.client_socket.recv(recv_size)
        self.send_func = lambda data: self.client_socket.send(data)

        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

    def recv_str(self):
        future = self.executor.submit(self.recv_func)
        result = future.result()
 # 受け取ったデータをutf8にデコードする
        return bytes(result).decode('utf-8')

    def send_str(self, data):
        self.executor.submit(self.send_func, bytes(data.encode('utf-8')))
        
# coding=utf-8
#from tcp_server import *

if __name__ == '__main__':

# ドメイン名、もしくはIPアドレス。
# ドメイン名は socket.gethostname() で取得することもできる。
    host = "192.168.1.170"


 # wellknownと衝突しない適当なポート番号
    port = 55555

    connection = TcpServer(host, port)

    try:
        while True:
            data = connection.recv_str()
            print(data)
            srvdata1=data.split(",")
            srvdata2=srvdata1[1].split(".")
            srv1_d=int(srvdata1[0])
            srv2_d=int(srvdata2[0])

            duty1 = 2.5 + (12.0 - 2.5) * srv1_d / 1000   #角度からデューティ比を求める
            if duty1 >= 12 :
                duty1 = 12
            elif duty1 <= 2.5 :
                duty1 = 2.5
            Servo1.ChangeDutyCycle(duty1)     #デューティ比を変更

            duty2 = 2.5 + (12.0 - 2.5) * srv2_d / 1000   #角度からデューティ比を求める
            if duty2 >= 12 :
                duty2 = 12
            elif duty2 <= 2.5 :
                duty2 = 2.5
            Servo2.ChangeDutyCycle(duty2)     #デューティ比を変更

            """
            if data == 'ON_CLICK_BUTTON_UPPER':
                print("ON_CLICK_BUTTON_UPPER")

            elif data == 'ON_CLICK_BUTTON_LEFT':
                print("ON_CLICK_BUTTON_LEFT")

            elif data == 'ON_CLICK_BUTTON_RIGHT':
                print("ON_CLICK_BUTTON_RIGHT")

            elif data == 'ON_CLICK_BUTTON_LOWER':
                print("ON_CLICK_BUTTON_LOWER")

            elif data == 'ON_CLICK_BUTTON_QUIT':
                print("ON_CLICK_BUTTON_QUIT")
                quit()
            """
    finally:
        connection.close()

