#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """print to divid two lists of element by element.
    Agrs:
        my_list_1 (lis): the first list.
        my_list_2 (list): the second list.
        list_length (int): the No. of element to divide.
    Return:
        new list of length, list_length over all divisions."""

    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
        return (new_list)
