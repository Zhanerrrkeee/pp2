import math  
import time  
 
 
 
sec = int(input()) 
milisec = int(input()) 
time.sleep(milisec/1000) 

print("Square root of " , sec, "after", milisec , "miliseconds is ", math.sqrt(sec))
