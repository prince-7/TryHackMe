# -*- coding: utf-8 -*-
import pickle
with open('download.dat', 'rb') as file:
	pickle_data = file.read()
	creds = pickle.loads(pickle_data)

user = ['']*30
password = ['']*30
for i in range(len(creds)):
	if 'user' in creds[i][0]:
		user[int(str(creds[i][0][8:]))] = str(creds[i][1])
	if 'pass' in creds[i][0]:
		password[int(str(creds[i][0][8:]))] = str(creds[i][1])
print(''.join(user))
print(''.join(password))