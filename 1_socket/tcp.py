
#TCP Server file

import socket


#create a servide socketIPV4(AF_INET) and TCP(SOCK_STREAM)

server_socket =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)



# see how to get IP ADDRESS dynamically

print(socket.gethostname()) # host name
print(socket.gethostbyname(socket.gethostname())) #ip of the given hostname



#Bind our new socket to a tuple (IP Address, Port Address)


server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))


#put the socket inot listening mode for any possible connections


server_socket.listen()


#listening forver to accept any connection


while True:
    # Accept every single connect store piece of information
    client_socket, client_addresss = server_socket.accept()
    # print(type(client_socket))
    # print(client_socket)
    print(type(client_addresss))
    print(client_addresss)

    print(f"Connected to {client_addresss} !\n")
    #send a message to the client
    client_socket.send("you are connected".encode("utf-8"))


    #close the connection
    server_socket.close()

    break