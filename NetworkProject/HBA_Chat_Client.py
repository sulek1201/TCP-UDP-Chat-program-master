#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import *
from threading import Thread
import tkinter
import sys
import time
import json
###################################################################################################################################
sock = socket(AF_INET, SOCK_DGRAM)
server_address = ('', 5000) #Address for announcer
sock.bind(server_address)
thislist = []               #Python Dict. for JSON datas.
timeout = time.time() + 30  #Setting the time for breaking the while loop after amount of time.
i = 0                       #Data Index Counter for List.
try:
        while True:
                #Checks the time that set above and if it's passed, just breaks the loop and stops receiving host infos.
                if time.time() > timeout:
                    break
                #Waits until a data package comes and receives data and address.
                data, address = sock.recvfrom(4096)
                #If coming data is from same pc, than just continue to loop.
                if address[0] != gethostbyname(gethostname()):
                        #Got the JSON info data.
                        data = str(data.decode('UTF-8'))
                        print('Received ' + str(len(data)) + ' bytes from ' + str(address) )
                        #Getting count for data members in the list.
                        rng = len(thislist)
                        #If list is not empty, than..
                        if len(thislist) != 0:
                                #Got first data member to the list before checking if it's duplicate or not.
                                thislist.append(data)
                                #Going through the list for duplicate check, but not counting the last added member.
                                for k in range(rng):
                                        #If there is a duplicate member of last added member, than just pop the list and break.
                                        if data == thislist[k]: #If there is no duplicate, we just added the member above the loop.
                                                thislist.pop()
                                                break
                        else: #If list is empty, just add the first data member to the list.
                                thislist.append(data)
                        #This code controls the count of list members before the adding procedure.
                        #If there is a change on count, just print the index and add one for the other coming data members.
                        if rng != len(thislist):
                                print('Data Index: ', i)
                                i += 1
                        else: #If there is no change, it seems this data member is duplicate, just continue to loop.
                                continue
                        print('Data:' + data)
                        
finally:
        print('closing socket')
        #This socket's job is done. Just close it.
        sock.close()

###################################################################################################################################




def receive():
    """Handles receiving of messages."""
    #Receives messages from target host and us, than inserts it to tkinter interface.
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            #Adds receiving time of a message to the head of chat message.
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            msg_list.insert(tkinter.END, current_time+ " - "+msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    #Got our typed message.
    msg = my_msg.get()
    # Clears input field.
    my_msg.set("")
    #Sends the message to the target host.
    client_socket.send(bytes(msg, "utf8"))
    #Sends the message to the our tkinter interface.
    client_socket1.send(bytes(msg, "utf8"))
    #If user types "{quit}" , than socket will be close and chat will be stopped for this user.
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    #Automatically, quits from chat when closing the ChatClient.
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
# For the messages to be sent.
my_msg = tkinter.StringVar()
my_msg.set("Type your messages here.")
# To navigate through past messages.
scrollbar = tkinter.Scrollbar(messages_frame)
# Following code will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
if len(thislist) != 0:
        #If the list has hosts, then just type it's index number
        #and json code will parse the list for to be usable with ip_address index.
        INDEX = input("Enter a index: ")
        y = json.loads(thislist[int(INDEX)])
        HOST = y["ip_address"]
else:   #If there is no host on the list, then we can type hostname by ourselves.
        HOST = input("Enter a host: ")
PORT = 5000
if not PORT:
    PORT = 5000
else:
    PORT = int(PORT)

BUFSIZ = 4096
#Address for target host.
ADDR = (HOST, PORT)
#Address for sending our messsages to our tkinter interface.
ADDR1 = (gethostbyname(gethostname()),PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
client_socket1 = socket(AF_INET, SOCK_STREAM)
client_socket1.connect(ADDR1)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.
