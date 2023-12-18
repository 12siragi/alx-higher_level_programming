#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(int(my_list[i])), end=" ")
                count += 1
            except (ValueError, TypeError):
                continue
    except IndexError:
        pass  # Expected exception when x is greater than the length of the list

    print()  # New line after printing integers
    return count
