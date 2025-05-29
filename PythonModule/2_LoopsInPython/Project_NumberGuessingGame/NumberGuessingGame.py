# Project: Number Guessing Game
# Neha Rao


import random       # Importing the random module to generate random numbers


number_to_guess = random.randint(1, 100)        # Generating a random number between 1 and 100
numOfAttempts = 0       # Initializing the number of attempts to 0

userGuess = input("Guess the number (between 1 and 100): ")     # Getting the user's guess


while int(userGuess) != number_to_guess:        # While the user's guess is not equal to the number_to_guess
    numOfAttempts += 1      # Incrementing the number of attempts by 1

    if int(userGuess) > number_to_guess:        # If the user's guess is greater than the number_to_guess
        print("Too high! Try again.")
    else:       # If the user's guess is less than the number_to_guess
        print("Too low! Try again.")

    if numOfAttempts > 9:       # If the number of attempts is greater than 9
        break

    userGuess = input("Guess the number (between 1 and 100): ")     # Getting the user's guess again


# Printing result
if int(userGuess) == number_to_guess:       # If the number of attempts is not greater than 9 & is correct
    numOfAttempts += 1      # Incrementing the number of attempts by 1
    print (f"Congratulations! You guessed it in {numOfAttempts} attempts! 🏆\n")        # Printing the number of attempts
else:
    print("Game over! Better luck next time! 👾\n")        # Printing the game over message if didn't get in 10 attempts