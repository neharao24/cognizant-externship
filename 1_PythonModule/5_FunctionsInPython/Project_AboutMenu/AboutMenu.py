# Project: Password Strength Checker
# Neha Rao

import turtle


# Functions availble in the menu

def factorial(n):       # Function to calculate the factorial of a number
    if n == 0 or n == 1:        # Base case
        return 1
    return n * factorial(n - 1)     # Recursive call


def fibonacci(n):       # Function to calculate the nth Fibonacci number
    if n <= 0:      # Base case
        return 0
    elif n == 1:        # Base case
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)      # Recursive call


def patternHelper(length, level):       # Helper function to draw a fractal "snowflake arm"
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        patternHelper(length, level - 1)
        turtle.left(60)
        patternHelper(length, level - 1)
        turtle.right(120)
        patternHelper(length, level - 1)
        turtle.left(60)
        patternHelper(length, level - 1)

def fractalPattern():       # Main function to draw fractal pattern (snowflake)
    # Setup turtle
    turtle.speed(100)  # Fastest speed
    turtle.bgcolor("lightblue")
    turtle.color("white")

    # Starting position
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()

    # Draw 3 sides of snowflake
    for _ in range(3):
        patternHelper(300, 2)  # (length, recursion depth)
        turtle.right(120)

    # Finish
    turtle.hideturtle()
    turtle.done()


def inputValidation(input):     # Function for validating input
    if not input.isdigit():     # Check if the input is a digit
        print("Invalid input. Please enter a digit.")
        return False
    elif not int(input) >= 0:       # Check if the input is positive
        print("Invalid input. Please enter a positive digit.")
        return False
    else:       # Otherwise is valid
        return True




# Main Loop - loops until user chooses to exit

print("\nWelcome to the Recursive Artistry Program!")
while True:
    print("Select an option:")
    print("1. Calculate the factorial of a number.")
    print("2. Find the nth Fibonacci number.")
    print("3. Draw a recursive fractal pattern (bonus).")
    print("4. Exit")
    userChoice = input("Enter your choice: ")
    print("\n")



    if userChoice == "1":       # Calculate the factorial of a number
        userInput = input("Enter a number to find its factorial: ")
        if inputValidation(userInput):      # If the input is valid, factorial is calculated
            inputNum = int(userInput)
            resultingFactorial = factorial(inputNum)
            print(f"The factorial of {userInput} is {resultingFactorial}.")


    elif userChoice == "2":     # Find the nth Fibonacci number
        userInput = input("Enter the position of the Fibonacci number: ")
        if inputValidation(userInput):      # If the input is valid, fibonacci number is calculated
            inputNum = int(userInput)
            resultingFibonacci = fibonacci(inputNum)
            print(f"The {userInput}th Fibonacci number is {resultingFibonacci}.")


    elif userChoice == "3":     # Draw a recursive fractal pattern
        print("Snowflake drawing diplayed!")
        print("Close drawing tab to return to menu.\n")
        fractalPattern()
        continue
        

    elif userChoice == "4":     # Exit
        print("Exiting program...")

        break

    else:       # Invalid choice
        print("\nInvalid choice. Please try again.")
    

    print("\n\n")


print("Thank you for using the Recursive Artistry Program! 👋")

