# Surprior, 2017

import socket, sys

HOST = ''
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print("Connection from: " + str(addr))
while 1:
	data = conn.recv(100).decode()
	if data:
		print(data)
s.close()