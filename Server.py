import datetime
import socket


def main():
    serverPort = 12000
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Arguments represent the address and protocol
    serverSocket.bind(('127.0.0.1', serverPort))  # Bind the socket to address
    serverSocket.listen(10)  # Number of accepted connections
    print('The server is listening on localhost : ', serverPort)
    while 1:
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(1024).decode()  # Receive message from client
        print("--> Message received from client {} : {} on {}".format(addr[0], addr[1],
                                                                      datetime.datetime.now()))
        messageCount = str(len(message) - message.count(' '))  # Store characters count ignoring spaces
        connectionSocket.send(messageCount.encode())  # Send characters count to client
        print("<-- Message sent to client {} : {} on {}".format(addr[0], addr[1],
                                                                datetime.datetime.now()))
        connectionSocket.close()


if __name__ == '__main__': main()
