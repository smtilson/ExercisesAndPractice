#This is a reconstruction of the fibonacci sequence
#I know there is a decorator for this, I wonder if I can make my own...
# note that the decorators cache and lrucache from functools do this
#also, lrucache takes an argument for how many previous values you want to keep track of.

def fibonacci(n):
    #without memo
    if type(n) != int or n < 0:
        raise TypeError(f'You must enter a non-negative integer, not a {type(n)}.')
    elif n in {0,1}:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


for _ in range(10):
    print(fibonacci(_))


def fibonacci_m(n, cache: dict = {}):
    if type(n) != int or n < 0:
        raise TypeError(f'You must enter a non-negative integer, not a {type(n)}.')
    elif n in cache:
        return cache[n]
    elif type(n) != int or n < 0:
        #raise
        print(f'You must enter a non-negative integer, not a {type(n)}.')
        return None
    elif n in (0, 1):
        cache[n] = n
    else:
        cache[n] = fibonacci_m(n-1, cache)+fibonacci_m(n-2, cache)
    return cache[n]


print(fibonacci_m(5000))

222232244629420445529739893461909967206666939096499764990979600