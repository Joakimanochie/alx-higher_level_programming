#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    num_arg = len(argv)
    print("{} ".format(num_arg- 1), end="")
    if (num_arg - 1 == 1):
        print("argument:")
    else:
        print("arguments", end="")
        if (num_arg - 1 == 0):
            print(".")
        else:
            print(":")
    for i in range(1, num_arg):
        print("{}: {}".format(i, argv[i]))
