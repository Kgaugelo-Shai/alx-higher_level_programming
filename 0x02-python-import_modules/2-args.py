#!/usr/bin/python3
# program that prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys

    args_ls = sys.argv
    num = len(args_ls) - 1

    if num > 1:
        print("{} arguments:".format(num))
        for index in range(1, num + 1):
            print("{}: {}".format(index, args_ls[index]))
    elif num == 0:
        print("{} arguments.".format(num))
    else:
        print("{} argument:".format(num))
        print("{}: {}".format(num, args_ls[1]))
