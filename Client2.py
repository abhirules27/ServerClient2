import socket
HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_SERVER = '192.168.0.194'
s.connect((IP_SERVER, 1234))
while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"New msg length: {msg[:HEADERSIZE]}")
        full_msg += msg.decode('utf-8')
    print(full_msg)