#! /usr/bin/env python3
# findIPAddress.py finds and prints IP addresses in a string

import re

def isIPAddress(ipAddr):
	# Checks if the tuple ipAddr is valid IP address
	firstOct, secondOct, thirdOct, fourthOct = ipAddr
	if (int(firstOct) > 0) and (int(firstOct) < 255):
		if int(secondOct) <= 255:
			if int(thirdOct) <= 255:
				if (int(fourthOct) > 0) and (int(fourthOct) < 255):
					return True


message = 'The workstation has IP address 192.255.4.19'

ipAddrRegex = re.compile(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')
mo = ipAddrRegex.search(message)

if isIPAddress(mo.groups()):
	print (mo.group(1) + '.' + mo.group(2) + '.' + mo.group(3) + '.' + mo.group(4))
else:
	print ('There is no valid IP address in the message')