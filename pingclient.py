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

while True:
	clientSocket.sendto("ping", ('', 5000))
        startTime = time.clock()
        try:
            message, address = clientSocket.recvfrom(1024)
            responseTime = (time.clock() - startTime) * 1000
            print message
            sys.stdout.write("Total Time (seconds): ")
            print responseTime
        except:
            print "Request timed out"

        time.sleep(1)
