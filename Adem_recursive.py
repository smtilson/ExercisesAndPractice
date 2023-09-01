# the point of this is to run the Kristensen algorithm for
# recursively computing the Adem relations

def is_admiss(sample: tuple):
    if sample[0]>=2*sample[1]:
        return True
    else:
        return False

def proto(sample: tuple):
    if not is_admiss(sample):
        return (2*sample[1]-1,sample[1])
    else:
        #I am not sure if this is what I actually want here.
        return sample

def der(sample: tuple, k: int):
    first = (sample[0]- 2**k, sample[1])
    second = (sample[0], sample[1]-2**k)
    first=check_out(first)
    second=check_out(second)
    print(first)
    print(second)
    if first == 0 and second == 0:
        return ''
    elif first == 0:
        return str((second[0], second[1]))
    elif second == 0:
        return str((first[0], first[1]))
    else:
        return str((first[0], first[1])) + ' + ' + str((second[0], second[1]))

def lin_der(sum:str, k:int):
    summands = [eval(sum.split(+)]

def check_out(sample: tuple):
    if sample[0]<0 or sample[1]<0:
        return 0
    else:
        return sample

def two_max(total: int):
    #this should return the largest power of 2 smaller than the int
    for k in range(total):
        if total-2**k>=0:
            continue
        else:
            return 2**(k-1)


a = (2,5)
print(proto(a))

print(der(a,0))
print(der(a,1))
print(der(a,2))
