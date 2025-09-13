"""
Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

"""

"""
    Create a dictionary 
    person = {"name": "Alice", "age": 25, "city": "Sydney"}

    print perosn name 
    update age to 26 
    add new key, job developer
"""

thisdict = {
    "name": "Alice",
    "age": 25,
    "city": "Sydney"
}


x = thisdict["name"]
print(x)

thisdict.update({"age": 26})
print(thisdict)

thisdict["job"] = "developer"

print(thisdict)

