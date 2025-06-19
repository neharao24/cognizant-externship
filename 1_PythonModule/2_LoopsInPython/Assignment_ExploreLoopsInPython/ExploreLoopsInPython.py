# Assignment: Explore Loops in Python
# Neha Rao


# Task 1 - Counting Down with Loops
print("\n----------- Task 1 -----------\n")

userNum = input("Enter the starting number: ")      # Getting user input

currNum = int(userNum)      # Casting user input to integer
while(currNum != 0):        # Loop will run until currNum is equal to 0
    print(currNum, end = " ")
    currNum -= 1

print("Blast off! 🚀")



# Task 2 - Multiplication Table with for Loops
print("\n\n----------- Task 2 -----------\n")

userNum = input("Enter the starting number: ")      # Getting user input

for i in range(1, 11):      # Loop will run from 1 to 10
    print(f"{userNum} x {i} = {int(userNum) * i}", end=" ")       # Printing multiplication table



# Task 3 - Find the Factorial
print("\n\n----------- Task 3 -----------\n")

userNum = input("Enter the starting number: ")      # Getting user input

currFactorial = 1
for i in range(int(userNum) - 1):       # Loop will run from 0 to userNum - 1
    currFactorial = int(userNum)**i     # Calculating factorial

print(f"The factorial of {userNum} is {str(currFactorial)}.\n")     # Printing the result

