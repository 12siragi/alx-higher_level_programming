#!/usr/bin/python3
'''function dumps obj to file'''

import json


def save_to_json_file(my_obj, filename):
    """
     Write an object to a text file using JSON representation
     Args: filename , my_obj
     Retrun: obj dumped into file
    """

    with open(filename, "w") as filee:
        json.dump(my_obj, filee)
