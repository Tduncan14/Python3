#TCP client side

import socket


#create a client side IPV4 socket(AF_INET) and TCP (Socket_Stream)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#CONNECT THE socket to a server located at a given IP and PORT

client_socket.connect((socket.gethostbyname(socket.gethostname()),12345)) 


#recieve a message from the server... You must specify the max number of bytes to recieve

message = client_socket.recv(1024)
print(message.decode('utf-8'))


#close the client socket

client_socket.close()