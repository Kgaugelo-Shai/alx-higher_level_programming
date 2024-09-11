#!/usr/bin/python3
def fizzbuzz():
    for digits in range(1, 101):
        if digits % 3 == 0 and digits % 5 == 0:
            print("FizzBuzz ", end="")
        elif digits % 3 == 0:
            print("Fizz ", end="")
        elif digits % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(digits), end="")
