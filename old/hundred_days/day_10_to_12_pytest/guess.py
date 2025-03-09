import random

max_guesses= 5

start, end = 1, 20

def get_random_number():
    return random.randint(start, end)


class Game:

    def __init__(self):
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        guess = input(f'Guess a number between {start} and {end}.')
        if not guess:
            raise ValueError('Please enter a number.')
        try:
            guess = int(guess)
        except:
            raise ValueError('The guess should be a whole number.')

        if guess not in range(start, end+1):
            raise ValueError(f'The number must be between {start} and {end} (inclusive).')

        if guess in self._guesses:
            raise ValueError('This was already guessed.')

        self._guesses.add(guess)
        #print(f'Your guess was {guess}.')
        return guess

    def _validate_guess(self, guess):
        if guess == self._answer:
            print(f'That is correct! I was thinking of {self._answer}')
            return True
        else:
            high_or_low = 'low' if guess< self._answer else 'high'
            print(f'{guess} was {high_or_low}.')
            return False

    @property
    def num_of_guesses(self):
        return len(self._guesses)

    def __call__(self):
        while len(self._guesses)< max_guesses:
            try:
                guess = self.guess()
            except ValueError as ve:
                print(ve)
                continue
            win = self._validate_guess(guess)
            if win:
                guess_str = self.num_of_guesses == 1 and "guess" or "guesses"
                print(f'It took you {self.num_of_guesses} {guess_str}.')
                self._win = True
                break
        else:
            print(f'You guessed {max_guesses} times, the correct answer was {self._answer}.')

if __name__ == '__main__':
    game = Game()
    game()