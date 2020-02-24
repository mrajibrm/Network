import socket
import threading


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientSocket):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        print("New Connction added:{}".format(clientAddress))

    def run(self):
        print("Connection from: {}".format(clientAddress))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg == 'bye':
                break
            print("\n<From Client>:{}".format(msg))
            self.csocket.send(bytes(msg, 'UTF-8'))
        print("Client @ {}  disconnected")


host = str(input("Enter Host IP"))
port = int(input("Enter port Number"))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
print("\nServer Started....")
print("\nWaiting for Connection....")
while True:
    server.listen(2)
    clientsock, clientAddress = server.accept()
    new_thread = ClientThread(clientAddress, clientsock)
    new_thread.start()
