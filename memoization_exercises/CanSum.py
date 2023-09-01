#This is for determining if a target can be written as a sum
# of numbers from a given array/list
from functools import lru_cache

def can_sum(target, array):

    #Here are the "exit" conditions
    #min = min(array)
    if target==0:
        print('yea, it can be done.')
        return True
    elif target <0:
        return False
    print(f'computing can_sum on {target} and {array}.')
    for number in array:
        remainder = target-number
        if can_sum(remainder, array):
            return True
    return False


def can_sum_m(target, array,cache={}):
    print(f'computing can_sum on {target} and {array}.')
    #Here are the "exit" conditions
    #min = min(array)
    if target in cache:
        return cache[target]
    elif target == 0:
        print('Yes, it can be done.')
        return True
    elif target <0:
        return False
    for number in array:
        remainder = target-number
        if can_sum_m(remainder, array, cache):
            cache[remainder] = True
            return cache[remainder]
        cache[remainder]=False
    return False

#can_sum(7,{3,4,5})
#can_sum_m(1089,{3,4})
can_sum_m(3003, {10,14})