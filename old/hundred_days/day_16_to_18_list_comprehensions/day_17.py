NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

import random

def convert_to_title(sample_list):
    #this works
    return [name.title() for name in sample_list]

def gen_titles(sample_list):
    #this works
    for name in sample_list:
        yield name.title()

def swap_first_and_last_names(sample_list):
    # this works
    return [name.split()[1]+' '+name.split()[0] for name in sample_list]

def gen_swaps(sample_list):
    # this works
    for name in sample_list:
        yield name.split()[1]+' '+name.split()[0]

def gen_pairs(sample_list):
    k=len(sample_list)
    while k>1:
        first = sample_list.pop(random.randint(0, k-1))
        k-=1
        second = sample_list.pop(random.randint(0, k-1))
        k-=1
        yield first.split()[0] + ' teams up with '+second.split()[0]

pairs = gen_pairs(NAMES)
for i in pairs:
    print(i)
