import os
os.system('git pull')
from os import system
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
    import hmxa
else:exit('\033[1;31m\n Sorry System or 32bit device not supported ')
