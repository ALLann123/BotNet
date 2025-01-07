#!/usr/bin/python3
import socket
import sys

HOST=input("Enter the server IP>> ")
PORT=9999

#create a socket
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
	#connect to the server and send message
	sock.connect((HOST, PORT))
	gameover=True
	print("******[+]Start CHAT******")
	while gameover:
		#send data
		data=input("Enter Message(own_the_net): ")
		if data!="exit":
			sock.sendall(bytes(data + "\n", "utf-8"))
			#receive data from the server
			received=str(sock.recv(1024), "utf-8")
			print("Received: {}".format(received))
			print("------------------------------")
		else:
			gameover=False
			print("GoodBye!!")
			sys.exit()

