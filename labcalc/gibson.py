#!/usr/bin/env python3

"""Gibson (Isothermal) Assembly"""
#insert function to get variables for calculations

def gibson_calc(fragments):
    """
    Calculate ul needed for 1 insert, 1 vector for gibson assembly
    input
    fragments = {'vector': [v_size,v_conc], 'insert1': [i1_size, i1_conc]}
    size = base pairs; conc = ng/ul
    
    return
    reaction = {'vector': v_ul, 'insert1': i1_ul}
    """
    #vector calculations
    v_ng = 100 #suggested by protocol, can be changed
    v_pmol = v_ng*(1000/(fragments['vector'][0]*650))
    v_ul = v_ng/fragments['vector'][1]
    #insert calculations for 2 or less inserts
    i1_pmol = v_pmol*2
    i1_ng = i1_pmol/(1000/(fragments['insert1'][0]*650))
    i1_ul = i1_ng/fragments['insert1'][1]
    reaction = {'vector': v_ul, 'insert1': i1_ul}
    return reaction
