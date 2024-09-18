#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = [roman[c] for c in roman_string] + [0]
    count = 0

    for x in range(len(num) - 1):
        if num[x] >= num[x+1]:
            count += num[x]
        else:
            count -= num[x]

    return count
