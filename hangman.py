from random import choice
from time import sleep as slp
from os import system as sys

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
    print('Welcome, to hangman by N.E.C and Decoy.', end='\n\n>>> Press enter to continue.')
    pause = input()
    sys('cls')
    print('Please choose your difficulty.\n\n', end='')
    slp(.5)
    print('Easy: (3-5 letter words)\n', end='')
    slp(.5)
    print('Normal: (6-7 letter words)\n', end='')
    slp(.5)
    print('Hard: (8+ letter words)\n', end='')
    slp(.5)
    print('')
    slp(.5)
    print('\n[Easy, Normal, Hard]', end='\n>>> ')
    pause = input()
    sys('cls')

def fetch_word():
    while True:
        with open('hangman_data/word_list', 'r') as list_file:
            word_list = list_file.readlines()
        word = choice(word_list)
        word = ''.join(word.split())
        return word
