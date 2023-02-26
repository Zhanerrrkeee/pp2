import re


s = input()
x = re.sub('[\s+]', ',', s)
print(x)
