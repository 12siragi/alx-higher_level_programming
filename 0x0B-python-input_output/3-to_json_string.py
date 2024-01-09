#!/usr/bin/python3
'''define a JSON module'''
import json


def to_json_string(my_obj):
    """
  Converts an object to its JSON string representation.

  Args:
    my_obj: The object to be serialized.

  Returns:
    A string representing the JSON encoding of the object.

  """

    return json.dumps(my_obj)
