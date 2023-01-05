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


#Send/Recieve messages

while True:
    #Recieve information 
    message = client_socket.recv(btyesize).decode(Encoder)
    
    #QUIT if the connected server wants to quit, else keep sending message


    if message == "quit":
       client_socket.send("quit".encode(Encoder))
       print("\nEnding the chat ... goodbye!")
       break
    else:
        print(f"/n{message}")
        message = input("Message:")
        client_socket.send(message.encode(Encoder))




#Close the client socket

client_socket.close()
