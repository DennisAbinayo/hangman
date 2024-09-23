from theme_list import Themes
import random
import time


def select_theme():
    print(f"\nChoose a theme: ({', '.join(Themes.keys())})")
    time.sleep(1)
    selected_theme = input("\nEnter the theme: ").lower()
    
    while True:
        if selected_theme not in Themes:
            print("Invalid theme. Try again.")
            selected_theme = input("\nEnter the theme: ").lower()
        else:
            break

    print("\n")
    return selected_theme


def hangman():
    print("\nWelcome to the hangman game!".upper())
    time.sleep(1)
    selected_theme = select_theme()
    
    word = random.choice(Themes[selected_theme])
    guessed_letters = []
    attempts = 6
    guessed_word = ["_"] * len(word)

    while attempts > 0:
        print("\nCurrent word: " + " ".join(guessed_word))
        print("Guessed letters: " + ",".join(guessed_letters))
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha() :
            print("Invalid guess. Try again.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess. Attempts left: {attempts}")

        if "_" not in guessed_word:
            print("\nCongratulations".upper())
            print(f"You've guessed the word: {word}")
            return

        if attempts == 0:
            print("\nGame over".upper())
            
    print(f"You lost! The word was: {word}")


hangman()
