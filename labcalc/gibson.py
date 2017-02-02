#!/usr/bin/env python3

"""Gibson (Isothermal) Assembly"""

def input_info(insert_number):
    """
    input
    number of inserts

    prompts for
    size = base pairs; conc = ng/ul

    returns
    fragments = {'vector': [v_size,v_conc], 'insert1': [i1_size, i1_conc], ...}

    """
    n = 1
    fragments = {}
    for numbers in range(insert_number):
        insert_bp_input = float(input(('insert' + str(n) + ' bp: ')))  #insert has to be an integer
        insert_conc_input = float(input('insert' +str(n) + ' conc: '))
        fragments['insert' + str(n)] = [insert_bp_input, insert_conc_input]
        n = n + 1

    vector_ng_input = float(input('vector bp: '))
    vector_conc_input = float(input('vector conc: '))
    fragments['vector'] = [vector_ng_input, vector_conc_input]
    return(fragments)

def gibson_calc(fragments):
    """
    Calculate ul needed for 1 vector and 1+ inserts for gibson assembly
    #suggested by protocol - indicates where protocol defaults are. These may need to be altered if troubleshooting

    input
    fragments = {'vector': [v_size,v_conc], 'insert1': [i1_size, i1_conc], ...}
    size = base pairs; conc = ng/ul

    return
    reaction = {'vector': v_ul, 'insert1': i1_ul, ...}
    """

    #vector calculations
    v_ng = 100 #suggested by protocol
    v_pmol = v_ng*(1000/(fragments['vector'][0]*650))
    v_ul = v_ng/fragments['vector'][1]
    reaction = {'vector':v_ul}

    #determine vector:insert ratio
    if len(fragments) <= 3:
        ratio = 2 #suggested by protocol
    if len(fragments) > 3:
        ratio = 1 #suggested by protocol

    #insert calculations
    for key in fragments:
        if key.startswith('insert'):
            i_pmol = v_pmol*ratio
            i_ng = i_pmol/(1000/(fragments[key][0]*650))
            i_ul = i_ng/fragments[key][1]
            reaction[key] = i_ul

    return reaction

def print_result(dictionary):
    print('') #blank row for clarity
    print('Microliters for each fragment:')
    for key in dictionary:
        print(key, str(round(dictionary[key],2))+'ul')

#in progress writing
def analyze_results(fragments,results,insert_number):
    #test ul are within 10ul available for standard reaction
    #test ul amount is reasonable
    sum_ul = 0
    for key in results:
        sum_ul += results[key]
        if results[key] < 1:
            print('ul too small for %s. May want to dilute.' %key)
    if sum_ul > 10:
        print('Total of %sul exceeds standard 10ul for reaction.' %round(sum_ul,2))

    #test pmol are within range for given fragment number
    ratio = 2
    if insert_number >2:
        ratio = 1
    v_ng = 100 #suggested by protocol
    sum_pmol = v_ng*(1000/(fragments['vector'][0]*650)) #start equal to v_pmol

    for key in fragments:
        if key.startswith('insert'):
            sum_pmol += v_ng*(1000/(fragments['vector'][0]*650))*ratio
    if insert_number <= 2:
        if not(sum_pmol>=0.03 and sum_pmol <=0.2):
            print('Total of %spmol is outside recommended range for 2-3 total fragments' %round(sum_pmol,2))
    if insert_number >2:
        if not(sum_pmol>=0.2 and sum_pmol <=0.5):
            print('Total of %spmol is outside recommended range for 4-6 total fragments' %round(sum_pmol,2))


def gibson():
    #running the program
    insert_number = int(input('number of inserts (not incluing vector): '))
    fragments = input_info(insert_number)
    results = gibson_calc(fragments)
    print_result(results)
    analyze_results(fragments,results,insert_number)


if __name__ == '__main__':
    gibson()
