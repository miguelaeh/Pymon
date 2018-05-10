import socket

puerto = 162
HOST= socket.gethostbyname(socket.gethostname())

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((HOST,puerto))

while True:
	recivido,(addr,port) = socket.recvfrom(2048)
	print "received" + data + "from" + addr