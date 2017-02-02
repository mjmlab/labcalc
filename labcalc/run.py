#!/usr/bin/env python3

"""Parse the command line arguments and call the program."""
from .gibson import gibson

def runner(args):
    """Run the specified program"""
    eval(args[0] + '()')
