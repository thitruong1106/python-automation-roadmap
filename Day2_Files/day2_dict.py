
#create a dictionary of car 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

#print the current keys list 
x = car.keys()

print(x) #before the change

#add a new key, with the value of white
car["color"] = "white"

print(x) #after the change