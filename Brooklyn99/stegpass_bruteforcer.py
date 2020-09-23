import subprocess
file = open("/home/elli0t/Downloads/common.txt","r")
file = file.read()
psswd = file.split('\n')
passphrase = ''
for i in range(len(psswd)):
	out = subprocess.run('steghide extract -sf brooklyn99.jpg -p '+ psswd[i], shell=True)
	out=str(out)
	if('note.txt' in out):
		out = subprocess.run('y', shell=True)
		print(psswd[i])
		break
