#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx > 0) or (len(my_list) >= idx):
        return (my_list)
    if element:
        new_list = my_list[:]
        new_list[id] = element
        return (new_list)
