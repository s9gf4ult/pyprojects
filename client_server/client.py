
import socket

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 30033

serversocket.connect((host,port))

print serversocket.recv(1024)
serversocket.close
