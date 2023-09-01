import itertools
import time
import sys


def spinner_cycle_demo():
    thing = itertools.cycle('-\|/')

    while True:
        sys.stdout.write('\r'+next(thing))
        sys.stdout.flush()
        time.sleep(.5)

def prod_demo():
    #repeat argument is like cartesian power
    # you can also put another iterable in there.
    product = itertools.product('John', ['apple','thomas'], (2,123,3))
    for t in product:
        print(t)

def combinations_demo():
    friends = 'mike bob julian'.split()
    print(itertools.combinations(friends, 2))
    print(list(itertools.combinations(friends, 2)))

def permutations_demo():
    friends = 'mike bob julian'.split()
    print(itertools.permutations(friends, 2))
    print(list(itertools.permutations(friends, 2)))

permutations_demo()