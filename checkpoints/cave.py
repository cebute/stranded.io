def cave(
    character_name,
    hp,
    inventory
):
    print(
        "You arrive at the entrance of the dark cave and you're now hungry and thirsty. After filling yourself up, you lit your torch and step into the cave only to get bombarded by bats who you disturbed with your torch. taking a deep breath, you walk in some, and get to a junction where two paths diverge. There seem to be a third path but it's obscured somewhat. Better try my luck with this two first. Which will you choose?\n"
        "1. The path to the left?\n"
        "2. The path to the right?\n"
    )

    while True:
        choice = input("Make a choice: ")

        if choice == "1":
            print("Heading down the path to the left")
            break
        elif choice == "2":
            print("Heading down the path to the right")
            break
        elif "rope" in inventory and "key" in inventory:
            break
        else:
            print("God abeg...")
