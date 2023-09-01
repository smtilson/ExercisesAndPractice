import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    for participant in zip(names, locations+cycle, confirmed+cycle):
        print(participant)

dictionary = ['gilt','zonar','apio', 'peai','boce','garvey']


def get_possible_dict_words(draw):
    actual_words = []
    for word in _get_permutations_draw(draw):
        if word.lower() in dictionary:
            actual_words.append(word)
        else:
            continue
    return actual_words
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""

def _get_permutations_draw(draw):
    possibilities = []
    draw = ''.join(draw)
    print(draw)
    for i in range(len(draw)):
        #print([''.join(perm) for perm in list(itertools.permutations(draw, i))])
        possibilities.extend([''.join(perm) for perm in list(itertools.permutations(draw, i+1))])
    #print(possibilities)
    return possibilities


samples = [('T, I, I, G, T, T, L', 'gilt'),
    ('O, N, V, R, A, Z, H', 'zonar'),
    ('E, P, A, E, I, O, A', ('apio', 'peai')),
    ('B, R, C, O, O, E, O', 'boce'),
    ('G, A, R, Y, T, E, V', 'garvey'),
]

if __name__ == '__main__':
    tests = ['T, I, I, G, T, T, L',
        'O, N, V, R, A, Z, H',
        'E, P, A, E, I, O, A',
        'B, R, C, O, O, E, O',
        'G, A, R, Y, T, E, V']
    for test in tests:

        draw = test.split(', ')
        samples = _get_permutations_draw(draw)
        print(max(samples), len(samples))
        print()
        print(get_possible_dict_words(draw))