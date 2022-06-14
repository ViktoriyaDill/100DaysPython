import pandas
# import os
#
# print(os.getcwd())
# exit()

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

# string = True
# while string:


def generate():
    word = input("Write a word: ")
    try:
        # word_list = list(word)
        word_code = [nato_dict[key.upper()] for key in word]
        # string = False
    except KeyError:
        print("Sorry, you can entry only letters")
        generate()
    else:
        print(word_code)


generate()



