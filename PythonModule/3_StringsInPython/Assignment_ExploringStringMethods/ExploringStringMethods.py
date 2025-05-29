# Assignment: Exploring String Methods
# Neha Rao



# Task 1 - String Slicing and Indexing
print("\n----------- Task 1 -----------\n")

str = "Python is amazing!"      # Base string

# Printing diffeent parts/ reversed string
print("First word:", str[0:6])      # Printing first word
print("Amazing part:", str[11:18])      # Printing amazing part
print("Reversed string:", str[::-1])        # Printing reversed string



# Task 2 - String Methods
print("\n\n----------- Task 2 -----------\n")

str = " hello, python world! "      # Base string

# Printing strings each using different string methods
print("Removing extra spaces:", str.strip())        # Removing extra spaces
print("Capitalizing the first letter:", str.capitalize())       # Capitalizing the first letter
print("With replacement:", str.replace("world", "universe"))        # Replacing world with universe
print("Converting to uppercase:", str.upper())      # Converting to uppercase



# Task 3 - Check for Palindromes
print("\n\n----------- Task 3 -----------\n")

userWord = input("Enter a word: ")      # Getting user input
reverseWord = ""        # Variable to store reversed word

for i in range(len(userWord)):      # Loop to reverse the word
    reverseWord += userWord[len(userWord) - i - 1]      # Adding characters to reverseWord


# Checking if the word is a palindrome
if userWord == reverseWord: 
    print(f"Yes, \'{userWord}\' is a palindrome! 🤯\n")
else:
    print(f"No, \'{userWord}\' is not a palindrome. 😕\n")

