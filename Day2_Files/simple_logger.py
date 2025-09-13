"""



"""
import datetime
user_text = input("What would you like to log to file ? ")
# Get the current datetime
current_datetime = datetime.now()

# Format the datetime object as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

with open("logger.txt", "a") as f:
    f.write(f"{formatted_datetime} - {user_text}\n")  

with open("logger.txt") as f:
    print(f.read())