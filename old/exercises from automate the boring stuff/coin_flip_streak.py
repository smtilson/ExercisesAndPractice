import random


def produce_flips(length):
    sequence=''
    for i in range(length):
        x = random.randint(0,1)
        if x==0:
            sequence+='T'
        else:
            sequence+='H'
    return sequence

def count_head_streak(length: int, string: str):
    heads = 'H'*length
    tally=0
    i=0
    while i+length < len(string)-length:
        if Heads == string[i: i+length]:
            tally+=1
            i+=1
        else:
            i+=1
            continue
    return tally

def count_tail_streak(length, string):
    tails = 'T' * length
    tally = 0
    i = 0
    while i + length < len(string) - length:
        if tails == string[i: i + length]:
            tally += 1
            i += 1
        else:
            i += 1
            continue
    return tally

def run_experiment(trials, length, streak):

    total_tails=0
    total_heads=0
    for i in range(trials):
        seq = produce_flips(length)
        tails = count_tail_streak(streak, seq)
        heads = count_tail_streak(streak, seq)
        total_tails+=tails
        total_heads+=heads
    print(f'We ran the experiment {trials} times for {length} flips and searching for streaks of length {streak}.')
    print(f'The average number of streaks of tails is {total_tails/length}')
    print(f'The average number of streaks of heads is {total_heads/length}')

for i in range(10):
    run_experiment(100+i*100, 200, i+2)


print('hello, did this run')