import re



text = 'Awesome, I am doing the #100DaysOfCode challenge'

test_1 = re.search(r'I am', text)
test_2 = re.match(r'I am', text)
test_3 = re.match(r'Awesome.*challenge', text)

hundred = 'Awesome, I am doing the #100DaysOfCode challenge'
two_hundred = 'Awesome, I am doing the #200DaysOfCode challenge'

test_4 = re.match(r'.*(#\d+DaysOfCode).*', hundred)
test_5 = test_4.groups()[0]
test_6 = re.search(r'(#\d+DaysOfCode)', two_hundred)
test_7 = test_6.groups()[0]

text = '''
$ python module_index.py |grep ^re
re                 | stdlib | 005, 007, 009, 015, 021, 022, 068, 080, 081, 086, 095
'''

test_8 = re.findall(r'\d+', text)


movies = '''1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)'''.split('\n')

pat = re.compile(r'''
                  ^             # start of string
                  \d+           # one or more digits
                  \.            # a literal dot
                  \s+           # one or more spaces
                  (?:           # non-capturing parenthesis, so I don't want store this match in groups()
                  [A-Za-z']+\s  # character class (note inclusion of ' for "Schindler's"), followed by a space
                  )             # closing of non-capturing parenthesis
                  {2}           # exactly 2 of the previously grouped subpattern
                  \(            # literal opening parenthesis
                  \d{4}         # exactly 4 digits (year)
                  \)            # literal closing parenthesis
                  $             # end of string
                  ''', re.VERBOSE)
for movie in movies:
    print(movie, pat.match(movie))