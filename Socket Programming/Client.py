import socket
s = socket.socket()
port = 12345
s.connect(('10.58.10.114',port))
msg = s.recv(1024)
print(msg.decode('ascii'))
s.close()