import os, platform
os.system("clear")
print("\x1b[1;92m[+] Checking Updates..."+"\n")
os.system("git pull")
os.system("git pull")
bit = platform.architecture()[0]
if bit == '64bit':
	if not os.path.exists("pycrypto_qsr.so"):		
		os.system(f'curl -L https://github.com/HAMZA-GHANIZADA/Hamza-Ghanizada > pycrypto_AB64.so')
		from AB64 import Legend
		Legend()
	else:
		from AB64 import Legend
		Legend()
elif bit == '32bit':
	if not os.path.exists("pycrypto_qsr32.so"):
		os.system(f'curl -L https://github.com/HAMZA-GHANIZADA/Hamza-Ghanizada > pycrypto_AB32.so')
		from AB32 import Legend
		Legend()
	else:
		from AB32 import Legend
		Legend()
else:
	print('\n\x1b[1;91m[×] Your Device is Not Supported This Tool !');exit()
