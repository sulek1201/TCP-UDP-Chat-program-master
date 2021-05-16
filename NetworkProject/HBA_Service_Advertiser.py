from socket import *
import sys
import time
import json


sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

server_address = ('255.255.255.255', 5000)
#message = 'pfg_ip_broadcast_cl'


try:
        typeName = input("Enter a name: ")
        # some JSON:
        x =  '{"username": "name", "ip_address": "192.168.x.x"}'
        # parse x:
        y = json.loads(x)
        y["username"]=typeName
        y["ip_address"]=gethostbyname(gethostname())
        # convert into JSON:
        x = json.dumps(y)
        while True:
                # Send data
		#print('sending: ' + message)
                print('Sending...')
                sent = sock.sendto(x.encode(), server_address)
                # Receive response
                #print('waiting to receive')
                #data, server = sock.recvfrom(4096)
                #if server[0] != gethostbyname(gethostname()):
                        #if data.decode('UTF-8') == 'pfg_ip_response_serv':
                                #break
                time.sleep(5)
                
	
finally:
        sock.close()

