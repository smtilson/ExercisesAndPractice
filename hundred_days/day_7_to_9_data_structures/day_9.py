import pytest

us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ',
                   'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                   'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
                   'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                   'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                   'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                   'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                   'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                   'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
                   'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                   'New Mexico': 'NM', 'New York': 'NY',
                   'North Carolina': 'NC', 'North Dakota': 'ND',
                   'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
                   'Pennsylvania': 'PA', 'Rhode Island': 'RI',
                   'South Carolina': 'SC', 'South Dakota': 'SD',
                   'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
                   'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                   'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

states = ['Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon',
          'Mississippi', 'Minnesota', 'Colorado', 'Alabama',
          'Massachusetts', 'Arizona', 'Connecticut', 'Montana',
          'West Virginia', 'Nebraska', 'New York', 'Nevada', 'Idaho',
          'New Jersey', 'Missouri', 'South Carolina', 'Pennsylvania',
          'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
          'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky',
          'Virginia', 'Ohio', 'Wisconsin', 'Maryland', 'Florida',
          'Utah', 'Maine', 'California', 'Vermont', 'Arkansas', 'Wyoming',
          'Louisiana', 'North Dakota', 'South Dakota', 'Texas',
          'Illinois', 'Iowa', 'Michigan', 'Delaware']

NOT_FOUND = 'N/A'


def get_every_nth_state(states=states, n=10):
    new_list = []
    for i in range(len(states)// n):
        new_list.append(states[(i+1)*n-1])
    return new_list

def get_state_abbrev(state_name, us_state_abbrev=us_state_abbrev):
    return us_state_abbrev.get(state_name, NOT_FOUND)

def get_longest_state(data):
    longest = ''
    for state in data:
        if len(longest)<= len(state):
            longest = state
        else:
            continue
    return longest


def combine_state_names_and_abbreviations(us_state_abbrev=us_state_abbrev,
                                          states=states):
    new_list_1 = []
    new_list_2 = []
    states.sort()
    print(states)
    states_copy = states.copy()
    for i in range(10):
        new_list_1.append(us_state_abbrev[states[i]])
        new_list_2.append(states_copy.pop())
    new_list_2.reverse()
    new_list_1.sort()
    return new_list_1+new_list_2

def test_get_every_nth_state():
    expected = ['Massachusetts', 'Missouri', 'Hawaii',
                'Vermont', 'Delaware']
    assert list(get_every_nth_state()) == expected
    expected = ['Missouri', 'Vermont']
    assert list(get_every_nth_state(n=20)) == expected


def test_get_state_abbrev():
    assert get_state_abbrev('Illinois') == 'IL'
    assert get_state_abbrev('North Dakota') == 'ND'
    assert get_state_abbrev('bogus') == NOT_FOUND


def test_get_longest_state():
    # depending the direction of the sort (reversed or not)
    # both North and South Carolina are correct
    possible_answers = ('North Carolina', 'South Carolina')
    assert get_longest_state(us_state_abbrev) in possible_answers
    assert get_longest_state(states) in possible_answers


def test_combine_state_names_and_abbreviations():
    expected = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                'South Dakota', 'Tennessee', 'Texas', 'Utah',
                'Vermont', 'Virginia', 'Washington', 'West Virginia',
                'Wisconsin', 'Wyoming']
    assert combine_state_names_and_abbreviations() == expected