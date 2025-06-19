# Assignment: Hands on Python Data Structures
# Neha Rao


# Task 1 - Working with Lists
print("\n----------- Task 1 -----------\n")

favFruits = ['strawberry', 'mango', 'peach', 'watermelon', 'blueberry']     # List of favourite fruits


print("Original list:", favFruits)      # Print the original list

favFruits.append('kiwi')        # Add a new fruit to the list
print("After adding a fruit:", favFruits)       # Print the updated list

favFruits.remove('blueberry')       # Remove a fruit from the list
print("After removing a fruit:", favFruits)     # Print the updated list

print("Reversed List:", favFruits[::-1])        # Print the reversed list



# Task 2 - Exploring Dictionaries
print("\n\n----------- Task 2 -----------\n")

info = {"name": "Neha", "age": "21", "city": "Tracy"}       # Dictionary with personal info

info["favorite color"] = "Pink"     # Add a new key-value pair
info["city"] = "Tempe"      # Update an existing key-value pair


keys = list(info.keys())        # Get the keys of the dictionary
print("Keys: ", end="")     # Print the keys
for i in range(len(keys)):      # Loop through the keys, print each & add comma
    if  i == len(keys) - 1:    
        print(keys[i])
    else:     
        print(f"{keys[i]}, ", end="")  


values = list(info.values())        # Get the values of the dictionary
print("Values: ", end="")       # Print the values
for i in range(len(values)):        # Loop through the values, print each & add comma
    if  i == len(values) - 1:
        print(values[i])
    else:
        print(f"{values[i]}, ", end="")





# Task 3 - Using Tuples
print("\n\n----------- Task 3 -----------\n")

favThings = ('Big Hero 6', 'Hello', 'Ruby Red')     # Tuple of favourite things

try:        # Try to modify the tuple
    favThings[0] = 'Spiderman'
except TypeError:       # If it's a tuple, it will throw a TypeError
    print("Oops! Tuples cannot be changed.")

print(f"Length of tuple: {len(favThings)}\n")       # Print the length of the tuple

