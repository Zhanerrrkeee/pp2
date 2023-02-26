import re


s = input()
x = re.findall('a(.+)b$', s)
print(x)
if x:
    print("There is a match")
else:
    print("None")
