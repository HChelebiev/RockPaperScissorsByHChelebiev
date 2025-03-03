import random


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')

if player_move == 'r':
    player_move = rock
    print(f"My move is: {rock}")
elif player_move == 'p':
    player_move = paper
    print(f"My move is: {paper}")
elif player_move == 's':
    player_move = scissors
    print(f"My move is: {scissors}")
else:
    raise SystemExit("Invalid input. Try again ...")

computer_random_number = random.randint(1, 3)
computer_move = ""

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors
print(f"Computer move is: {computer_move}")
if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    prGreen("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    prRed("You lose!")
