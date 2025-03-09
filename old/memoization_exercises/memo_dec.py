"""This is an attempt to make my own decorator for
functions which implements memoization"""
from functools import wraps


def memo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'memo' not in func.__dict__:
            func.memo = dict()
        sorted_keys = list(kwargs.keys())
        sorted_keys.sort()
        kw_args = [(key, kwargs[key]) for key in sorted_keys]
        key = (tuple(args), tuple(kw_args))
        if key in func.memo.keys():
            return func.memo[key]
        value = func(*args, **kwargs)
        func.memo.update({key: value})
        return value
    return wrapper



def simple_memo(func):
    @wraps(func)
    def wrapper(argument):
        if 'memo' not in func.__dict__:
            func.memo = dict()
        if argument in func.memo:
            return func.memo[argument]
        value = func(argument)
        func.memo.update({argument: value})
        return value
    return wrapper

@memo
def fibonacci(n):
    if type(n) != int or n < 0:
        raise TypeError(f'You must enter a non-negative integer, not a {type(n)}.')
    elif n in {0, 1}:
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)

@memo
def fact(n):
    if n == 1:
        return n
    return n*fact(n-1)

print(fibonacci(100))