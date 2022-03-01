import socket

serverName = 'ubuntu2004-002.student.cs.uwaterloo.ca'
serverPort = 12000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

sentence = raw_input('Input lowercase sentence:')

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)

print(modifiedSentence.decode())
clientSocket.close()
