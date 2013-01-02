import socket


# define host and port
host = "localhost"
port = 30033


# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind/link our socket with host port
serversocket.bind((host,port))
serversocket.listen(5)

# waiting connect client
conn, addr = serversocket.accept()
print "Got connection from", addr

while True:

    buf = conn.recv(1024)
    print buf
    if buf == 'exit':
        conn.send("Thanks, bye!")
        break
    elif buf:
        conn.send(buf)

conn.close()
