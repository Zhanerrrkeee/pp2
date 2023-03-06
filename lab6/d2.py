import os  

path = r'C:\Users\asars\Desktop\pp2\lab6\dir-and-files\input.txt' 
path1 = os.access(path, os.F_OK) 
print("Exists the path:", path1) 
path2 = os.access(path, os.R_OK) 
print("Access to read the file:", path2) 
path3 = os.access(path, os.W_OK) 
print("Access to write the file:", path3) 
path4 = os.access(path, os.X_OK) 
print("Check if path can be executed:", path4)
