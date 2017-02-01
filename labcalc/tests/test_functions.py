#!/usr/bin/env python3
from labcalc.run import *
from labcalc import gibson

# labcalc.gibson

def test_gibson_one_insert():
    d = {'insert1': [300, 50], 'vector': [5000, 50]}
    assert gibson.gibson_calc(d) == {'insert1': 0.24, 'vector': 2.0}
