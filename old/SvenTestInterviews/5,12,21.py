test =89

def iteration(number):
    string_number = str(number)
    result = 0
    for digit in string_number:
        result += int(digit)**2
    return result

def happy_check(number):
    count = 0
    input = number
    previous_values=[]
    while number !=1 and number !=2:
        print(number)
        count += 1
        number = iteration(number)
    if number == 1:
        print(f'the number {input} is indeed happy.')
        return True
    else:
        print(f'the number {number} is not happy, it results in a loop.')
        return False


'''
89 -> 64+81=145-> 1+16+25=42-> 20->3->16
'''

happy_check(2)