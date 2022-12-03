#!/usr/bin/python3
"""a function that prints all integers of a list"""


def print_list_integer(my_list=[]):
    new_list = my_list

    for number in new_list:
        print("{}".format(number))
