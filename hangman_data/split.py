with open('word_list', 'r') as list_file:
    word_list = list_file.readlines()

for word in word_list:
    newword = word[:-1]
    print(newword)
    length = len(newword)
    if length < 4:
        word_list.remove(word)
print(word_list)
