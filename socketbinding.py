import socket
import sys
#Following http://www.binarytides.com/python-socket-programming-tutorial/
HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
 s.bind((HOST, PORT))
except socket.error , msg:
 print 'BIND FAILED. ERROR CODE : ' + str(msg[0]) + 'Message ' + msg[1]
 sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

#now keep talking with the client
while 1:
 conn, addr = s.accept()
 print 'Connected with ' + addr[0] + ':' + str(addr[1])
 
 data = conn.recv(1024)
 reply = 'OK...' + data
 if not data:
  break
 
 conn.sendall(reply)

 conn.close()
s.close()
