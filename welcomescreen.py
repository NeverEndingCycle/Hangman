from time import sleep as slp
from os import system as sys

class WelcomeScreen:
    def show():
        splash = ['+===============+','|               |','|    Hangman    |','|      by:      |','|     N.E.C.    |','|               |','+===============+']
        for text in splash:
            print(text)
            slp(.3)
        slp(2.7)
        sys('cls')
