import sys
import socket

disconnect_msg = "!DISCONNECT"
socketServer = socket.socket()
hostServer = socket.gethostname()
ip = socket.gethostbyname(hostServer)
format = 'UTF-8'
PORT = 1234
hostServer = input("HOST'S IP ADDRESS: ")
addr = (hostServer, PORT)
name = "user"

print(f"YOUR IP ADDRESS IS: {ip}")



socketServer.connect(addr)

socketServer.send(name.encode(format))
serverName = socketServer.recv(1024)
serverName = serverName.decode(format)

print(f"SUCCESSFULLY CONNECTED TO {serverName}")
connectedToServer = True

def message_send():
    while connectedToServer:
        sending_message = input("Me:")
        socketServer.send(sending_message.encode(format))
        sending_message = socketServer.recv(1024)
        if sending_message == disconnect_msg:
            sys.exit()


def receive_msg():
    while connectedToServer:
        message = socketServer.recv(1024)
        message = message.decode(format)
        print(f"USER: {message}")
while connectedToServer:
    receive_msg()