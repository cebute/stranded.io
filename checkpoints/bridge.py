def bridge(character_name, hp, inventory):

    print(
        f"\nWelcome to the Old Bridge, {character_name}!\n"
        "After leaving the cave, you arrive at an old wooden bridge.\n"
        "Unfortunately, part of the bridge has collapsed.\n"
        "Strong winds are shaking the remaining wooden planks.\n"
    )

    # Check whether the player has the rope
    if "rope" not in inventory:

        print(
            "You need a rope to secure the broken bridge.\n"
            "Unfortunately, you don't have one.\n"
            "You must return to the cave."
        )

        return hp, inventory, False

    print(
        "Fortunately, you have the rope you collected from the cave.\n"
        "You can use it to secure your crossing.\n"
    )

    while True:

        if hp <= 0:
            print("You have run out of energy!")
            return hp, inventory, False

        print(
            "\nWhat would you like to do?\n"
            "1. Use the rope to secure the bridge.\n"
            "2. Attempt to jump across.\n"
            "3. Wait for the storm to pass.\n"
            "4. Check inventory.\n"
        )

        choice = input("Make a choice: ").strip().lower()

        # OPTION 1: USE ROPE
        if choice == "1":

            print(
                "\nYou carefully tie the rope around a strong wooden post.\n"
                "You use it to support yourself while crossing.\n"
                "After a difficult journey, you successfully reach the other side!"
            )

            break

        # OPTION 2: JUMP ACROSS
        elif choice == "2":

            print(
                "\nYou attempt to jump across the broken section.\n"
                "Unfortunately, you lose your balance and fall back onto the bridge.\n"
                "You lose 2 HP."
            )

            hp = max(0, hp - 2)

            print(f"Remaining HP: {hp}")

        # OPTION 3: WAIT FOR THE STORM
        elif choice == "3":

            print(
                "\nYou decide to wait for the storm to calm down.\n"
                "However, the cold weather drains your energy.\n"
                "You lose 1 HP."
            )

            hp = max(0, hp - 1)

            print(f"Remaining HP: {hp}")

        # OPTION 4: CHECK INVENTORY
        elif choice == "4":

            print("\nYour inventory:")

            if inventory:
                for item in inventory:
                    print(f"- {item}")
            else:
                print("Your inventory is empty.")

        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")

    # CHECK FOR KEY BEFORE UNLOCKING THE GATE
    if "key" not in inventory:

        print(
            "\nYou successfully cross the bridge but discover an ancient gate.\n"
            "Unfortunately, the gate is locked.\n"
            "You need a key to unlock it.\n"
            "Return to the cave and search for the key."
        )

        return hp, inventory, False

    print(
        "\nYou discover an ancient gate on the other side of the bridge.\n"
        "You insert your key into the lock, and the gate opens!"
    )

    # GUARDIAN'S PUZZLE
    print(
        "\nSuddenly, an old guardian appears.\n"
        "'Before you proceed, answer my riddle.'\n"
        "\nWhat has cities but no houses, forests but no trees, "
        "and rivers but no water?\n"
        "\n1. A painting"
        "\n2. A map"
        "\n3. A book"
        "\n4. A mirror"
    )

    attempts = 2

    while attempts > 0:

        answer = input("\nChoose your answer: ").strip()

        if answer == "2":

            print(
                "\nCorrect! The guardian is impressed by your intelligence.\n"
                "He steps aside and allows you to proceed.\n"
                "You can now see the lighthouse in the distance!"
            )

            return hp, inventory, True

        else:

            attempts -= 1
            hp = max(0, hp - 1)

            print("\nIncorrect answer! You lose 1 HP.")
            print(f"Remaining HP: {hp}")

            if hp <= 0:
                print("You have run out of energy. Game over!")
                return hp, inventory, False

            if attempts > 0:
                print("You have one final attempt.")

    print(
        "\nThe guardian refuses to let you proceed.\n"
        "You must return and try again."
    )

    return hp, inventory, False