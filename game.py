"""
Number Guessing Game
--------------------
A simple command-line interface (CLI) game built with Python where the user 
tries to guess a randomly generated number between 1 and 100 within a limited 
number of attempts.
"""


import random

def play_game():
    """
    Main function to run the number guessing game loop, handle user input,
    perform range validation, and track attempts.
    """

    min_num=1
    max_num=100
    max_attempts=5

    # Generate a random secret number for the player to guess
    secret_number = random.randint(min_num,max_num)

    attempts = 0
 
    print("-"*50)
    print("Welcome to NUMBER GUESSING GAME!\nI have a number between 1 and 100 in mind. Guess the secret number.")
    print("-"*50)

    # Main game loop runs until the player uses up all allowed attempts
    while(attempts<max_attempts):

        # Handle non-integer entries
        try:
            number=int(input("Enter your guess:"))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Validate that the number falls within the limits
        if number<min_num or number>max_num:
            print(f"Out of range! Please guess a number between {min_num} and {max_num}.\n")
            continue
        
        # Increment attempt counter
        attempts+=1

        # Compare user guess number with the secret number
        if number<secret_number:
            print("Too low!Try a higher number.")
        elif number>secret_number:
            print("Too high!Try a lower number.")
        else:
            print(f"Correct!. You won in {attempts} attempts!")
            break

        print(f"Remaining attempts:{max_attempts-attempts}\n")

    else:   
        print("\nGame Over !! Your attempts are over!!")
        print("The secret number was: ",secret_number)

# Entry point of the script execution
if __name__ == "__main__":
    play_game()