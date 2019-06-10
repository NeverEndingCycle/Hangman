from hangman import *

if __name__ == '__main__':
    startup = False
    if startup == True:
        startup.show_welcome_screen()
        startup.start()

    while True:
        difficulty = main.get_dif()
        word = main.fetch_word(difficulty)
        print(word)
