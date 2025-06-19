# Project: Password Strength Checker
# Neha Rao



userPassword = input("Enter a password: ")      # Getting user password
# Initializing variable to False
length = False
lower = False
upper = False
digit = False
special = False
# Initializing password length to 10
passStrength = 10

# Checking password requirements
for i in range(len(userPassword)):
    if len(userPassword) >= 8:      # Checking password length
        length = True
    if userPassword[i].islower():       # Checking for lower case
        lower = True
    if userPassword[i].isupper():       # Checking for upper case
        upper = True
    if userPassword[i].isdigit():       # Checking for digit
        digit = True
    if userPassword[i] in "!@#$%^&*()_+-={}:<>":        # Checking for special character
        special = True


# Checking password strength & which requirements are not met
if (length == True) and (lower == True) and (upper == True) and (digit == True) and (special == True):
    print("Your password is strong! 💪")
else:
    needs = []      # Initializing list to store requirements not met
    if length == False: 
        needs.append("at least 8 characters")
        passStrength -= 2       # Reducing password strength by 2 if not met
    if lower == False:
        needs.append("at least one lowercase letter")
        passStrength -= 2       # Reducing password strength by 2 if not met
    if upper == False:
        needs.append("at least one uppercase letter")
        passStrength -= 2       # Reducing password strength by 2 if not met
    if digit == False:
        needs.append("at least one digit")
        passStrength -= 2       # Reducing password strength by 2 if not met
    if special == False:
        needs.append("at least one special character")
        passStrength -= 2       # Reducing password strength by 2 if not met


    message = ""        # Initializing message variable
    for i in needs:
        if i != needs[-1]:      # Checking if it's not the last requirement, then adding comma after
            message += i + ", "
        else:
            if len(needs) > 1:      # Adds "and" before last requirement if there are more than one requirements not met
                message += "and "
            message += i
            print(f"Password Strength: {str(passStrength)}/10")        # Printing password strength
            print(f"Your password needs {message}.")       # Printing message with requirements that are not met