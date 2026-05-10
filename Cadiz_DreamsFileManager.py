# Surname_DreamsFileManager.py

file_name = "dreams.txt"

while True:

    print("\n===== DREAMS FILE MANAGER =====")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # READ FILE
    if choice == "1":

        try:
            with open(file_name, "r") as file:
                content = file.read()

                print("\n--- Inspiring Messages ---")

                if content.strip() == "":
                    print("The file is empty.")
                else:
                    print(content)

        except FileNotFoundError:
            print("The file does not exist yet.")

    # ADD MESSAGE
    elif choice == "2":

        message = input("Enter a new inspiring message: ")

        with open(file_name, "a") as file:
            file.write(message + "\n")

        print("Message added successfully!")

    # REWRITE FILE
    elif choice == "3":

        confirm = input(
            "This will replace all contents of the file. Continue? (yes/no): "
        )

        if confirm.lower() == "yes":

            new_content = input("Enter new inspiring message: ")

            with open(file_name, "w") as file:
                file.write(new_content + "\n")

            print("File rewritten successfully!")

        else:
            print("Rewrite cancelled.")

    # EXIT
    elif choice == "4":

        print("Exiting program...")
        break

    # INVALID CHOICE
    else:
        print("Invalid choice. Please try again.")
