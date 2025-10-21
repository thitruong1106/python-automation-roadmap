"""
Purpose - Load people.csv file, print only names 
print rows where age >= 18 
count rows per city
"""

import csv 
with open("people.csv", newline="") as f:
    r = csv.DictReader(f) #Read file
    for row in r:
        print(row.get("name", ""))

#print ages over 18 
with open("people.csv", newline="") as f:
    r = csv.DictReader(f)
    for row in r:
        age = int(row.get("age", 0)) #convert string to int 
        if age >= 18:
            print(row)

#count rows per city 
counts = {}
with open("people.csv", newline="") as f:
    r = csv.DictReader(f)
    for row in r:
        city = row.get("city", "?")
        counts[city] = counts.get(city,0) + 1
print(counts)