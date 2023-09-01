test = list(range(100))
test1 = list(range(10))
test2=[7,5,2,7,8,-2,25,25]

def meandering_sorT(lst):
    sol=[]
    max_or_min='max'
    lst.sort()
    while lst !=[]:
        if max_or_min =='max':
            print(lst[-1])
            sol.append(lst.pop(-1))
            max_or_min = 'min'
        elif max_or_min == 'min':
            print(lst[0])
            sol.append(lst.pop(0))
            max_or_min = 'max'
        print(sol)
    return sol

print(meandering_sorT(test2))

