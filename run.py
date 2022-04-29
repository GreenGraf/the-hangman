import os
import random

import words
from man_art import logo, stages


def clear_console():
    """
    Clears console
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def game_rules():

    """
    Function for the rules section of the game
    """

    print('====================================')
    print()
    print('                 RULES:')
    print()
    print('====================================')
    print('A secret word will be chosen at random.')
    print('You must try to guess what the word is, one letter at a time.')
    print('Guess a letter and press enter/return key.')
    print("You have six chances to survive the hangman's noose.")
    print()
    print("Would you like to try to beat the Hangman's noose?")
    play_now = input("Enter yes or no: ")
    if play_now.lower() == "yes":
        clear_console()
        play_game()

    elif play_now.lower() == 'no':
        clear_console()
        main()

    else:
        clear_console()
        print()
        print('  Invalid entry.')
        print("  Please enter 'yes' or 'no'.")
        print(' ***************')
        game_rules()


def play_game():
    """
    Core logic of the game —
    Check guessed letter. Prints correct letter in place and if lives = 0
    then print "You Lose" and end game.
    """
    chosen_word = random.choice(words.word_list)
    word_length = len(chosen_word)

    print(chosen_word)

    end_of_game = False
    lives = 6

    # Print ASCII Hangman
    print(stages[lives])

    # Create blank spaces for letter in random word
    display = []
    for _ in range(word_length):
        display += "_"
    
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print("")

    while not end_of_game:
        valid_word = True
        guess = input("Guess a letter: ").lower()
        clear_console()
        
        if not guess.isalpha():
            print("You did not enter a letter. Please try again.")
            valid_word = False

        if len(guess) > 1:
            print("You can't guess a whole word!")
            valid_word = False

        if guess in display:
            print(f"You've already guessed '{guess}'. Try again.")
            valid_word = False

        if valid_word:
            duplicate = False

            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
                    if not duplicate:
                        print(f"You guessed '{guess}' ... good guess.")
                        duplicate = True

            if guess not in chosen_word:
                print(f"You guessed '{guess}'. That's not in the word. You lose a life. HA HA HA!")
                lives -= 1
                if lives == 0:
                    end_of_game = True
                    print("You lose.")
                    # Print ASCII Hangman
                    print(stages[lives])
                    play_again()

    # Print ASCII Hangman
    print(stages[lives])

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print("")   

    # Check if user has guessed all letters.
    if "_" not in display:
        end_of_game = True
        print()
        print("You win!")
        play_again()


def play_again():
    """
    This function is to restart the game
    """
    print()
    print()
    print("Would you like to play again?")
    play_again = input(" Enter 'yes' or 'no': ")

    if play_again.lower() == "yes":
        clear_console()
        play_game()

    elif play_again.lower() == 'no':
        clear_console()

        print()
        print()
        print("  COWARD! HA HA HA!")
        print()
        print('  Come back soon ...')
        print()
        print('  ***************')
        print()

        quit()

    else:
        print()
        print('  Invalid entry.')
        print("  Please enter 'yes' or 'no'.")
        print('  ***************')


def main():
    """
    Print welcome screen and call functions
    """
    print(logo)
    print()
    print('====================================')
    print()
    print('     CAN YOU BEST THE HANGMAN?')
    print()
    print('====================================')
    print()

    print('Would you like to see the rules or play the game?')
    choice = input("Enter 'rules' or 'play': ")

    if choice.lower() == "rules":
        clear_console()
        game_rules()

    elif choice.lower() == "play":
        clear_console()
        play_game()

    else:
        clear_console()
        print(logo)
        print()
        print('  Invalid entry.')
        print("  Please enter 'rules' or 'play'")
        print('  ***************')
        main()


if __name__ == '__main__':
    main()
