import socket,threading 


#define constants to be used

print('HELLO')



HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER ='utf-8'
BYTESIZE = 1024


#create a server socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST_IP,HOST_PORT))
server_socket.listen()

#CREATE two blank lists to store connected clients sockaets and there names

client_socket_list = []
client_name_list = []


def broadcast_message(message):
    ''' Send a message to all clients connected to the server'''
    pass


def recieve_message(client_socket):
  """ Recieve an incoming message from a specific cleint and forward the message to be broadcast"""
  pass



def connect_client():
 '''Connect an incoming client'''
 while True:
      #Accept any incoming client connection
      client_socket,client_address = server_socket.accept()
      print(f"""connected with {client_address}....""")

      #send a name flag to p=rompt the client for their name
      client_socket.send("NAME".encode(ENCODER))
      client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

      #Add new client socket and client to appropriate lists
      client_socket_list.append(client_socket)
      client_name_list.append(client_name)


      #updadte the server, indiduval client, and all clients
      print(f"Name of new client is {client_name}\n")
      client_socket.send(f"{client_name},you have connected to the server".encode(ENCODER))
      broadcast_message(f"{client_name} has joined the chat".encode(ENCODER))




      #Start the server

      
print("Server is listening for incoming connections... \n")
connect_client()