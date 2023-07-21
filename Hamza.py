import platform
bit = platform.architecture()[0]
if bit == '64bit':
  import AB.64
if bit == '32bit':
  import AB.32
