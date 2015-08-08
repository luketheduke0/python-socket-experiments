import socket
import sys

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

#wait to accept a connection - blocking call
conn, addr = s.accept()

print 'Connected with ' + addr[0] + ':' + str(addr[1])
