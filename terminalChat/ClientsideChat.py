import socket,threading


#Define constants to be used

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024


#CREATE a client socket


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((DEST_IP,DEST_PORT))



def sendMessage():
    '''send a message to the server to be broadcast'''
    pass


def recieve_Message():
    '''Recieving incoming message from the server'''
    while True:
        try:
            #recieve an incoming message
            message = client_socket.recv(BYTESIZE).decode(ENCODER)

            #check for the name flag, else show the message
            if message == "NAME":
                name = input("What is your name: ")
                client_socket.send(name.encode(ENCODER))

            else:
                print(message)

        except:
            # An error occured,close the connection
            print("An error occured")
            client_socket.close()
            break




        #call the client and start
recieve_Message()