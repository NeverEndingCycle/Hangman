from random import choice
from time import sleep as slp
from os import system as sys

class startup:
    def welcome():
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
        print('Welcome to hangman. By: NeverEndingCycle.', end='\n\n>>> Press enter to continue.')
        pause = input()
        sys('cls')

class function:
    def fetch_word(difficulty):
        if difficulty == 'easy':
            with open('hangman_data/easy', 'r') as list_file:
                word_list = list_file.readlines()
            word = choice(word_list)
            word = ''.join(word.split())
            return word
        elif difficulty == 'normal':
            with open('hangman_data/norm', 'r') as list_file:
                word_list = list_file.readlines()
            word = choice(word_list)
            word = ''.join(word.split())
            return word
        elif difficulty == 'hard':
            with open('hangman_data/hard', 'r') as list_file:
                word_list = list_file.readlines()
            word = choice(word_list)
            word = ''.join(word.split())
            return word

    def get_globals(word):
        global char_list, word_print, guessed
        char_list = list(word)

        length = function.get_length(word)
        word_print = list(length)

        guessed = []

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

    def validate_guess(guess):
        invalid = False
        if guess in guessed:
            invalid = 'already guessed'

        elif guess == '' or not guess.isalpha():
            invalid = True

        else:
            guessed.append(guess)
        return invalid

    def check_guess(word, guess, bad_guesses):
        letter_length = function.get_length(word)
        char_index = None
        victory = None

        if guess in char_list:
            char_index = [i for i in range(len(char_list)) if char_list[i] == guess]
            for i in char_index:
                i = int(i)
                char_list[i] = '-'
                word_print[i] = guess

        elif guess == word:
            victory = True

        else:
            bad_guesses = function.add_guess(bad_guesses)

        return bad_guesses, word_print, victory

class game:
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
            dif = input()
            dif = dif.lower()
            if dif != 'easy' and dif != 'normal' and dif != 'hard':
                print('Invalid choice.', end='')
                print('\n>>> ', end='')
            else:
                break
        sys('cls')
        return dif

    def start(dif):
        word = function.fetch_word(dif)
        function.get_globals(word)
        victory = None
        bad_guesses = 0
        guess = None
        char_index = None
        word_print = None
        new_word_print = None
        invalid = True

        while True:
            for pic in function.picture(bad_guesses):
                print(pic, end='')

            if bad_guesses == 7:
                victory = False
                return word, victory

            elif victory == True:
                return word, victory

            if word_print == None:
                new_word_print = function.get_length(word)
            else:
                new_word_print = ''
                for i in word_print:
                    new_word_print += i

            if new_word_print == word:
                victory = True
                return word, victory
            else:
                print(f'{new_word_print}')

            while True:
                guess = input('\n\nGuess a letter or word.\n>>> ')
                guess = guess.lower()

                invalid = function.validate_guess(guess)

                if invalid == True:
                    print('Invalid Answer.', end='')
                elif invalid == 'already guessed':
                    print("You can't guess the same answer twice.", end='')
                else:
                    bad_guesses, word_print, victory = function.check_guess(word, guess, bad_guesses)
                    break

            sys('cls')

    def cont(word, victory):
        if victory == True:
            print(f"\nCongradulations, you won!\n\nThe word was: '{word}'\n")
        elif victory == False:
            print(f"\nBummer, you lost!\n\nThe word was: '{word}'\n")
        while True:
            print("Would you like to play another match?")
            answer = input('\n[Yes, No]\n>>> ')
            answer = answer.lower()

            if answer == 'yes' or  answer == 'no':
                sys('cls')
                break
            else:
                print('Invalid Choice.\n')

        if answer == 'yes':
            cont = True
        elif answer == 'no':
            cont = False

        return cont
