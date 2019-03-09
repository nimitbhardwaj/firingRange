#!/usr/bin/env python3
import socket
host = '192.168.43.87'
tcpPort = 65432
udpPort = 65433

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((host, tcpPort))
#     s.sendall(('12345678|133|123').encode())
#     data = s.recv(1024)

# print('Received', repr(data))



# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# for i in range(1,1001):
#     message = ("12345678|"+str(i)+"|hola").encode()
#     print(message)
#     addr = (host, udpPort )
#     client_socket.sendto(message, addr)

from scipy.io import wavfile
fs, data = wavfile.read('./audio.wav')
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = (host, udpPort)
data = data.tobytes()
import sys
fileSize = sys.getsizeof(data)

index, pointer, flag = 0, 0, 0
while True:
    if pointer >= fileSize:
        pointer = fileSize - 1
        flag = 1
    # message = "12345678|"+str(index)+"|"
    message = ("12345678", index)
    size = sys.getsizeof(message)
    remSize = 1024 - size
    sendData = data[pointer:pointer+remSize]
    message = ("12345678", index, sendData)
    client_socket.sendto(message, addr)
    index = index + 1
    pointer = pointer + remSize
    if flag == 1:
        break
