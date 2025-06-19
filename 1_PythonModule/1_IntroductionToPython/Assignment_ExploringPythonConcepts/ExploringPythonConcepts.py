# Assignment: Exploring Python Concepts
# Neha Rao


# Task 1 - Variables: Your First Python Intro
print("\n----------- Task 1 -----------\n")

name = "Neha"
age = 21
height = 5

# Printing greeting with the appropriate variables
print(f"Hi! Nice to meet you, my name is {name}. I am {age} years old and my height is {height} feet.")



# Task 2 - Operators: Playing with Numbers
print("\n\n----------- Task 2 -----------\n")

# Initializing the variables
num1 = 12
num2 = 24

# Printing the results
print("The sum of 12 and 24 is", num1 + num2)       # Prints the result of num1 + num2
print("The difference of 12 and 24 is" , num1 - num2)       # Prints the result of num1 - num2
print("The product of 12 and 24 is", num1 * num2)       # Prints the result of num1 * num2
print("The quotient of 12 and 24 is", num1 / num2)       # Prints the result of num1 / num2



# Task 3 - Conditional Statements: The Number Checker
print("\n\n----------- Task 3 -----------\n")

userNum = input("Please enter a number: ")      # Getting user input

# Checking the number & printing the result
if int(userNum) > 0:     # Checking if the number is greater than 0
    print("This number is positive. Awesome!\n")
elif int(userNum) == 0:      # Checking if the number is equal to 0
    print("Zero it is. A perfect balance!\n")
else:       # If the number is less than 0
    print("This number is negative. Better luck next time!\n")


