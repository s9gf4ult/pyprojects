import socket


# define host and port
host = "localhost"
port = 30033


# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# bind/link our socket and host
serversocket.bind((host,port))


# close socket
serversocket.close()
