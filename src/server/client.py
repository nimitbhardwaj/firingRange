#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 65432      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))



client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = b'test'
addr = ("127.0.0.1", PORT+1)

client_socket.sendto(message, addr)
data, server = client_socket.recvfrom(1024)
print(data)