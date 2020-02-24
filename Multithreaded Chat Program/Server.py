import socket
import select
import sys
import _thread

# AF_INET is the address domain of the socke; it is used for two host that are connected with internet
# SOCK_STREAM means that the data or messages are read in a continuous flow
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This args defines the type of Socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Check the Sufficient arguements; i.e- IP address, Port number etc.
if (len(sys.argv) != 3):
    print("Check the Following:\n Script, IP Address, Port Number")
    exit()

# It takes thee first arguement as IP address
IP_address = str(sys.argv[1])
# print(IP_address)

# It takees the second arguement as port number
Port = int(sys.argv[2])
print(Port)

# Bind the server with the IP and specified port number of client
server.bind((IP_address, Port))

#!The maximum no of client that can accept server at a time. Here 100 conn @ a time
server.listen(100)
list_of_clients = []

#!Buliding Client thread


def client_thread(c, addr):
    c.send("Welcome to the Chat Room")
    while True:
        try:
            msg = c.recv(2048)
            if msg:
                #!It prints the message with its senders ip in the server terminal
                print("< {} >: {}".format(addr[0], msg))
                #!Broadcst the message
                send_msg = "<" + addr[0] + ">" + msg
                broadcast(send_msg, c)
            else:
                #!It removes the inactive client; i.e. which don't have a connection
                remove(c)
        except:
            continue

#!Defining the broadcast moethod


def broadcast(msg, connection):
    for clients in list_of_clients:
        #!Check that client as availavale or not
        if clients != connection:
            try:
                #!If available then send messages
                clients.send(msg)
            except:
                #!Check for brocken connection among clients if found remove it
                clients.close()
                remove(clients)

#!Removes the user which connection is brocken


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
        while True:
            #!Make the connection with the client by accepting connection requeest from the user and store two parameter 'c' is the socket object and address is the IP address of the client or user
            c, addr = server.accept()

            #! After client connected update the list of connected user
            list_of_clients.append(c)

            #!Print the address of the user who jusr got connected
            print("{} got connected".format(addr[0]))

            #!Create individual thread for every single user
            _thread.start_new_thread(client_thread, (c, addr))

            c.close()


server.close()
