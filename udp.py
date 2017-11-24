import socket, errno, time
from string import *

UDP_IP = "127.0.0.1"
UDP_PORT = 5555

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(0)
def get():
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                return "connection closed"
                sock.close()
                break
            else:
                #print "Received %d bytes: '%s'" % (len(data), data)
                if "coreasar" in data:
                    junk,data2=split(data,'coreasar')
                    return 'artist='+data2

                if "coreasal" in data:
                    junk,data2=split(data,'coreasal')
                    return 'album='+data2

                if "coreminm" in data:
                    junk,data2=split(data,'coreminm')
                    return 'song='+data2

                
                #return data
        except socket.error, e:
            if e.args[0] == errno.EWOULDBLOCK: 
                
                time.sleep(.1)           # short delay, no tight loops
                return 'EWOULDBLOCK'
            else:
                print e
                break

def close():
    sock.close()
