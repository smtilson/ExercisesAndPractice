import random

class Player():
    def __init__(self, name):
        self.name = name
        self.wins = 0

class Roll():
    def __init__(self, name, defeats, defeated_by):
        self.name = name
        self.defeats = defeats
        self.defeated_by = defeated_by


def get_rolls():
    Rock = Roll('rock', {'scossprs'},{'paper'})
    Scissors = Roll('scissors', {'paper'},{'rock'})
    Paper = Roll('paper', {'rock'},{'scissors'})
    rolls = {'r':Rock, 'p':Paper, 's':Scissors}

    return rolls

def get_individual_roll(rolls):

    valid = False
    while not valid:
        roll = input('What do you throw? [r]ock, [p]aper, or [s]cissors?')
        if roll in rolls.keys():
            valid = True
            roll = rolls[roll]
        else:
            print('Please enter a valid throw.')
    return roll

def main():
    print_header()
    player, num = get_started()
    rolls = get_rolls()
    game_loop(player, num, rolls)

def print_header():
    print('-'*60)
    sample = 'Welcome to rock, paper, scissors!'
    buffer = (60-len(sample))//2
    print('*'*buffer+sample+'*'*buffer)
    print('-'*60)

def get_started():
    name = input('Please state your name.')
    num = input('Please input how many matches are needed to win.')
    num = int(num)
    player = Player(name)
    return player, num

def game_loop(player, num, rolls):
    computer = Player('computer')
    while max(player.wins, computer.wins)< num:
        computer_roll = rolls[random.choice(['r','s','p'])]
        player_roll = get_individual_roll(rolls)
        print(f'The computer threw a {computer_roll.name}.')
        print(f'You threw a {player_roll.name}.')
        if computer_roll.name in player_roll.defeats:
            player.wins+=1
            print(f"You win! You have {player.wins} wins, the computer has {computer.wins} wins.")
        elif computer_roll.name in player_roll.defeated_by:
            computer.wins+=1
            print(f"The computer won! You have {player.wins} wins, the computer has {computer.wins} wins.")
        else:
            print(f'You both threw a {computer_roll.name}, let\'s go again!')
    winner = 'the computer' if computer.wins== num else 'you'
    print(f'It looks like {winner} won.')

if __name__ == '__main__':
    main()