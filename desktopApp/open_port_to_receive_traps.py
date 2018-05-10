import socket

puerto = 162

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((socket.gethostbyname(socket.gethostname()),puerto))

while True:
	recivido,(addr,port) = sock.recvfrom(2048)
	print "received" + data + "from" + addr