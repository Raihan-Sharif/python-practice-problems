
def guessing_game():
    secret_number = 6  # The number to guess
    guess = int(input("Guess a number between 1 and 9: "))  # Get user input

    if guess < secret_number:
        print("Your guess is almost there.")
    elif guess > secret_number:
        print("Your guess is higher.")
    else:
        print("Your Guess Is Correct!")
        
# Example of usage
guessing_game()
