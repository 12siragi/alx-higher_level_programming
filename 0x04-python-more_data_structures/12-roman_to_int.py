#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_score = float('-inf')  # Initialize with negative infinity for comparison
    best_key = None

    # Iterate through the items in the dictionary
    for key, value in a_dictionary.items():
        # Check if the value is greater than the current max_score
        if value > max_score:
            max_score = value
            best_key = key

    return best_key
