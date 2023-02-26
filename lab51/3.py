import re


s = input()
x = re.findall('[a-z]+_', s)
print(x)
if x:
    print("There is a match")
else:
    print("None")
