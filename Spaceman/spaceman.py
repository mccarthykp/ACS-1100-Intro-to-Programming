import random
import os

running = True
letters_guessed = []

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(current_word):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        current_word: string of current correctly guessed letters

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''

    for letter in current_word:
        if letter == '_':
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Returns: 
        string: letters and underscores.
    '''
    guessed_word = ''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    
    # set_intersection = set(letters_guessed).intersection(set(secret_word))

    # print(f'{set_intersection}')

    
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''

    # number of guesses when starting game
    num_guesses = 7

    # checks if letter guess is in secret_word
    if guess.lower() in secret_word or guess.upper() in secret_word:
        return True
    else:
        num_guesses -= 1
        return False

    
def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    # print(secret_word)
    

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    player_input = input('Enter a letter: ')
    os.system('clear')
    if player_input.isalpha():
        if len(player_input) > 1 or len(player_input) <= 0:
            player_input = input('Please enter one letter: ')

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    if is_guess_in_word(player_input, secret_word):
        letters_guessed.append(player_input)
        print('Nice! You\'ve guessed a letter correctly.')
    else:
        print('Guess is not in the secret word. Try again.')

    #TODO: show the guessed word so far
    current_guessed_word = get_guessed_word(secret_word, letters_guessed)
    print(current_guessed_word)
    return current_guessed_word
    


# Start game
secret_word = load_word()

while running:
    print('\nWelcome to Spaceman!\n\nA word has been chosen . . .\nTo find this word, guess its letters!\n\n')

    if is_word_guessed(spaceman(secret_word)):
        running = False