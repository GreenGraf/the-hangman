import random
import man_art
import words
import os


#clears console after each guess
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

from man_art import logo, stages
print(logo)


def play_game():
    chosen_word = random.choice(words.word_list)
    word_length = len(chosen_word)
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

        if not guess.isalpha():
            print("You did not enter a letter. Please try again by entering a letter.")
            continue

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
                play_again()

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Check if user has guessed all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
            play_again()

        #Print ASCII Hangman 
        print(stages[lives])

def play_again():
    """
    This function is to restart the game
    """
    print()
    print()
    print("Would you like to play again?")
    play_again = input(" Enter y or n: ")

    if play_again.lower() == "y":
        clearConsole()
        play_game()

    
    elif play_again.lower() == 'n':
        clearConsole()

        print()
        print()
        print("COWARD! HA HA HA!")
        print() 
        print('  Come back soon ...')
        print()
        print('***************')
        print()

        quit()

    else:
        print()
        print('  Invalid entry.')
        print("  Please enter 'y' or 'n'.")
        print('***************')

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