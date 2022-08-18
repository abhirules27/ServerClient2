import socket
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP_SERVER = '192.168.0.194'
IP_SERVER = '5.180.61.49'
s.connect((IP_SERVER, 1234))
while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"New msg length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg.decode('utf-8')
        if len(full_msg) - HEADERSIZE == msglen:
            print("Full Message Received")
            print(full_msg[HEADERSIZE:])
            new_msg = True
    print(full_msg)