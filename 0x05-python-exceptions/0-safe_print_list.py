#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ Print a specified number of elements from a list.

    Args:
        my_list (list): The list from which elements will be printed.
        x (int): The number of elements to print from the list.

    Returns:
        int: The count of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
