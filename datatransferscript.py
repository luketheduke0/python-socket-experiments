#Following http://www.binarytides.com/python-socket-programming-tutorial/
import socket
import sys

try:
 #create TCP socket
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
 print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
 sys.exit();
 
print 'Socket Created'

host = 'www.google.com'

try:
 remote_ip = socket.gethostbyname( host )
except socket.gaierror:
 #could not resolve
 print 'Hostname could not be resolved. Exiting.'
 sys.exit()

print 'IP address of ' + host + ' is ' + remote_ip
