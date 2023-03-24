import math 

guesses = 9
n = 30

while True:
    inp = int(input('Guess the number: '))
    if inp != 30:
        guesses -= 1
        print(f"Wrong guess! \nTry Again. {guesses} guesses left")
        if guesses == 0:
            print('Game Over')
            break
    else:
        print(f'You have guessed the correct number in {guesses} guesses')
        break