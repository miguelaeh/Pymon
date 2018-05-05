import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((socket.gethostbyname(socket.gethostname()),162))

while True:
	recivido,(addr,port) = sock.recvfrom(2048)
	print "received" + data + "from" + addr