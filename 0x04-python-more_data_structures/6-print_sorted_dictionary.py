#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort keys in alphabetical order
    sorted_keys = sorted(a_dictionary.keys())
    
    # Iterate through sorted keys and print dictionary contents
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
