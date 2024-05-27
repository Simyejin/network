from socket import *
import threading
import time

port = 2500
BUFSIZE = 1024
clients = []

def echoTask(sock, addr):
    while True:
        data = sock.recv(BUFSIZE)
        if 'quit' in data.decode():
            if sock in clients:
                print(addr, 'exited')
                clients.remove(sock)
                continue
        if sock not in clients:
            print('new client', addr)
            clients.append(sock)
        print(time.asctime() + str(addr) + ':' + data.decode())
        for client in clients:
            if client != sock:
                client.send(data)
    sock.close()

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', port))
s.listen(5)
print('Server Started')

while True:
    conn, addr = s.accept()
    print('connected by', addr)
    th = threading.Thread(target=echoTask, args=(conn, addr))
    th.start()
