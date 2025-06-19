# Project: Calculator with Exception Handling
# Neha Rao


import logging   

# Create a logger
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(levelname)s:%(message)s')


def inputValidation():      # Function to validate user input

    while True:
        userInput1 = input("Enter the first number: ")
        userInput2 = input("Enter the second number: ")

        try:
            num1 = int(userInput1)
            num2 = int(userInput2)
            return num1, num2
        except ValueError as ve:
            print("Invalid input! Please enter a valid number.")
            logging.error(f"ValueError occurred: {ve}")



# Main loop  - until user chooses to exit
print("\nWelcome to the Error-Free Calculator!")
while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    userChoice = input("Enter your choice: ")
    print("\n")



    if userChoice == "1":       # Addition
        num1, num2 = inputValidation()      # Get two numbers from user

        try:        # Perform addition
            result = num1 + num2        
        except Exception as e:      # If error occurs, log it and continue
            print("An unexpected error occurred during addition.")
            logging.error(f"Addition error: {e}")
        else:       # Display result if no error
            print(f"{num1} + {num2} = {result}")        
        finally:        # Always print this message
            print("Addition operation attempted.\n")        


    elif userChoice == "2":         # Subtraction
        num1, num2 = inputValidation()      # Get two numbers from user

        try:        # Perform subtraction
            result = num1 - num2    
        except Exception as e:      # If error occurs, log it and continue
            print("An unexpected error occurred during subtraction.")
            logging.error(f"Subtraction error: {e}")
        else:       # Display result if no error
            print(f"{num1} - {num2} = {result}")
        finally:        # Always print this message
            print("Subtraction operation attempted.\n")


    elif userChoice == "3":     # Multiplication
        num1, num2 = inputValidation()      # Get two numbers from user

        try:        # Perform multiplication
            result = num1 * num2
        except Exception as e:      # If error occurs, log it and continue
            print("An unexpected error occurred during multiplication.")
            logging.error(f"Multiplication error: {e}")
        else:       # Display result if no error
            print(f"{num1} * {num2} = {result}")
        finally:        # Always print this message
            print("Multiplication operation attempted.\n")


    elif userChoice == "4":     # Division
        num1, num2 = inputValidation()      # Get two numbers from user

        try:        # Perform division
            result = num1 / num2
        except ZeroDivisionError as zde:        # Handle division by zero
            print("Error! Division by zero is not allowed.")
            logging.error(f"ZeroDivisionError occurred: {zde}")
        else:       # Display result if no error
            print(f"{num1} / {num2} = {result}")
        finally:        # Always print this message
            print("Division operation attempted.\n")


    elif userChoice == "5":     # Exit
        print("Exiting program...")
        break


    else:       # Invalid choice
        print("\nInvalid choice. Please try again.")
    


print("Thank you for using the Error-Free Calculator! Goodbye!👋")


