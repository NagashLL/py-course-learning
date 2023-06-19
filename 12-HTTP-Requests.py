import socket
#here we import the socket library
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        #here we make a socket that talks to the internet, and make a socket that transmits a string of letters instead of a block of text
mysock.connect( ('data.pr4e.org', 80))
        #we connect to a host ^,   ^at this port

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#                                                              ^ here we encode the GET command from a UTF-8 string into bytes so that we can send it over the network
#here we write the GET request that we will be sending to the host via the socket
   
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
    #           ^ and here we decode the bytes into strings
mysock.close