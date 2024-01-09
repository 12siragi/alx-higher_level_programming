#!/usr/bin/python3
"""
Contains the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """return true if obj is an instance or inherited ,else False"""
    '''can also use issubclass'''
    return isinstance(obj, a_class)
