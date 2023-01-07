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
    for client_socket in client_socket_list:
        client_socket.send(message)


def recieve_message(client_socket):
  """ Recieve an incoming message from a specific cleint and forward the message to be broadcast"""
  while True:
       try:
           #Get the name of the given cleint
           index = client_socket_list.index(client_socket)
           name = client_name_list[index]

           #Recieve message from the client
           message = client_socket.recv(BYTESIZE).decode(ENCODER)
           message = f"{name}: {message}".encode(ENCODER)
           broadcast_message(message)
       except:
          # find the index of the client socket in our list
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

         #remove the client socket and name from lists
            client_socket_list.remove(client_socket)
            client_name_list.remove(name)


            #close the clieint socket
            client_socket.close()

            #Broad cast the client has left the chat
            broadcast_message(f"{name} has left the chat".encode(ENCODER))
            break


         



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

      #Now that a client has connected, start a thread
      recieve_thread = threading.Thread(target=recieve_message, args=(client_socket,))
      recieve_thread.start()






      #Start the server

      
print("Server is listening for incoming connections... \n")
connect_client()