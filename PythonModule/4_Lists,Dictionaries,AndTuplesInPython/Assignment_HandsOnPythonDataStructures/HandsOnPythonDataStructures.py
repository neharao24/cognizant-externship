# Assignment: Hands on Python Data Structures
# Neha Rao


# Task 1 - Working with Lists
print("\n----------- Task 1 -----------\n")

favFruits = ['strawberry', 'mango', 'peach', 'watermelon', 'blueberry']


print("Original list:", favFruits)

favFruits.append('kiwi')
print("After adding a fruit:", favFruits)

favFruits.remove('blueberry')
print("After removing a fruit:", favFruits)

print("Reversed List:", favFruits[::-1])



# Task 2 - Exploring Dictionaries
print("\n\n----------- Task 2 -----------\n")

info = {"name": "Neha", "age": "21", "city": "Tracy"}

info["favorite color"] = "Pink"
info["city"] = "Tempe"


keys = list(info.keys())
print("Keys: ", end="")
for i in range(len(keys)):
    if  i == len(keys) - 1:
        print(keys[i])
    else:
        print(f"{keys[i]}, ", end="")


values = list(info.values())
print("Values: ", end="")
for i in range(len(values)):
    if  i == len(values) - 1:
        print(values[i])
    else:
        print(f"{values[i]}, ", end="")





# Task 3 - Using Tuples
print("\n\n----------- Task 3 -----------\n")

favThings = ('Big Hero 6', 'Hello', 'Ruby Red')

try:
    favThings[0] = 'Spiderman'
except TypeError:
    print("Oops! Tuples cannot be changed.")

print(f"Length of tuple: {len(favThings)}\n")

