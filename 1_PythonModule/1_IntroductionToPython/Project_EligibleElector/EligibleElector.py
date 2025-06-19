# Project: Eligible Elector
# Neha Rao



age = int(input("How old are you? "))       # Geeting user input


# Checking if the user is eligible to vote
if int(age) >= 18:      # If 18 or above, the user is eligible to vote

    # Printing result
    print("Congratulations! You are eligible to vote. Go make a difference!\n")

else:       # If below 18, the user is not eligible to vote
    moreYears = 18 - int(age)       # Calculating the number of years left to be eligible

    # Printing result and the number of years left to be eligible
    print(f"Oops! You’re not eligible yet. But hey, only {moreYears} more years to go!\n")