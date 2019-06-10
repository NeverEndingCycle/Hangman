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
    def start():
        print('Welcome to hangman. By: N.E.C and Decoy.', end='\n\n>>> Press enter to continue.')
        pause = input()
        sys('cls')

class main:
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

    
