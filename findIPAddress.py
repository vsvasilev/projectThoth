#! /usr/bin/env python3
# findIPAddress.py finds and prints IP addresses in a string

import re

def isIPv4Address(ipAddr):
	# Checks if the string ipAddr is valid IP address
	firstOct, secondOct, thirdOct, fourthOct = tuple(ipAddr.split('.'))
	if (int(firstOct) > 0) and (int(firstOct) < 255):
		if int(secondOct) <= 255:
			if int(thirdOct) <= 255:
				if (int(fourthOct) > 0) and (int(fourthOct) < 255):
					return True
	else:
		return False


message = '1.1.1.1 is IPv4 address and 2001:0db8:0000:0000:0000:ff00:0042:8329 is IPv6 address.\
         short 2001:db8:0:0:0:ff00:42:8329 shorter 2001:db8::ff00:42:8329\
         \nThe workstation has IP address 192.255.4.19 and the server 10.255.1.7'

ipv4AddrRegex = re.compile(r'''
	(^\d{1,3}|\s\d{1,3})\. 					# First octed
	(\d{1,3})\. 							# Second octet
	(\d{1,3})\. 							# Third octet
	(\d{1,3}\s?)							# Fourth octet
	''', re.X | re.M)

ipv6AddrRegex = re.compile(r'''
	(^[0-9a-f]{,4}|\s[0-9a-f]{,4})::?		# First 16 bit group
	([0-9a-f]{,4})::?						# Second 16 bit group
	([0-9a-f]{,4})::?						# Third 16 bit group
	([0-9a-f]{,4})::?						# Fourth 16 bit group
	([0-9a-f]{,4})::?						# Fifth 16 bit group
	([0-9a-f]{,4})::?						# Sixth 16 bit group
	([0-9a-f]{,4})::?						# Seventh 16 bit group
	([0-9a-f]{,4})							# Eigth 16 bit group	
	''', re.X | re.M)

ipv4Addresses = []
ipv6Addresses = []

for groups in ipv4AddrRegex.findall(message):
	ipv4Addresses.append('.'.join([groups[0].strip() , groups[1] , groups [2] , groups[3]]))

if len(ipv4Addresses) > 0:
	print('IPv4 Addresses:\n--------------------')
	for i in range(len(ipv4Addresses)):
		if isIPv4Address(ipv4Addresses[i]):
			print(ipv4Addresses[i])
else:
 	print('No IPv4 Addresses found.')

for groups in ipv6AddrRegex.findall(message):
	ipv6Addresses.append((':'.join(groups).strip()))

if len(ipv6Addresses) > 0:
	print('\nIPv6 Addresses:\n--------------------')
	for j in range(len(ipv6Addresses)):
		print(ipv6Addresses[j])
else:
	print('No IPv6 Addresses found.')

