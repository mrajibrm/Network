#Import the socket library
import socket
#Create Socket Object
s = socket.socket()
print("Socket Successfulyy Creatd")
#Reserve the port address for Other Computer Connction
port = 12345
#Bind the port address with the incoming ip connection from other computer
s.bind(('', port))
#Listen for incoming connection
s.listen(5)
print("Socket is Listening for Incoming Connection")

while True:
    #Establish connection with Client
    c,addr = s.accept()
    print("Incoming Connection from{} ".format(addr))
    #Send a Acknowledgement to CLient for Successful Connection
    msg = 'Thank You For Connecting' + "\r\n"
    c.send(msg.encode('ascii'))
    #Close the connection with Client
    c.close()