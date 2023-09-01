import time
from functools import wraps

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('==starting timer')
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'== {func.__name__} took {int(end - start)} secodns to complete')
    return wrapper

def print_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print()
        print('***args')
        for arg in args:
            print(f'={arg}')
        print('**** kwargs')
        for k, v in kwargs.items():
            print(f'= {k}: {v}')
        print()
        func(*args, **kwargs)

    return wrapper

aristocrats = {'asd':123, 'as':31}

@time_it
@print_args
def stupid(*months, **aristocrats):
    '''Hello'''

    print('start thing')
    time.sleep(3)
    print('ending thing, slept for 3 seconds.')


from functools import wraps


def make_html(argument):
    def dumb_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return '<'+argument+'>'+func(*args, **kwargs)+'</'+argument+'>'
        return wrapper
    return dumb_decorator

@make_html('p')
def get_text(text='I code with PyBites'):
    return text

print(get_text())





def decorator_func(x, y):
    def Inner(func):
        def wrapper(*args, **kwargs):
            print("I like Geeksforgeeks")
            print("Summation of values - {}".format(x + y))

            func(*args, **kwargs)

        return wrapper

    return Inner


@decorator_func(x=1,y=3)
def my_fun(*args):
    for ele in args:
        print(ele)

my_fun('ads')