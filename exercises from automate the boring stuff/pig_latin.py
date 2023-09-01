#this takes input and transforms it into pig latin

message = input()
vowels = ['a','e','i','o','u','y']

def translate_word(word):
    if len(word) == 0:
        return word
    elif word[0].lower() not in vowels:
        print(word[1:] + word[0] + 'ay')
        return word[1:]+word[0]+'ay'
    else:
        print(word + 'yay')
        return word + 'yay'

def case_trans(word):
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    new_word = translate_word(word.lower())
    if wasTitle:
        return new_word.title()
    elif wasUpper:
        return new_word.upper()
    else:
        return new_word

def translate_all(line):
    new_words=[]
    for word in line.split():
        pre, stripped_word, suff = remove_non_alpha(word)
        if len(word) == 0:
            new_words.append(pre+suff)
        else:
            new_words.append(pre+case_trans(stripped_word)+suff)

    new_line = ' '.join(new_words)
    return new_line

def remove_non_alpha(word):
    prefix_non_alpha = ''
    suffix_non_alpha = ''
    while len(word)>0 and not word[0].isalpha():
        prefix_non_alpha += word[0]
        word = word[1:]

    while len(word)>0 and not word[-1].isalpha():
        suffix_non_alpha += word[-1]
        word = word[:-1]

    return prefix_non_alpha, word, suffix_non_alpha

print(translate_all(message))