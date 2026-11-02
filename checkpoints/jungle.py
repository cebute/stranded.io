def jungle(
    character_name,
    hp,
    backpack
):
    print(
        f"You have {hp} left. You have to do something else you won't make it.\n"
        "1. Treat your wounds\n"
        "2. Try some herbs you see. Perhaps it could help\n"
        "What are you doing to do?\n"
    )

    choice = input("Make a choice: ")

    choice = "0"
    while choice is "0":
        if choice == "1":
            hp += 20
            # backpack.pop(0)
            print(f"Feel a lot better after a few minutes. But you still need to find food and clean water.")

        elif choice == "2":
            print("Should have taken those herb classes seriously. DEATH!!!!")
            hp -= 20
            return "game_over"

        else:
            print("God abeg...")
            choice = "0"

    print(
        "While treating yourself, you begin to hear the sound of what sounds lik a brook. You go to check it out and yep, there's a clear stream. Looking around you see some fruit trees and even a deer feeding some yards away. Are feeling lucky;\n"
        "1. Try hunting the deer\n"
        "2. Try your luck at fishing\n"
        "3. Get some fruits from the tall trees around you\n"
    )

    choice = input("What's your decision: ")

    while True:
        if choice == "1":
            print(
                "You were attacked and killed while trying to hunt a deer by a very hungry bear...DEATH!!!!!"
            )
            return "game_over"
        elif choice == "2":
            print(
                "You construct a make shift fishing tool and got lucky. You caught 3 fishes before your line broke."
            )
        elif choice == "3":
            print(
                "You climb a tree and while gathering some fruits you sot a lighthouse in the distance. looks like you found your next destination."
            )

    backpack = {
        "fruits",
        "water",
        "dried_fish"
    }