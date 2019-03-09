#!/usr/bin/env python3

import socket
host = '192.168.43.87'
tcpPort = 65432
udpPort = 65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, tcpPort))
    s.sendall(('12345678|133|123').encode())
    data = s.recv(1024)

print('Received', repr(data))



client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(1,1001):
    message = ("12345678|"+str(i)+"|hola").encode()
    print(message)
    addr = (host, udpPort )
    client_socket.sendto(message, addr)