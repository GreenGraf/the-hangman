import random
import man_art
import words
import os

#clears console after each guess
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

from man_art import logo, stages
print(logo)


def play_game():
    #Testing code
    print(chosen_word)
    end_of_game = False
    lives = 6
    #Create blank spaces for letter in random word
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        
        clearConsole()

        """
        Check guessed letter. Prints correct letter in place and if lives = 0 
        then print "You Lose" and end game.
        """
        if guess in display:
            print(f"You've already guessed {letter}. Try again.")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                print("Good guess.")
        

        if guess not in chosen_word:
            print(f"You guessed {guess}. Thant's not in the word. You lose a life. HA HA HA!")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Check if user has guessed all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        #Print ASCII Hangman 
        print(stages[lives])

def main():
    """
    Print welcome screen and call functions
    """

    print()
    print('====================================')
    print()
    print('     CAN YOU BEST THE HANGMAN?')
    print()
    print('====================================')
    print()
    print('RULES:')
    print()
    print('Follow the prompts.')
    print('Guess a letter.')
    print("You have six chances to survive the hangman's noose.")
    print()
    print('******  GOOD LUCK  ******')
    print()
    print()

    play_game()

main()