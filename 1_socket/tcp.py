
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