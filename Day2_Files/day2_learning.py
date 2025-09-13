#list are used to store multiple items in a single variable 

"""
List is one of the 4 built in date type in python used to store collections of data 
    The other 3 is 
        Tuple 
        Set 
        Dictionary 

List is created using square bracket []
"""

list = [1,2,3,4,5]
print(list)

#list are ordered, it means that the items have a defined order, and that order will not change. 
#if you add a new item, that order will not change. the new item will be placed at the end of the list 

#Changeable - The list is changeable, meaning we can ADD, CHANGE, and REMOVE, after a list has been created 

#since list are index, list can have items of the same value. 

#to get the length of list 
print(len(list))

#data types 
#string, int, boolean data types 

#A list with strings, int, and boolean, 
list1 = ["abc", 34, True, 40, "male"]
#data types 

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

"""

Access items 

List items are indexed, and you can access them by referring to the index number 

"""

print(mylist[1]) #will print second position item
print(mylist[-1]) #last item, -2 second last item

# Range of index - we can specifiy a range of indexes by specifying where to start and where to end the range. 
print(mylist[0:2])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #this will print the list, except for index 4 kiwi 
print(thislist[2:]) #this return items from index two, forward.

###CHANGING ITEM 
#change item value 
thislist[1] = "blackcurrant" #this will change index item 1, to 

"""
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] #will remove item 2
print(thislist)

###APPENDING ITEMS#### 

thislist.append("orage") #add orange to the list 

# INSERTING ITEM # 
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") #insert orange at index 1
print(thislist)

#remove an iteam 
thislist.remove("apple") #remove apple from list, if theres duplicates, it will remove the first apple 

#pop() method removes at certain index
thislist.pop(1) #remove item at index 1 
#if 1 is not specify, it will remove the last item 

#del thislist will delete the list 
#clear will clear the list 

#looping through a list 
for x in thislist:
    print(x)
    #will print each item of the list 

#looping through a list with index number [0,1,2]
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i], [i]) #loops through each inedx, print the item name, and print the index locaitons

#WHILE LOOP 
#can loop thorugh the list items by using a while loop 
# using the len() function to deletermine the length of the list. Then start at 0, and loop your way through the list item by referr

#Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


"""
List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.


"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
#for item in fruits, if it contains a, append to new list
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#sorting list 
thislist.sort() #will srot alphanumerically, ascending by default. 
#.sort(reverse=True), will sort decensding. 

#make a copy 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#joining list 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)