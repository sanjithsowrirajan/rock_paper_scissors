import random

player_score = 0
computer_score = 0

while True:
    choices = ['rock','paper','scissors']
    computer = random.choice(choices)  # computer chooses randomly
    player = ''
    while True:
        player = input('rock, paper, or scissors?: ').lower()
        if player == 'rock' or player == 'scissors' or player == 'paper': # player is stuck in loop until they enter valid input
            break
        print('invalid input\n')

    print(f'\ncomputer: {computer}') # prints computer and player choices
    print(f'player: {player}\n')
    # calculates outcome of the game and adds score
    if player == computer:
        print('tie')
    elif player == 'rock':
        if computer == 'scissors':
            print('you win')
            player_score += 1
        else:
            print('you lose')
            computer_score += 1
    elif player == 'paper':
        if computer == 'scissors':
            print('you lose')
            computer_score += 1
        else:
            print('you win')
            player_score += 1
    else:
        if computer == 'rock':
            print('you lose')
            computer_score += 1
        else:
            print('you win')
            player_score += 1

    print(f'\nyour score: {player_score}') # displays scores
    print(f'computer score: {computer_score}\n')

    play_again = input('play again? (y/n): ').lower() # player can choose to play again or not
    if play_again != 'y':
        break
print('bye')