#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r") as f:
        for 1i in f:
            print(1i, end="")
    f.closed
