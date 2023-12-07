#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()

    # Iterate through the elements in my_list
    for num in my_list:
        # Add unique integers to the set
        unique_integers.add(num)

    # Calculate the sum of unique integers
    sum_unique = sum(unique_integers)

    return sum_unique
