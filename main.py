import hangman

if __name__ == '__main__':
    welcome = False
    if welcome == True:
        hangman.show_welcome_screen()
    hangman.start()
    hangman.fetch_word()
