import socket 					#imports socket library
import threading				#for multiclient based application multi threads are required

s = socket.socket()         	#Creating an object of the socket class 
port = 12345 					#Port that the socket will bind to
s.bind(('', port))        		#Socket is bound to the port
s.listen(5)						#Can accept upto 5 connections
client_list = []				#will keep a record of all the systems connected to the machine

def new_thread(c):				#Function to be used in Multithreading for many clients
	global client_list
	#print(client_list)
	while True:					#loop through the same client, maintain connection for chat app
		val = c.recv(1024)
		for i in client_list:
			i.send(val)
		print(val)

while True:						#accepting multiple clients on this using this loop
	c, addr = s.accept()     	#This will stop execution unless there is a connection request
	print('accepted',addr)
	c.send('Thank you for connecting'.encode('utf-8'))
	global client_list
	client_list.append(c)
	t1 = threading.Thread(target=new_thread,args=(c,))
	t1.start()
		
   
