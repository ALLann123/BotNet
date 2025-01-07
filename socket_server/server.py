#!/usr/bin/python3

import socketserver

class MYTCPHandler(socketserver.BaseRequestHandler):
	#request handler for our class, used to instanciate once per connection to the server
	#must override the handle method to implement communication to client
	def handle(self):
		#self.request is the TCP server connected to the client
		print("Got Connection from {}".format(self.client_address[0]))
		print("[+]Message Below")
		gameover=True
		while gameover:
			self.data = self.request.recv(1024).strip()
			if not self.data:
				print("Closing connection with {}".format(self.client_address[0]))
				print("-------------------------------------")
				break
			else:
				print("Received from {}:".format(self.client_address[0]))
				print(self.data)
				#send back the same data but uppercase
				self.request.sendall(self.data.upper())


if __name__=="__main__":

	print("[+]Welcome")
	print("-----------------------")
	HOST, PORT = "localhost", 9999

	#create a binding to local host on port 9999
	with socketserver.TCPServer((HOST,PORT), MYTCPHandler) as server:
		#activate the server
		#server will keep runing until you hit ctrl+c
		server.serve_forever()
