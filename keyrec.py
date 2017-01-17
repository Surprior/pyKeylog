import socket, sys

HOST = ''
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, _ = s.accept()
while 1:
	data = conn.recv(100).decode()
	if data:
		print(data)
		#if data[0] == "'" and data[-1] == "'":
		#	print data.lstrip("'").rstrip("'")
		#elif data[0] == '"' and data[-1] == '"':
		#	print data.lstrip('"').rstrip('"')
s.close()