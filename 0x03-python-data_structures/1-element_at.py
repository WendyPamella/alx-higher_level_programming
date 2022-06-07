#!/usr/bin/python3


def element_at(my_list, idx):
    """ Returns an element in a list"""
    if idx < 0 or idx > len(my_list) - 1:
        return None
    else:
        return my_list[idx]
