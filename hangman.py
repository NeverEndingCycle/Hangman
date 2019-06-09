from random import choice
from time import sleep as slp
from os import system as sys

class HangMan:
    def show_welcome_screen():
        splash = ['+===============+','|               |','|    Hangman    |','|      by:      |','|     N.E.C.    |','|               |','+===============+']
        for text in splash:
            print(text)
            slp(.3)
        slp(2.7)
        sys('cls')

    def start():
        print('Welcome, to hangman by N.E.C and Decoy.', end='\n\n>>> Press enter to continue.')
        pause = input()

    def fetch_word():
        while True:
            with open('hangman_data/word_list', 'r') as list_file:
                word_list = list_file.readlines()
            word = choice(word_list)
            word = ''.join(word.split())
            return word
