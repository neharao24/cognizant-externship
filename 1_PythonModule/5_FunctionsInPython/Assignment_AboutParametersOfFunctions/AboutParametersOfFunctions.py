# Assignment: About Parameters of Functions
# Neha Rao



# Task 1 - Writing Functions
print("\n----------- Task 1 -----------\n")

def greet_user(name):           # Function to greet a user
    print(f"Hi {name}, Nice to meet you!", end=" ")

def add_numbers(num1, num2):        # Function to add two numbers
    sum = num1 + num2
    return print(f"The sum of {num1} and {num2} is {sum}.")


# Example
greet_user("Alice")
add_numbers(5, 10)





# Task 2 - Using Default Parameters
print("\n\n----------- Task 2 -----------\n")

def describe_pet(pet_name, animal_type = 'dog'):        # Function to describe a pet
    print(f"I have a {animal_type} named {pet_name}.", end=" ")


# Example
describe_pet("Buddy")
describe_pet("Whiskers", "cat")




# Task 3 - Functions with Variable Arguments
print("\n\n----------- Task 3 -----------\n")

def make_sandwich(*ingredients):        # Function to make a sandwich
    print("Making a sandwich with the following ingredients:", end=" ")
    for item in ingredients:        # Loop through the ingredients
        print(f"- {item}", end=" ")


# Example
make_sandwich("Lettuce", "Tomato", "Cheese")



# Task 4 - Understanding Recursion
print("\n\n----------- Task 4 -----------\n")

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


# Example usage
resultingFactorial = factorial(5)
resultingFibonacci = fibonacci(6)

print(f"Factorial of 5 is {resultingFactorial}.", end=" ")
print(f"The 6th Fibonacci number is {resultingFibonacci}.")
