# Writeup for Kenobi (TryHackMe)

Samba is the standard Windows interoperability suite of programs for Linux and Unix. It allows end users to access and use files, printers and other commonly shared resources on a companies intranet or internet. Its often refereed to as a network file system.

Samba is based on the common client/server protocol of Server Message Block (SMB). SMB is developed only for Windows, without Samba, other computer platforms would be isolated from Windows machines, even if they were part of the same network.


# Scan the machine with nmap, how many ports are open?
7 ports are open.

____________________________________________________________________________


Nmap has the ability to run to automate a wide variety of networking tasks. There is a script to enumerate shares!
```
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.97.17
```

____________________________________________________________________________

	
On most distributions of Linux smbclient is already installed. Lets inspect one of the shares.

smbclient //<ip>/anonymous

_____________________________________________________________________________

We can find a file in the system. > log.txt
You can recursively download the SMB share too. Submit the username and password as nothing.

```
smbget -R smb://<ip>/anonymous
```

____________________________________________________________________________

Your earlier nmap port scan will have shown port 111 running the service rpcbind. This is just an server that converts remote procedure call (RPC) program number into universal addresses. When an RPC service is started, it tells rpcbind the address at which it is listening and the RPC program number its prepared to serve. 

In our case, port 111 is access to a network file system. Lets use nmap to enumerate this.
```
nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.97.17
```

we see /var 

_______________________________________________________________________

	
We can use searchsploit to find exploits for a particular software version.

Searchsploit is basically just a command line search tool for exploit-db.com

```
searchsploit ProFTPd 1.3.5
```

____________________________________________________________________________

	
You should have found an exploit from ProFtpd's mod_copy module. 

The mod_copy module implements SITE CPFR and SITE CPTO commands, which can be used to copy files/directories from one place to another on the server. Any unauthenticated client can leverage these commands to copy files from any part of the filesystem to a chosen destination.

We know that the FTP service is running as the Kenobi user (from the file on the share) and an ssh key is generated for that user.  

_____________________________________________________________________

We're now going to copy Kenobi's private key using SITE CPFR and SITE CPTO commands.

[image](LajBhh2.png)




