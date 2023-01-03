import time
from enum import Enum
import numpy as np

class Choices(Enum):
    PAPER = 0
    ROCK = 1
    SCISSORS = 2
    
    def __or__(self, other):
        if self.value == other.value: # if the choices are the same
            return None, f'Draw : {self.name} == {other.name}'

        elif self.value == (other.value - 1) % 3: # if self.value is one less than other.value
            return self.value, f'Winner : {self.name} Loser: {other.name}'

        else: # self.value must come after other.value
            return other.value, f'Winner : {other.name} Loser: {self.name}'

def main():
    rng = np.random.default_rng()
    consent = input('Would you like to play rock paper scissors? (yes/no)')
    print('Please choose from the following options...')
    while consent.lower().startswith('y'):
        try:
            player_digit = int(input('Paper : 0, Rock : 1, Scissors : 2'))
        except ValueError as exc:
            print('Please enter the corresponding integer')
            continue
        player_choice = Choices(player_digit)
        computers_choice = Choices(rng.integers(3))
        winner_digit, text = player_choice | computers_choice
        if player_digit == winner_digit:
            print('Congratulations, you win!')
        print(text)
        time.sleep(0.3)
        consent = input('Would you like to play again? (yes/no)')
    
    print('Thanks for playing')

if __name__ == '__main__':
    main()