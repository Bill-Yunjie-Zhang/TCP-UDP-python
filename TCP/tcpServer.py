import socket

serverPort = 12000

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSock.bind(("", serverPort))

serverSock.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSock.accept()

    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())

    connectionSocket.close()
    