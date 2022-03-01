import socket

serverName = 'ubuntu2004-002.student.cs.uwaterloo.ca'
serverPort = 12000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = raw_input('Input lowercase sentence:')

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())
clientSocket.close()