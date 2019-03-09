import socket

(HOST,PORT)=('localhost',19123)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((HOST,PORT))

with open('audio.wav', 'rb') as f:
  for l in f: s.sendall(l)
s.close()
