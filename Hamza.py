import AB32_enc
import AB64_enc
import platform
bit = platform.architecture()[0]
if bit == '64bit':
  import AB64
elif bit =='32bit':
  import AB32
