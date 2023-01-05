#Chat client side
import socket


#Define const to be used 

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
Encoder = "utf-8"
btyesize=1024

#create a client socet and connect to the server
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))