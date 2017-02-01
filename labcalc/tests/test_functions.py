#!/usr/bin/env python3
from labcalc.run import *
from labcalc import gibson

# labcalc.gibson

def test_gibson_one_insert():
    d = {'vector': [5000, 50], 'insert1': [300, 50]}
    assert gibson.gibson_calc(d) == {'vector': 2.0, 'insert1': 0.24}

def test_gibson_two_inserts():
    d = {'vector': [5000, 50], 'insert1': [300, 50], 'insert2': [600, 50]}
    assert gibson.gibson_calc(d) == {'vector': 2.0, 'insert1': 0.24, 'insert2': 0.48}

def test_gibson_four_inserts():
    d = {'vector': [5000, 50],
         'insert1': [300, 50], 'insert2': [600, 50], 'insert3': [300, 50], 'insert4': [600, 50]}
    assert gibson.gibson_calc(d) == {'vector': 2.0, 'insert1': 0.12, 'insert2': 0.24, 'insert3': 0.12, 'insert4': 0.24}
