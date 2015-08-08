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
