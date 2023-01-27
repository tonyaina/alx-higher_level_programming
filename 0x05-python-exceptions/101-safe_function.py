#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """print executes a function safely.
    Args:
        fct: the function to execute.
        args: arguments for fct.
    Return:
        if an error occurs - None.
        Otherwise - the result of the call to fct.
    """

    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
