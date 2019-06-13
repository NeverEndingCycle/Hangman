from random import choice
from time import sleep as slp
from os import system as sys

class startup:
    def show_welcome_screen():
        splash = [
                '+===============+',
                '|               |',
                '|    Welcome    |',
                '|      to:      |',
                '|    Hangman    |',
                '|               |',
                '+===============+'
                ]
        for text in splash:
            print(text)
            slp(.5)
        slp(1.5)
        sys('cls')
        print('Welcome to hangman. By: N.E.C and Decoy.', end='\n\n>>> Press enter to continue.')
        pause = input()
        sys('cls')

class function:
    def get_dif():
        print('Please choose your difficulty.\n\n', end='')
        slp(.5)
        print('Easy:   (5-6 letter words)\n', end='')
        slp(.5)
        print('Normal: (7-8 letter words)\n', end='')
        slp(.5)
        print('Hard:   (9+ letter words)\n', end='')
        slp(.5)
        print('')
        slp(.5)
        print('\n[Easy, Normal, Hard]', end='\n>>> ')
        while True:
            diff = input()
            diff = diff.lower()
            if diff != 'easy' and diff != 'normal' and diff != 'hard':
                print('Invalid choice.')
                print('\n>>> ', end='')
            else:
                break
        sys('cls')
        return diff

    def fetch_word(difficulty):
        if difficulty == 'easy':
            while True:
                with open('hangman_data/easy', 'r') as list_file:
                    word_list = list_file.readlines()
                word = choice(word_list)
                word = ''.join(word.split())
                return word
        elif difficulty == 'normal':
            while True:
                with open('hangman_data/norm', 'r') as list_file:
                    word_list = list_file.readlines()
                word = choice(word_list)
                word = ''.join(word.split())
                return word
        elif difficulty == 'hard':
            while True:
                with open('hangman_data/hard', 'r') as list_file:
                    word_list = list_file.readlines()
                word = choice(word_list)
                word = ''.join(word.split())
                return word

    def get_globals(word):
        global char_list, word_print
        char_list = list(word)

        length = function.get_length(word)
        word_print = list(length)

    def picture(bad_guesses):
        bad_guesses = str(bad_guesses)
        with open(f'hangman_data/hangman({bad_guesses})', 'r') as file:
            picture = file.readlines()
        return picture

    def get_length(word):
        length = len(word)
        letter_length = ''

        while length != 0:
            length -= 1
            letter_length += '_'

        return letter_length

    def add_guess(bad_guesses):
        bad_guesses += 1
        return bad_guesses

    def check_guess(word, guess, bad_guesses):
        letter_length = function.get_length(word)
        char_index = None

        if guess in char_list:
            char_index = [i for i in range(len(char_list)) if char_list[i] == guess]
            for i in char_index:
                i = int(i)
                char_list[i] = '-'
                word_print[i] = guess

        elif guess == word:
            print('You win!')
        else:
            function.add_guess(bad_guesses)

        return bad_guesses, word_print

class game:
    def start(word):
        function.get_globals(word)
        bad_guesses = 0
        guess = None
        char_index = None
        word_print = None

        while True:
            for pic in function.picture(bad_guesses):
                print(pic, end='')

            print(word)

            if word_print == None:
                new_word_print = function.get_length(word)
                print(f'{new_word_print}')
            else:
                new_word_print = ''
                for i in word_print:
                    new_word_print += i
                print(f'{new_word_print}')

            guess = input('\n\nGuess a letter or word.\n>>> ')
            guess = guess.lower()

            bad_guesses, word_print = function.check_guess(word, guess, bad_guesses)
            sys('cls')
