import re


s = input()
x = re.sub('_', ' ', s).title()
print(x.replace(" ",""))
