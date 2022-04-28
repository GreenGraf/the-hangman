import random
import man_art
import words
import os


#clears console after each guess
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

from man_art import logo, stages, gallows 
print(logo)

def game_rules():
    print('====================================')
    print()
    print('                 RULES:')
    print()  
    print('====================================')
    print('  A secret word will be chosen at random.')   
    print('  You must try to guess what the word is, one letter at a time.')
    print('  Guess a letter and press enter/return key.')
    print("  You have six chances to survive the hangman's noose.")
    print()
    print("Would you like to try to beat the Hangman's noose?") 
    play_now = input("Enter yes or no: ")
    if play_now.lower() == "yes":
        clearConsole()
        play_game()

    
    elif play_now.lower() == 'no':
        clearConsole()
        main()

    else:
        clearConsole()
        print()
        print('  Invalid entry.')
        print("  Please enter 'yes' or 'no'.")
        print(' ***************')
        game_rules()

def play_game():
    chosen_word = random.choice(words.word_list)
    word_length = len(chosen_word)
    # print(gallows[stage])
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
            print(f"You've already guessed '{guess}'. Try again.")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                print(f"You guessed '{guess}' ... good guess.")
        
        if guess not in chosen_word:
            print(f"You guessed '{guess}'. Thant's not in the word. You lose a life. HA HA HA!")
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
            print(lives)
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
    play_again = input(" Enter 'yes' or 'no': ")

    if play_again.lower() == "yes":
        clearConsole()
        play_game()

    
    elif play_again.lower() == 'no':
        clearConsole()

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
        clearConsole()
        game_rules()
    
    elif choice.lower() == "play":
        clearConsole()
        play_game()

    else:
        clearConsole()
        print(logo)
        print()
        print('  Invalid entry.')
        print("  Please enter 'rules' or 'play'")
        print('  ***************')
        main()
        
main()