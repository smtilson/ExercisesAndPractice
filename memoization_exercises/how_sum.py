#takes a target and an array and returns a sum that adds up to exactly that target.

def how_sum(target, array):
    if target == 0:
        return []
    elif target < 0:
        return None
    for num in array:
        remainder = target-num
        res = how_sum(remainder, array)
        if res is not None:
            print(f'res is {res} and num is {num}')
            res.append(num)
            return res
    return None

def how_sum_c(target, array, cache={}):
    if target in cache:
        return cache[target]
    elif target == 0:
        return []
    elif target < 0:
        return None
    for num in array:
        remainder = target-num
        res = how_sum_c(remainder, array, cache)
        if res is not None:
            print(f'res is {res} and num is {num}')
            res.append(num)
            cache[remainder]=res
            return cache[remainder]
    cache[target]= None
    return None


print(how_sum(8,[3,2]))
print(how_sum(7,[2,4]))
print(how_sum_c(2070,[12,14]))
