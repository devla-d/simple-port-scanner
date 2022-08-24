#!/bin/python3

import sys #allows us to enter command line agurment and other things
import socket
import re
from datetime import datetime


 

#Define our target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate a host name to IPV4
else:
	print("Invalid Amount Of Arguments")
	print("SYNTAX :  python3 scanner.py <ip>")
	sys.exit()
	
	
print("-" * 50)
print(f"Scanning target {target}")
print("Time started :" + str(datetime.now()))
print("-" * 50)




try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))#return error indicator
		print(f"Checking port {port}")
		if result == 0:
			print(f"Port {port} is open")
		s.close()
except KeyboardInterrupt:
	print("\nExisting program.")
	sys.exit()
except socket.gaierror:
	print("Host Could Not Be Resolved.")
	sys.exit()
except socket.error:
	print("Couldn't connet to server.")
	sys.exit()
	
	
	
	

