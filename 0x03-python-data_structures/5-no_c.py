#!/usr/bin/python3


def no_c(my_string):
    str_copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(str_copy))
