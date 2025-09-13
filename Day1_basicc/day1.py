def validate_num(prompt):
    
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            return number
        except ValueError:
            print("Invalid number")

odd_even = validate_num("Enter a number to check for odd of even") #store the number in odd_even

if odd_even % 2 == 0: 
    print(f"The number {odd_even} is even")
else:
    print(f"The number {odd_even} is odd")

age_gate = validate_num("What is your age")  

if age_gate >=18:
    print("Welcome!")
else:
    print("You are not allowed")

fizz_buzz = validate_num("Enter a number for fizzbizz")

for i in range(1, fizz_buzz + 1): #start at 1, end at number entered + 1
    if i % 3 == 0 and i % 5 == 0: 
        print("FizzBuzz")
    elif i % 3 == 0: 
        print("Fizz")
    elif i % 5 == 0: 
        print("Buzz")
    else:
        print(i)

temp = validate_num("Enter temperture in Celsius /n The program will convert it to fahrenheit")
fahrenheit = (temp * 9/5) + 32 
print(f"{temp} Celsius converted to Fahrenheit is {fahrenheit}")

username = input("Please enter your username")
password = input("Please enter your password")

if username == "admin" and password == "password":
    print("Access granted")
else:
    print("you are not welcome")