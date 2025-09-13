import time
import random

in_stock = False

while True:
    print("Checking stock...")
    time.sleep(2)

    # simulate stock appearing randomly (1 in 5 chance)
    if random.randint(1, 5) == 3:
        in_stock = True

    if in_stock:
        print("Item is in stock!")
        break   # <-- exit the loop immediately
