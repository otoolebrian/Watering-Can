import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 12345
s.bind((host, port))

s.listen(5)
while True:
	c, addr = s.accept()
	print ('Connection from ', addr)
	reply =  c.recv(4096)
	print reply
	c.close()

	
