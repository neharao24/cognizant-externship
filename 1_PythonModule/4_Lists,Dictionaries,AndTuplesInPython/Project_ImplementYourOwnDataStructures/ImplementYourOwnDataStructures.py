# Project: Implement Your own Data Structures
# Neha Rao


inventory = {}      # empty dictionary for inventory

# Loop until user chooses to exit
print("\nWelcome to the Inventory Manager!")
while True:
    print("Select an option:")
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Update item quantity")
    print("4. Update item price")
    print("5. Display inventory")
    print("6. Calculate Total Value of Inventory")
    print("7. Exit")
    userChoice = input("Enter your choice: ")
    print("\n")

    if userChoice == "1":       # Add item to inventory
        # Get item name, quantity, price from user
        itemName = input("Enter item name: ")
        itemQuantity = int(input("Enter item quantity: "))
        itemPrice = float(input("Enter item price: $"))

        # Add item to inventory dictionary as tuple
        inventory[itemName] = (itemQuantity, itemPrice)
        print(f"\nItem {itemName} added to inventory.")

        # Updated inventory
        print(" Updated inventory:")
        for item, details in inventory.items():
            print(f"  -Item: {item}, Quantity: {details[0]}, Price: ${details[1]}")



    elif userChoice == "2":     # Remove item from inventory
        # Get item name from user
        itemName = input("Enter item name: ")

        if itemName in inventory:       # Check if item exists in inventory
            # Remove item from inventory dictionary
            del inventory[itemName]
            print(f"\nItem '{itemName}' removed from inventory.")

            # Updated inventory
            print(" Updated inventory:")
            for item, details in inventory.items():
                print(f"  -Item: {item}, Quantity: {details[0]}, Price: ${details[1]}")

        else:       # If item does not exist in inventory
            print(f"\nItem '{itemName}' not found in inventory.")



    elif userChoice == "3":     # Update item quantity
        # Get item name and new quantity from user
        itemName = input("Enter item name: ")

        if itemName in inventory:       # Check if item exists in inventory
            # Get new quantity from user & update inventory
            newQuantity = int(input("Enter new quantity: "))
            inventory[itemName] = (newQuantity, inventory[itemName][1])
            print(f"\nItem '{itemName}' quantity updated.")

            # Updated inventory
            print(" Updated inventory:")
            for item, details in inventory.items():
                print(f"  -Item: {item}, Quantity: {details[0]}, Price: ${details[1]}")

        else:       # If item does not exist in inventory
            print(f"\nItem '{itemName}' not found in inventory.")


 
    elif userChoice == "4":     # Update item price
        # Get item name and new price from user
        itemName = input("Enter item name: ")

        if itemName in inventory:       # Check if item exists in inventory
            # Get new price from user & update inventory
            newPrice = float(input("Enter new price: $"))
            inventory[itemName] = (inventory[itemName][0], newPrice)
            print(f"\nItem '{itemName}' price updated.")

            # Updated inventory
            print(" Updated inventory:")
            for item, details in inventory.items():
                print(f"  -Item: {item}, Quantity: {details[0]}, Price: ${details[1]}")

        else:       # If item does not exist in inventory
            print(f"\nItem '{itemName}' not found in inventory.")



    elif userChoice == "5":     # Display inventory
        if not inventory:       # Check if inventory is empty
            print("Inventory is empty.")
        else:       # If inventory is not empty, display it
            print("Current Inventory:")
            for item, details in inventory.items():
                print(f" -Item: {item}, Quantity: {details[0]}, Price: ${details[1]}")



    elif userChoice == "6":     # Calculate Total Value
        totalValue = 0
        for item, details in inventory.items():     # Iterate through inventory & calculate total value
            totalValue += details[0] * details[1]
        print(f"Total value of inventory: ${totalValue:.2f}")      



    elif userChoice == "7":     # Exit
        print("Exiting program...")
        break


    else:       # Invalid choice
        print("\nInvalid choice. Please try again.")
    

    print("\n\n")


print("Thank you for using the Inventory Manager! 👋")

