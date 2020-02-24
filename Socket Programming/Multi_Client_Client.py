import socket
import sys


def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #!host = "#!Muy IP"
    host = str(input("Enter Server IP:"))
    port = int(input("Enter Server Port:"))
    try:
        soc.connect(host, port)

    except:
        print("Connection Error")
        sys.exit()
    print("Please Enter QUIT to Exit")
    message = input("->")
    while message != 'QUIT':
        soc.sendall(message.encode("utf8"))
        if soc.recv(1024).decode("utf8") == "-":
            pass
        message = input("->")
        soc.send(b'--QUIT--')


if __name__ == "main":
    main()
