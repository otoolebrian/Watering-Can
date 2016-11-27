import socket

#Define the different cases that this listener will respond to
#The listener responds to commands in the format {command arg 1, arg 2, ... arg n}

def network_command(recvString):
	#get the command, it should be the first word
	recvComm = recvString.split()
	
	#Check which command was recieved, if not recognised return an error
	if(recvComm[0].lower() == "adddevice"):
		returnVal = 'OK'	
	elif(recvComm[0].lower() == "rectemp"):

		returnVal = 'OK'	
	elif(recvComm[0].lower() == "recsoil"):

		returnVal = 'OK'	
	else:
		returnVal = 'commands are addevice, rectemp, recsoil'
	
	return returnVal

	
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
	c.send(network_command(reply) + '\n')
	c.close()

	
