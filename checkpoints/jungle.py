def jungle(
    character_name,
    hp,
    inventory
):
    print(
        f"You have {hp} HP left. You have to do something, otherwise you won't make it.\n"
        "1. Treat your wounds\n"
        "2. Try some herbs you see. Perhaps it could help\n"
        "What are you going to do?\n"
    )

    # Start with an empty or invalid choice to trigger the loop
    choice = "0"
    
    while choice not in ["1", "2"]:
        choice = input("Make a choice: ").strip()

        if choice == "1":
            hp += 20
            # If inventory is a list, you can remove the kit like this:
            if "first_aid_kit" in inventory:
                inventory.remove("first_aid_kit")
                print("💉 You use the First Aid kit to bandage your bleeding wounds.")
            else:
                print("You don't have a first aid kit! You try your best without tools.")
                
            print(f"Feel a lot better after a few minutes. [HP: {hp}]. But you still need to find food and clean water.")
            # Move on to the next part of the jungle level here...

        elif choice == "2":
            print("\n🤢 Should have taken those herb classes seriously. It was poisonous! DEATH!!!!")
            hp = 0
            return "game_over", hp, inventory

        else:
            print("\nGod abeg... That's not an option. Try again!")
            # The loop will automatically repeat because choice is still not "1" or "2"

    print(
        "While treating yourself, you begin to hear the sound of what sounds lik a brook. You go to check it out and yep, there's a clear stream. Looking around you see some fruit trees and even a deer feeding some yards away. Are feeling lucky;\n"
        "1. Try hunting the deer\n"
        "2. Try your luck at fishing\n"
        "3. Get some fruits from the tall trees around you\n"
    )


    while True:
        choice = input("What's your decision: ")
        
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
        else:
            print("\nGod abeg...")

    # inventory = {
    #     "fruits",
    #     "water",
    #     "dried_fish"
    # }