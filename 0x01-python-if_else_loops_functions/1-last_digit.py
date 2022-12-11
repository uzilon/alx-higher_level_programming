#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numstr = str(number)
last_number = numstr[-1]
last_number = int(last_number)
if last_number > 5:
    print(f"Last digit of {number:d} is {last_number:d} and is greater than 5")
elif last_number > 5:
    print(f"Last digit of {number:d} is {last_number:d} and is 0")
elif last_number < 6 and last_number != 0:
    print(f"Last digit of {number: d} is {last_number: d}
          and is less than 6 and not 0")
