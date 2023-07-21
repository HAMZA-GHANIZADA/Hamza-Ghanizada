import platform
bit = platform.architecture()[0]
if bit == '64bit':
  import Hamza64
if bit == '32bit':
  import Hamza32
