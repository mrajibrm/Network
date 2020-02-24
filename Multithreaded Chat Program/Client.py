import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Check the Following:\n Script, IP Address, Port Number")
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

while True:

    # Maintain the possibl input stream
    socket_list = [sys.stdin, server]

    # /*There are two possible input situations. Either the
    # user wants to give  manual input to send to other people,
    # or the server is sending a message  to be printed on the
    # screen. Select returns from sockets_list, the stream that
    # is reader for input. So for example, if the server wants
    # to send a message, then the if condition will hold true
    # below.If the user wants to send a message, the else
    # condition will evaluate as true*/
    read_socket, write_socket, error_socket = select.select(
        socket_list, [], [])
    for socks in read_socket:
        if socks == server:
            message = socks.recv(2048)
            print(message)
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
