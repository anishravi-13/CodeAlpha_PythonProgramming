import random

def get_hangman_art(mistakes):
    stages = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        ---------
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        ---------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |     
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
        ---------
        """
    ]
    return stages[mistakes]

def play_hangman():
    # 5 Predefined words as required by the specification
    words = ["PYTHON", "PROGRAMMING", "DEVELOPER", "ALGORITHM", "CODING"]
    secret_word = random.choice(words)
    
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("=" * 45)
    print("        WELCOME TO HANGMAN GAME")
    print("=" * 45)
    print(f"Guess the word! You are allowed {max_incorrect} incorrect guesses.")

    while incorrect_guesses < max_incorrect:
        print(get_hangman_art(incorrect_guesses))
        
        # Display word progress (e.g. P _ T _ O N)
        display_word = [char if char in guessed_letters else "_" for char in secret_word]
        print("Word: " + " ".join(display_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining attempts: {max_incorrect - incorrect_guesses}")
        print("-" * 45)

        # Check win condition
        if "_" not in display_word:
            print(f"\n CONGRATULATIONS! You guessed the word correctly: {secret_word}\n")
            return

        guess = input("Enter a letter: ").strip().upper()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print(">> Invalid input. Please enter a single alphabetic letter.\n")
            continue

        if guess in guessed_letters:
            print(f">> You already guessed '{guess}'. Try another letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f">> Good job! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f">> Sorry! '{guess}' is not in the word.\n")

    # If loop ends, user ran out of guesses
    print(get_hangman_art(max_incorrect))
    print(f" GAME OVER! You ran out of attempts.")
    print(f"The correct word was: {secret_word}\n")

if __name__ == "__main__":
    while True:
        play_hangman()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again not in ["y", "yes"]:
            print("Thanks for playing Hangman! Goodbye.")
            break
