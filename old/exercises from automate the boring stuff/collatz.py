#This is the collatz sequence exervise from the section on functions.

def collatz(number):
    if number%2 == 0:
        return number//2
    else:
        return 3*number+1

def run_sequence():
    number = False
    while not number:
        try:
            print('Please input a positive integer:')
            number = int(input())
            while number != 1:
                print(f'Running collatz function on {number}.')
                print(f' The new value is {collatz(number)}.')
                number = collatz(number)
        except ValueError:
            print('That is not an integer.')
            number = False
    print('We have arrived at 1.')

run_sequence()