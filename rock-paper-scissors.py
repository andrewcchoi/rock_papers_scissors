"""
rock-paper-scissors
"""

import random

def rock_paper_scissors():
    def show_winner(user_throw, my_throw):
        
        if user_throw.lower() == my_throw.lower():
            winner = 'its a tie'
        
        elif user_throw.lower() == 'rock': 
            if my_throw.lower() == 'paper':
                winner = 'i win'
            elif my_throw.lower() == 'scissors':
                winner = 'you win'
        
        elif user_throw.lower() == 'paper':
            if my_throw.lower() == 'rock':
                winner = 'i win'
            elif my_throw.lower() == 'scissors':
                winner = 'you win'
        
        elif user_throw.lower() == 'scissors':
            if my_throw.lower() == 'rock':
                winner = 'i win'
            elif my_throw.lower() == 'paper':
                winner = 'you win'
        
        return f'\n{winner}! you threw {user_throw} and I threw {my_throw}'


    throws = ['rock', 'paper', 'scissors']

    while True:
        user_throw = input('make a throw\n\trock, paper, or scissors: ')
        my_throw = random.choice(throws)

        if user_throw in throws:
            winner = show_winner(user_throw=user_throw, my_throw=my_throw)
            print(winner)   
        else:
            print(f'{user_throw} is not a valid throw.')

        play = input('\nwould you like to continue playing? (y/n)')
        if play.lower() == 'n':
            break

    print('\nthank you for playing! let\'s play again soon!')


if __name__ == '__main__':
    rock_paper_scissors()
