# Assignment: Check your Knowledge on Errors
# Neha Rao



# Task 1 - Understanding Python Exceptions
print("\n----------- Task 1 -----------\n")

while(True):        # Infinite loop

    try:        # converts user input, performs division, & prints result
        userNum = int(input("Enter a number: "))        # Prompt for user input
        result = 100 / userNum

        print(f"100 divided by {userNum} is {result}")
        break
    except ZeroDivisionError:       # If causing a division by 0
        print("Oops! You cannot divide by zero.")
    except ValueError:      # If input is not a number
        print("Invalid input! Please enter a valid number.")



# Task 2 - Types of Exceptions
print("\n\n----------- Task 2 -----------\n")

try:        # Will raise a TypeError because trying to access index out of range
    shapes = ['circle', 'square', 'triangle', 'rectangle']
    shape = shapes[5]
except IndexError:
    print("IndexError occurred! List index out of range")


try:        # Will raise a TypeError because trying to access key that doesn't exist
    greeting = {"English": "Hello", "Spanish": "Hola", "French": "Bonjour"}
    print(greeting["Chinese"])
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")


try:        # Will raise TypeError because adding string & integer
    test = "hi" + 5
except TypeError:
    print("TypeError occurred! Unsupported operand types.")



# Task 3 - Using try...except...else...finally
print("\n\n----------- Task 3 -----------\n")

try:        # Prompting user to enter 2 numbers & try to convert inputs to integers & divide
    userNum1 = int(input("Enter the first number: "))
    userNum2 = int(input("Enter the second number: "))

    result = userNum1 / userNum2
except ZeroDivisionError:     # If dividing by 0
    print("You cannot divide by zero.")
except ValueError:     # If not int
    print("Invalid input! Please enter valid numbers.") 
else:       # If no exception occurs, print the result
    print(f"The result is {result}")
finally:        # This block will always be executed
    print("This block always executes.")

