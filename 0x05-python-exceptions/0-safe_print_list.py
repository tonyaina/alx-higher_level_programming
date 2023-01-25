#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """print x element of a list.
    Agrs:
        my_list (list): The list to be printed of elements.
        x (int): No. of elements my_list to print.
    Return:
        No. of printed elements."""

    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
