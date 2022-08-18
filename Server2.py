import socket
import time
HEADERSIZE = 10
IP_SERVER = '192.168.0.194'
# IP_SERVER = '5.180.61.49'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP_SERVER, 1334))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} established")
    msg = "Welcome to the Server"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    clientsocket.send(bytes(msg, "utf-8"))
    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        clientsocket.send(bytes(msg, "utf-8"))
