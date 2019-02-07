import datetime
import socket


def main():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverIP = input("Enter server hostname or IP: ")
    serverPort = int(input("Enter server port: "))
    clientSocket.connect((serverIP, serverPort))  # connect to the server
    message = input("Enter your message: ")
    clientSocket.send(message.encode())  # Send message to the server
    print("<-- Message sent to server {} : {} on {}".format(serverIP, serverPort,
                                                            datetime.datetime.now()))
    messageCount = clientSocket.recv(1024).decode()  # Receive characters count from the server
    print("--> Message received from server {} : {} on {}".format(serverIP, serverPort,
                                                                  datetime.datetime.now()))
    print("-----------------------------------------------")
    print("The count of characters in your message is: {}".format(messageCount))
    print("-----------------------------------------------\n")
    clientSocket.close()


if __name__ == '__main__': main()
