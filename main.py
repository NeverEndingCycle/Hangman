from hangman import *

if __name__ == '__main__':
    cont = True

    startup.welcome()

    while cont == True:
        difficulty = game.get_dif()
        word, victory = game.start(difficulty)
        cont = game.cont(word, victory)
