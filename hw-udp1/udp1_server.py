import socket
port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))
mybox = {}
sendmsg = ''
while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    opt, mboxID, message = msg.decode().split(' ', 2)
    if opt == 'send':
        if mboxID not in mybox:
            mybox[mboxID] = [message]
        else:
            mybox[mboxID].append(message)
        
        sendmsg = "OK"
    
    elif opt == 'receive':
        if mboxID not in mybox:
            sendmsg = "No messages"
        else:
            if mybox[mboxID]:
                sendmsg = mybox[mboxID][0]
                mybox[mboxID].pop(0)
            else:
                sendmsg = "No messages"

    sock.sendto(sendmsg.encode(), addr)