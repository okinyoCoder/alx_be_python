def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            x = input("Add item to the list: ")
            return shopping_list.append(x)

        elif choice == '2':
            # Prompt for and remove an item
            x = input(" Name of item name to be removed from List")
            return shopping_list.remove(x)
        elif choice == '3':
            # Display the shopping list
            display_menu()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()