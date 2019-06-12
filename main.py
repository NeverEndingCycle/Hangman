from hangman import *

if __name__ == '__main__':
    startup = False
    if startup == True:
        startup.welcome()

    while True:
        difficulty = function.get_dif()
        word = function.fetch_word(difficulty)
        game.start(word)
        exit()
