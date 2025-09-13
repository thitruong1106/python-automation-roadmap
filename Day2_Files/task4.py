#File Handling 

"""
Write a script to 

- create a file notes.txt
- write "Day 2 file handling test" inside it 
- reopen and print the contents 

"""

"""
Create a New File

"x" - creat - will create a file, returns an error if the file exists 
"a" - append - will create a file if the specified file does not exists
"w" - write - will create a file if the specifc file does not exists 
"""


with open("notes.txt", "a") as f: 
    f.write("Day 2 file handling test")

#open and read the file after appending 
with open ("notes.txt") as f:
    print(f.read())