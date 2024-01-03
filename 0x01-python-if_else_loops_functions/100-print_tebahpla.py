#!/usr/bin/python3
for index in range(ord('z'), ord('a') - 1, -1):
    if index % 2 == 0:
        num = 0
    else:
        num = 32
    print('{}'.format(chr(index - num)), end='')
