#given a target string and a list of other strings, can you construct the desired
# string from this list

def can_construct(word, array):
    pass
    if word == '':
        return True
    for test_word in array:
        if word.startswith(test_word):
            rem=word.lstrip(test_word)
            return can_construct(rem, array)
    return False

def bad_can_construct(target, array):
    if target=='':
        return True
    for word in array:
        if word==target[0:len(word)]:
            return bad_can_construct(target[len(word):], array)
    return False

def bad_can_construct_c(target, array, cache):
    if target in cache:
        return cache[target]
    elif target=='':
        return True
    for word in array:
        if word==target[0:len(word)]:
            cache[target]=bad_can_construct_c(target[len(word):], array, cache)
            return cache[target]
    return False

e_word='ee'*498+'eea'
e_bank=['eeeeeeeeee'[0:i+2] for i in range(2)]

example={
    'abcdef':['abc', 'ab', 'def'],
    'skateboard':['sk','ska','te','eboar','boa','rd'],
    e_word:e_bank
}
for key, value in example.items():
    print(bad_can_construct_c(key, value, {}))