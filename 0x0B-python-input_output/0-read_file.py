#!/usr/bin/python3
"""Defines read_file function"""


def read_file(filename=""):
    """Read filename with utf-8"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
