import socket
import sys
import traceback
from threading import Thread
import time


def main():
    start_server()


def start_server():
    #!host = "#!MY IP Adrres"
    host = socket.gethostname()
    ip = socket.gethostbyname()
    port = int(input("Enter Port:"))
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket Created")
    try:
        soc.bind((ip, port))

    except:
        print("Bind Failed. \n Error:" + str(sys.exc_info()))
        sys.exit()

    #!Maximum Queue upto 6 Request
    soc.listen(6)
    print("Socket is Now Listening for Connection")
    time.sleep(1)
    #!Infinite lop - do not reset for every request
    while True:
        connection, address = soc.accept()
        ip, port = str(address[0], str(address[1]))
        print("Connected with {} : {}".format(ip, port))
        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()

        except:
            print("Thread Didn't Started.")
            traceback.print_exc()

        soc.close()


def client_thread(connection, ip, port, max_buffer_size=1024):
    is_active = True
    while is_active:
        client_input = receive_input(connection, max_buffer_size)
        if "--QUIT--" in client_input:
            print("Client is Requsting for Quit")
            connection.close()
            print("Connection {} : {} Closed".format(ip, port))
            is_active = False

    else:
        print("<{}>: {}".format(ip, client_input))
        connection.sendall("-".encode("utf8"))
    return client_input


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)
    if client_input_size > max_buffer_size:
        print("Message is Too Large to Read. Try to update the Server script {}".format(
            client_input_size))
        decoded_input = client_input.decode("utf8").rstrip()
        result = process_input(decoded_input)
        return result


def process_input(input_str, ip):
    print("<{}>: {}".format(ip, input_str))


if __name__ == "main":
    main()
