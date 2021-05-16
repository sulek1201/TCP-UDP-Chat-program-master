from socket import * 
import sys
import json

sock = socket(AF_INET, SOCK_DGRAM)

server_address = ('', 5000)

sock.bind(server_address)

while True:
        data, address = sock.recvfrom(4096)
        if address[0] != gethostbyname(gethostname()):
                data = str(data.decode('UTF-8'))
                print('Data:' + data)
