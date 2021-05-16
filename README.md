# TCP-UDP-Chat-program
~First of all, to start all components of TCP/UDP
chat program, you need to open "startChat.bat" file.

~It will open files automatically.

~Then, three command windows will pop up.

~One which has "Waiting for connection..." printed in the screen is 
your "Chat_Listener", which is important for gathering data from 
bounded address and send it to your client for your chat connectivity.

~Other one which has "Enter a name: " printed in the screen is your
"Service_Advertiser", which sends your JSON String that contains
your name and IP address to the other Listeners in the network.
So you should type your name in order to introduce yourself.

~Last one which has nothing printed in the screen until it gets
some JSON data from other Advertisers is your "Chat_Client".
It's main file for Chatting, because it's doing many things together
like listening for online users, adding them into python dictionary
and chatting with a chat interface that contains all of messages 
that sent or received. 

~So, our program will wait 30 seconds for listening online people 
on the network and add them into the dictionary. After 30 seconds,
you should type a index number for which person you want to chat with.

~(P.1) After that, a chat interface will pop up and you will
type your chat username. After pressed "Enter", if other person
is connected to you properly, than you can chat with him/her freely.
If you want to quit from chat, just type "{quit}" and press "Enter" or
if you close the chat window, this will be done automatically.

!!IMPORTANT!!
~Before typing index number, when you can't find that person 
you want chat with after 30 seconds, than you can open 
"Service_Listener" for checking online persons. If he/she is online, 
just close "Chat_Client" window and reopen it for new scan.

~After 30 seconds from opening "Chat_Client", If no one is online,
than you can type that person's IP address on your own or just
close the "Chat_Client" windows and reopen it.

~After reopening, you can follow (P.1) part for rest of them.

