#!/usr/bin/env python3

"""Parse the command line arguments and call the program."""
import pkgutil
from .gibson import gibson

def runner(args):
    """Run the specified program"""
    eval(args[0] + '()')

def list():
    """List the programs available."""
    programs = {'gibson': 'Gibson (Isothermal) Assembly',
                #'pcr': 'Polymerase Chain Reaction',
               }
    for program in sorted(programs):
        print(program.ljust(15), programs[program])
