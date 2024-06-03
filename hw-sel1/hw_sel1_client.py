import socket
import threading
port = 2500
def handler(sock):
    while True:
        msg = sock.recv(1024)
        print(msg.decode())
svr_addr = ('localhost', port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(svr_addr)
my_id = input('ID를 입력하세요: ')
sock.send(('['+my_id+']').encode())
th = threading.Thread(target=handler, args=(sock,))
th.daemon = True
th.start()
while True:
    msg = '[' + my_id + '] ' + input()
    sock.send(msg.encode())