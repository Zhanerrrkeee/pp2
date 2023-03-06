import os  
path = r'C:\Users\asars\Desktop\pp2\lab6' 
 
if os.path.exists(path): 
    print(os.path.exists(path)) 
    print(os.path.basename(path)) 
    print(os.path.dirname(path))
