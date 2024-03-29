#!/usr/bin/python3
"""Defines save_to_json_file function."""


import json


def save_to_json_file(myobj, filename):
    """write an object to text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
