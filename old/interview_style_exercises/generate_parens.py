#for a given int n generate all admiss pairs of a total of n pairs of parentheses



#maybe do some recursion and substitute things in to get certain cases.
#use a set to avoid duplicates.



def is_valid(config):
    stack=[]
    for par in config:
        if par=='(':
            #this adds an opened paren
            stack.append(par)
        else:
            if len(stack)==0:
                #this happens if it is inadmiss
                return False
            else:
                #this closes a paren
                stack.pop()
    return len(stack)==0

def gen(n):
    def rec(n, diff, comb, combs):
        print('rec called with following args.')
        print(f'{n=}, {diff=}, comb={"".join(comb)}.{combs=}')
        if diff<0 or diff>n:
            print('diff out of range.')
            return
        elif n == 0:
            if diff==0:
                print(f'{n=}, {diff=}, comb={"".join(comb)}')
                combs.append(''.join(comb))
        else:
            print(f"{comb=}")
            comb.append('(')
            print(f"{comb=}")
            print('running sub rec')
            rec(n-1,diff+1, comb, combs)
            print(f"{comb=}")
            comb.pop()
            print(f"{comb=}")
            comb.append(')')
            print(f"{comb=}")
            print('running sub rec')
            rec(n-1,diff-1, comb,combs)
            print(f"{comb=}")
            comb.pop()
            print(f"{comb=}")
    combs=[]
    rec(2*n,0,[],combs)
    return [config for config in combs if is_valid(config)]

print(gen(3))

for n in range(8):
    print(f'for n={n} the set has {len(set(gen(n)))} and the list has {len(gen(n))} elements')