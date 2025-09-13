"""
    Learning goals, 
    - to understand and use lists, dicts, sets, typles 
    - learn file handling: reading, writing, appending 
    - apply this knowledge in mini project (simple logger + expense tracker)
"""

"""
    Create a list of 5 numbers 
    - print the first element 
    - print the last element 
    - the list lenght
"""

import random

random_int = [] #create an empty list to store random int 

for _ in range(5): #Run this 5 times 
    random_int.append(random.randint(1, 10))

print(random_int)
#[5, 1, 8, 6, 2]
print(random_int[0]) #print item in first location 
print(random_int[-1]) #print item in last location
print(len(random_int))

random_int.append(11) #add 11 to list 
print(random_int)
random_int.remove(11) #remove 11 from list 
print(random_int)