from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return(mylist)

example = [' ', 'O', ' ']
shuffled_sample = shuffle_list(example)

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick a number: 0, 1 or 2: ')
        if guess not in ['0','1', '2']:
            print(f'The selected guess : {guess} is not in the available menu')
    return int(guess)

# player_guess()

def check_guess(example, guess):
    if example[guess] == 'O':
        print('Correct')
        print(example)
    else:
        print('Oh, that was wrong')
        print(example)

guess = player_guess()
check_guess(shuffled_sample, guess)
