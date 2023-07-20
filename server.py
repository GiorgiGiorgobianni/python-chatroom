import sys
import socket
import threading
import time

disconnect_msg = "!DISCONNECT"
sock = socket.socket()
host = socket.gethostname()
server_ip = socket.gethostbyname(host)
format = 'UTF-8'
port = 1234
address = (server_ip, port)
name = "host"

sock.bind(address)

print(f"YOUR IP ADDRESS IS: {server_ip}")


sock.listen(1)
conn, add = sock.accept()

print(f"CONNECTING TO {add[0]}")
print(f"SUCCESSFULLY CONNECTED TO {add[0]}")
client_connected = True


client = (conn.recv(1024)).decode(format)
print(f"{client} HAS CONNECTED")
conn.send(name.encode(format))


def message_send():
    while client_connected:
        sending_message = input("Me:")
        conn.send(sending_message.encode(format))
        sending_message = conn.recv(1024)
        


def receive_msg():
    message = conn.recv(1024)
    message = message.decode(format)
    print(f"USER: {message}")
while client_connected:
    message_send()

def multiTask():
    thread = threading.thread(target = message_send())


