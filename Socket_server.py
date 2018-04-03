import time
import socket 

s = socket.socket()         
port = 12345 
s.bind(('', port))        
s.listen(5)     

c, addr = s.accept()     
print('accepted',addr)
c.send('Thank you for connecting'.encode('utf-8'))

while True:
	val = c.recv(1024)
	c.send(val)
	print(val)

		
c.close()
   
