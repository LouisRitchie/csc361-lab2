import random
import time
import sys
from socket import *

# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
clientSocket.bind(('', 5001))
clientSocket.settimeout(1)

for i in range(10):
        message = "ping" + " " + str(i + 1) + " " + str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec)
	clientSocket.sendto(message, ('', 5000))
        startTime = time.clock()
        try:
            response, address = clientSocket.recvfrom(1024)
            responseTime = (time.clock() - startTime) * 1000
            print response
            sys.stdout.write("Total Time (seconds): ")
            print responseTime
        except:
            print "Request timed out"
