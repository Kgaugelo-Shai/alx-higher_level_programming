#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_d = number % 10
else:
    last_d = number % -10
str_output = "Last digit of {:d} is {:d} and is {}"
if last_d > 5:
    print(str_output.format(number, last_d, "greater than 5"))
elif last_d < 6 and last_d != 0:
    print(str_output.format(number, last_d, "less than 6 and not 0"))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_d))
