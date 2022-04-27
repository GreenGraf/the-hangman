word_list = ["python", "possum", "cat", "Container"]

import random

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Correct")
    else:
        print("Wrong")