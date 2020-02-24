import socket
server = str(input("Enter Server IP:"))
port = int(input("Enter Server port"))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server, port))
client.sendall(bytes("From client", 'UTF-8'))
while True:
    in_data = client.recv(1024)
    print("<Server> : {}".format(in_data.decode()))
    out_data = input()
    client.sendall(bytes(out_data, 'UTF-8'))
    if out_data == 'bye':
        break
client.close()
