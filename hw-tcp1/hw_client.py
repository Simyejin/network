import socket
sock = socket.socket(socket.AF_INET, 
socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)  #연결요청
msg = sock.recv(1024)
print(msg.decode())
name = 'sim ye jin'
sock.send(name.encode())
id = sock.recv(1024)
print(id.decode())
sock.close()