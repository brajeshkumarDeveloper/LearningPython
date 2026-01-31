import socket

s= socket.socket()
print('Socket successfully created')

s.bind(('localhost', 9999))

s.listen(3)
print('Waiting for connection')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('Got connection from', addr, 'name:', name)


    c.send(bytes('Thank you for connecting', 'utf-8'))
    c.close()