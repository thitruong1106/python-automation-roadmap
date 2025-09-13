#11/09/2025

"""
Write a script that prings checking... every seconds
Add a counter so it stops after 5 checks
"""
import time 
try:
    for _ in range(5): #run this 5 times. 
        print("checking....")  
        time.sleep(1)
except KeyboardInterrupt:
    print("Program ended by user")

print("Finished checks")