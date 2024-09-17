#!/usr/bin/python3
def args_add(argv):
    size = len(argv) - 1
    if size == 0:
        print("{:d}".format(size))
        return
    else:
        index = 1
        sum = 0
        while index <= size:
            sum += int(argv[index])
            index += 1
        print("{:d}".format(sum))


if __name__ == "__main__":
    import sys
    args_add(sys.argv)
