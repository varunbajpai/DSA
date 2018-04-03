import time
import socket 
import threading

s = socket.socket()         
port = 12345 
s.bind(('', port))        
s.listen(5)

def new_thread(c):
	while True:
		val = c.recv(1024)
		c.send(val)
		print(val)

while True:
	c, addr = s.accept()     
	print('accepted',addr)
	c.send('Thank you for connecting'.encode('utf-8'))
	t1 = threading.Thread(target=new_thread,args=(c,))
	t1.start()
		
   
