#UDP Client side
import socket

#Create a UDP IPDV4 socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send information connections less

client_socket.sendto("Hello server world".encode("utf-8"),(socket.gethostbyname(socket.gethostname()),12345))