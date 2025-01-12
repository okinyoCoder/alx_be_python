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
            x = input("Enter item to add: ")
            return shopping_list.append(x)

        elif choice == '2':
            # Prompt for and remove an item
            x = input(" Enter item name to remove")
            if x in shopping_list:
                return shopping_list.remove(x)
            else:
                 print(f"'{x}' not found in the shopping list.")
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