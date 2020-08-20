# NAX Writeup

Starting With basic enumerations we find this result with nmap
```
PORT    STATE SERVICE
22/tcp  open  ssh
25/tcp  open  smtp
80/tcp  open  http
389/tcp open  ldap
443/tcp open  https
```
So we have a website, the website has an ascii art and some elements of the periodic table. 
```
     ,+++77777++=:,                    +=                      ,,++=7++=,,
    7~?7   +7I77 :,I777  I          77 7+77 7:        ,?777777??~,=+=~I7?,=77 I
=7I7I~7  ,77: ++:~+777777 7     +77=7 =7I7     ,I777= 77,:~7 +?7, ~7   ~ 777?
77+7I 777~,,=7~  ,::7=7: 7 77   77: 7 7 +77,7 I777~+777I=   =:,77,77  77 7,777,
  = 7  ?7 , 7~,~  + 77 ?: :?777 +~77 77? I7777I7I7 777+77   =:, ?7   +7 777?
      77 ~I == ~77=77777~: I,+77?  7  7:?7? ?7 7 7 77 ~I   7I,,?7 I77~
       I 7=77~+77+?=:I+~77?     , I 7? 77 7   777~ +7 I+?7  +7~?777,77I
         =77 77= +7 7777         ,7 7?7:,??7     +7    7   77??+ 7777,
             =I, I 7+:77?         +7I7?7777 :             :7 7
                7I7I?77 ~         +7:77,     ~         +7,::7   7
               ,7~77?7? ?:         7+:77           77 :7777=
                ?77 +I7+,7         7~  7,+7  ,?       ?7?~?777:
                   I777=7777 ~     77 :  77 =7+,    I77  777
                     +      ~?     , + 7    ,, ~I,  = ? ,
                                    77:I+
                                    ,7
                                     :777
                                        :
				Welcome to elements.
			Ag - Hg - Ta - Sb - Po - Pd - Hg - Pt - Lr

```

## What hidden file did you find?
Now we can deduce that the elements must have a hidden message. So lets convert the elements to there periodic numbers and that may represent an ascii character for this we can write a basic python script.
```
from periodictable import elements
symbols = ['Ag', 'Hg', 'Ta', 'Sb', 'Po', 'Pd', 'Hg', 'Pt', 'Lr']
numbers={x.symbol:x.number for x in elements}
ans = []
for el in symbols:
	ans.append(chr(numbers[el]))
print(''.join(ans))
```
This gives output as :- /PI3T.PNg
this might be a hidden directory, so when visit the directory we find this image
![image](PI3T.PNg)

##	Who is the creator of the file?
Dowloading and reading metadata of this image we find the creator and understand that this is the piet esoteric language.

## If you get an error running the tool for on your downloaded image about an unknown ppm format -- just open it with gimp or another paint program and export to ppm format and try again!
After doing this we can decode the image using npiet tool.
```
./npiet -e 1000 ~/location/piet.ppm 
```
we get this 
```
nagiosadmin%n3p3UQ&9BjLp4$7uhWdY
```
% is a seperator.

##	What is the username you found?
nagiosadmin

## What is the password you found?
n3p3UQ&9BjLp4$7uhWdY

##	What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000
From internet we find NagiosXI vulnerability, CVE-2019-15949.

## Now that we've found our vulnerability, let's find our exploit. For this section of the room, we'll use the Metasploit module associated with this exploit. Let's go ahead and start Metasploit using the command `msfconsole`.

## After Metasploit has started, let's search for our target exploit using the command 'search applicationame'. What is the full path (starting with exploit) for the exploitation module?

searching for nagios_xi in msfconsole we find this exploit
exploit/linux/http/nagios_xi_authenticated_rce

##	Compromise the machine and locate user.txt & Locate root.txt
we are root so we can get user and root txt files easily.

