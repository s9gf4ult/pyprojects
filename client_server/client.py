
import socket

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = 'localhost'
port = 30033

serversocket.connect((host,port))

while True:
    buf = raw_input(">> ")
    serversocket.send(buf)
    result = serversocket.recv(1024)
    print result

    if buf == "exit":
        break

serversocket.close()
