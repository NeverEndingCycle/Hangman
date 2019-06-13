easy=[]
norm=[]
hard=[]

with open('word_list', 'r') as word_list:
    word_list = word_list.readlines()

for word in word_list:
    newword = word[:-1]
    length = len(newword)

    if length in range(5, 7):
        easy.append(word)
        print(f'{word} appended to easy_list.')
    elif length in range(7, 10):
        norm.append(word)
        print(f'{word} appended to norm_list.')
    elif length >= 10:
        hard.append(word)
        print(f'{word} appended to hard_list.')
    else:
        print(f"ERROR: '{word}' failed to append to a list.")

with open('easy', 'w') as easy_file:
    for word in easy:
        easy_file.write(word)
        print(f'{word} appended to easy_file.')

with open('norm', 'w') as norm_file:
    for word in norm:
        norm_file.write(word)
        print(f'{word} appended to norm_file.')

with open('hard', 'w') as hard_file:
    for word in hard:
        hard_file.write(word)
        print(f'{word} appended to hard_file.')
