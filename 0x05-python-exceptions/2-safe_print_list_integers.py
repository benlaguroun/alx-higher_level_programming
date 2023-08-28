#!/usr/bin/python3
"""
Print the first x integer elements from a list.

Args:
    my_list (list): The list from which to print integer elements.
    x (int): The number of integer elements to print.

Returns:
    int: The count of integer elements printed.
"""
ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)

