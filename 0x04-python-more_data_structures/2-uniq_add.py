#!/usr/bin/python3
def uniq_add(my_list=[]):
    for x in set(my_list):
        result = sum(set(my_list))
        return result
