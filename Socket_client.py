import socket               
s = socket.socket()         
port = 12345

s.connect(('127.0.0.1', port))
print(s.recv(1024))

while True:
	a = input('Enter Message>>')
	s.send(a.encode())
	print(s.recv(1024))
s.close() 