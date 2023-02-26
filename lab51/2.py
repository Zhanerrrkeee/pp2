import re


s = input()
x = re.findall('ab{2,3}',s)
print(x)
if x:
    print("There is a match")
else:
    print("None")
