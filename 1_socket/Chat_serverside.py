#Chat serverside
import socket

#Define constant to be used

HOST_IP = socket.gethostbyname(socket.gethostname())

HOST_PORT = 12345

ENCORDER ="utf-8"


btyesize = 1024

#Create a server socket, bind it to an ip/port, and listen

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP,HOST_PORT))

server_socket.listen()


#Accept any incoming connection and let them know they are connected

print("Server is running...\n")
client_socket,client_address = server_socket.accept()

client_socket.send("You are connected to the server...\n".encode(ENCORDER))



#send/recieve message

while True:
     #Reciever inormation from the client
     message = client_socket.recv(btyesize).decode(ENCORDER)

     #Quit if the client socket wants to quit, else display the message

     if message == "quit":
        client_socket.send("quit".encode(ENCORDER))
        print("\nEnding the chat ..goodbye!")
        break
     else:
        print(f"\n{message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCORDER))



#Close the socket 

server_socket.close()

