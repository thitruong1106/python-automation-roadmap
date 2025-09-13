#Error handling intro 

"""
    Write a loop that ask for numbers 
    if a user enter something invalid, catch the valueError and ask again 
    Only exit the loops once a valid integer is given 
"""
while True:
    try:
        user_num = int(input("Please enter a number: \n"))
        print(f"{user_num}")
        break
    except ValueError:
        print("Please Enter an int")