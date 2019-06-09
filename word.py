from random import choice

class Word:
    def get():
        while True:
            with open('hangman_data/word_list', 'r') as list_file:
                word_list = list_file.readlines()
            word = choice(word_list)
            word = ''.join(word.split())
            return word
