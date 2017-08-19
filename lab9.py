from __future__ import print_function
import re

file = open('lab9-in-file', 'r')
content = file.read()
file.close()

file = open('lab9-out-file', 'w')
content = re.sub('the', 'xxx', content)
file.write(content)
file.close()

print("Done!!!")
