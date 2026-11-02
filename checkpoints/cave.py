def cave(character_name, hp, inventory):

    print(
        f"\nWelcome to the cave, {character_name}!\n"
        "You arrive at the entrance of a dark cave.\n"
        "After filling yourself up, you light your torch and step inside.\n"
        "Suddenly, bats fly past you because you disturbed them!\n"
        "Taking a deep breath, you continue walking until you reach a junction.\n\n"
        "Two paths lie ahead. Which will you explore?\n"
    )

    while True:

        if hp <= 0:
            print("You have run out of energy! Your adventure ends here.")
            return hp, inventory

        if "rope" in inventory and "key" in inventory:
            print("\nCongratulations! You have collected both the rope and the key.")
            print("You can now proceed towards the Old Bridge.")
            return hp, inventory

        print("\nAvailable paths:")
        print("1. The path to the left")
        print("2. The path to the right")
        print("3. Check inventory")
        print("4. Leave the cave")

        choice = input("Make a choice: ").strip().lower()

        # LEFT PATH - KEY PUZZLE
        if choice == "1":

            if "key" in inventory:
                print("You have already collected the key!")
                continue

            print(
                "\nYou enter the left path and discover an ancient statue.\n"
                "The statue speaks:\n"
                "'I have keys but open no locks.\n"
                "I have space but no room.\n"
                "What am I?'\n"
                "\n1. A keyboard\n"
                "2. A treasure chest\n"
                "3. A door\n"
                "4. A map"
            )

            attempts = 2

            while attempts > 0:

                answer = input("Choose your answer: ").strip()

                if answer == "1":
                    print("\nCorrect! The statue reveals a hidden key.")
                    inventory.append("key")
                    break

                else:
                    attempts -= 1
                    hp -= 1

                    print(f"Wrong answer! You lost 1 HP.")
                    print(f"Remaining HP: {hp}")

                    if attempts > 0 and hp > 0:
                        print("You have one more attempt.")

            if "key" not in inventory:
                print("You failed to solve the riddle.")

        # RIGHT PATH - ROPE PUZZLE
        elif choice == "2":

            if "rope" in inventory:
                print("You have already collected the rope!")
                continue

            print(
                "\nYou enter the right path and discover a mysterious inscription.\n"
                "It reads:\n"
                "'I am long and strong.\n"
                "I help people climb, pull and cross.\n"
                "What am I?'\n"
                "\n1. A lantern\n"
                "2. A rope\n"
                "3. A stone\n"
                "4. A wooden box"
            )

            attempts = 2

            while attempts > 0:

                answer = input("Choose your answer: ").strip()

                if answer == "2":
                    print("\nCorrect! You discover a rope behind a loose rock.")
                    inventory.append("rope")
                    break

                else:
                    attempts -= 1
                    hp -= 1

                    print("Wrong answer! You lost 1 HP.")
                    print(f"Remaining HP: {hp}")

                    if attempts > 0 and hp > 0:
                        print("You have one more attempt.")

            if "rope" not in inventory:
                print("You failed to solve the riddle.")

        # CHECK INVENTORY
        elif choice == "3":

            print("\nYour inventory:")

            if inventory:
                for item in inventory:
                    print(f"- {item}")
            else:
                print("Your inventory is empty.")

        # LEAVE CAVE
        elif choice == "4":

            print("You decide to leave the cave.")
            return hp, inventory

        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")