import os
import subprocess

IP = str(input('Enter IP :- '))
all_ports = open('all_ports','r')
possible_ports = all_ports.read()
lower=9000
higher=14000
while(True):
	port = round(int((lower+higher)/2))
	if str(port) in str(all_ports):
		print('port DNE')
	output = subprocess.check_output("ssh -o StrictHostKeyChecking=no -p " + str(port) + " " + IP,shell=True)
	output = str(output)
	if 'Lower' in output :
		lower = port
	if 'Higher' in output :
		higher = port 
	if 'real service' in output:
		print(output)
	print(output)
	print(str(port))
print(output)
print(str(port))