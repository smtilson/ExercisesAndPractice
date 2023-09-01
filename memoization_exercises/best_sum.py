#the goal of this is to find the shortest way of writing a given int as a sum of elements from an array

#note that we have to be careful about early returns

from functools import lru_cache

def best_sum(target, array):
    if target == 0:
        return []
    elif target<0:
        return None
    shortest = None
    for num in array:
        rem=target-num
        res = best_sum(rem,array)
        if res is not None:
            res.append(num)
            if shortest is None:
                shortest=res
            elif len(shortest) > len(res):
                shortest=res
    return shortest

def best_sum_c(target, array, cache):
    #the lesson here is that if I return things from the dictionary that are mutable
    #then they will be changed if I do something to them.
    '.. '
    if target in cache.keys():
        return cache[target].copy()
    elif target == 0:
        return []
    elif target < 0:
        return None
    shortest = None
    for num in array:
        rem = target - num
        res = best_sum_c(rem, array, cache)
        #print(f'target is {target}, rem is {rem}, num is {num}, res is {res}')
        if res is not None:
            #print(f'appending {num} from {array} to {res}')
            res.append(num)
            if shortest is None:
                shortest = res
            elif len(shortest) > len(res):
                shortest = res
            #print(f'shortest is {shortest}')
    print(cache)
    print(f'cacheing {shortest} to key {target}')
    new = shortest.copy()
    cache[target] = new
    print(target, cache)
    return shortest

def best_sum_a(target, array, cache):
    #the lesson here is that if I return things from the dictionary that are mutable
    #then they will be changed if I do something to them.
    '.. '
    if target in cache.keys():
        return cache[target]
    elif target == 0:
        return []
    elif target < 0:
        return None
    shortest = None
    for num in array:
        rem = target - num
        res = best_sum_c(rem, array, cache).copy()
        #print(f'target is {target}, rem is {rem}, num is {num}, res is {res}')
        if res is not None:
            #print(f'appending {num} from {array} to {res}')
            res.append(num)
            if shortest is None:
                shortest = res
            elif len(shortest) > len(res):
                shortest = res
            #print(f'shortest is {shortest}')
    print(cache)
    print(f'cacheing {shortest} to key {target}')
    new = shortest.copy()
    cache[target] = new
    print(target, cache)
    return shortest

examples = {
    #7:[5,2,3,4],
    #4:[1,2,3],
    #4:[1,4,5],
    #8:[1,4,5],
    #30:[1,2,5,25],
    3:[1,2],
    #100:[1,2,5,25]
          }

def main(test):
    for key, value in test.items():
        print(f'running {key}: {value}')
        print(best_sum(key, value))

main(examples)
