# want to get the min number of parentheses needed to make a string valid

test ='()))))))))))))))))))))))()()))()))))))))()))))))()))()))))(()))))))))))))()))))))(()))))))))()()))))))))))))()))))(())()))))))(()))))()))))))()))()())))())))))))))))()))())(()()())()()())))))()))))())()))()))))))))))))))()())))()))))()))))))()))())()))())))(()))()))))))))())))())))(())()))))()((()))))))((((()())())())(())))))())())))))))())))))()(()))))()))))())))))()())())()))()))))))))()))))))))))()))))())))))(((()))))()))((())))())))))))())))()()())())))))())))())())))))(())())))))))())))()()))))))))))))(())())())))((()))))))(())))()())))()))))(())))(())))))))))))))(())))(())()))))(()))())())))))))()())(()(())())))))))))))))))))))))))((()())))())))())))((()())))()))())()))))())()())))))))))))(()))))))))))))))()))))))()))))))))))))))))(()(()))(()))()))))))()))()()))))))))))()))())()))))())))()()()))()))))(())))))))))))))()()))))(())))()))))))()))()())()))())()())())))()()(()())))))()())))))))())))())))(())))())))))))()))))))))()((()(())))))))))(())))())))())))))))))()())))()))))))))('
test2 =')))))))))))))))))))))))()()))()))))))))()))))))()))()))))(()))))))))))))()))))))(()))))))))()()))))))))))))()))))(())()))))))(()))))()))))))()))()())))())))))))))))()))())(()()())()()())))))()))))())()))()))))))))))))))()())))()))))()))))))()))())()))())))(()))()))))))))())))())))(())()))))()((()))))))((((()())())())(())))))())())))))))())))))()(()))))()))))())))))()())())()))()))))))))()))))))))))()))))())))))(((()))))()))((())))())))))))())))()()())())))))())))())())))))(())())))))))())))()()))))))))))))(())())())))((()))))))(())))()())))()))))(())))(())))))))))))))(())))(())()))))(()))())())))))))()())(()(())())))))))))))))))))))))))((()())))())))())))((()())))()))())()))))())()())))))))))))(()))))))))))))))()))))))()))))))))))))))))(()(()))(()))()))))))()))()()))))))))))()))())()))))())))()()()))()))))(())))))))))))))()()))))(())))()))))))()))()())()))())()())())))()()(()())))))()())))))))())))())))(())))())))))))()))))))))()((()(())))))))))(())))())))())))))))))()())))()))))))))('
test1=')))((('

def get_min(string):
    count=0
    if string[0]=='(':
        switch = 1
    else:
        switch = -1
    for ind, t in enumerate(string):
        #print(count)
        #print(string[:i])
        if t == '(':
            count += switch*1
        elif t == ')':
            count += -1*switch
        if count == 0:
            switch=switch*(-1)
        if ind <len(string):
            if string[ind]==')' and string[ind+1]=='(':
                switch=switch*(-1)



    return abs(count)

def new_min(string):
    lst=string.split(')(')
    fixed = fix(lst)
    count=0
    for substring in fixed:
        count+=get_min(substring)
    return count

def fix(lst):
    fixed =[]
    for i, item in enumerate(lst):
        if i%2==0:
            fixed.append(item+')')
        else:
            fixed.append(item + '(')
    return fixed

def rec_min(string):
    if string=='':
        return 0
    elif len(string) == 1:
        return 1
    elif string[0] == '(':
        if string[1] == ')':
            return rec_min(string[1:]) - 1
        else:
            return rec_min(string[1:])+1
    elif string[0] == ')':
        return rec_min(string[1:])+1

def new_get_min(string):
    if string[0]=='(':
        left_or_right='left'
    else:
        left_or_right = 'right'
    for t in string:
        current = left_or_right
        if current == 'left':
            if t == '(':
                count_left += 1
            elif t == ')':
                count_left -= 1

        else:
            if t == '(':
                count_right -= 1
            if t == ')':
                count_right += 1
        if current == 'left':
            if count_left == 0:
                left_or_right = 'right'
        elif current == 'right':
            if count_right == 0:
                left_or_right = 'left'
        print(f'current:{current}, left:{count_left}, right:{count_right}')
    return max(count_right,count_left)

def online_sol(p):
    bal = 0
    ans = 0
    for i in range(0, len(p)):
        if (p[i] == '('):
            bal += 1
        else:
            bal += -1

        # It is guaranteed bal >= -1
        if (bal == -1):
            ans += 1
            bal += 1
    return bal + ans

print(online_sol(test))

def dummy(sample):
    count=0
    for t in sample:
        if t != ')':
            count+=1
    print(f'there are {count} non ")" in the sample')

'''
'''
