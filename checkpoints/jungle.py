def jungle(character_name, hp, inventory):
    print("\n" + "="*50)
    print("🌴 CHECKPOINT: THE JUNGLE")
    print("="*50)
    print(
        f"You have {hp} HP left. You have to do something, otherwise you won't make it.\n\n"
        "1. Treat your wounds\n"
        "2. Try some herbs you see. Perhaps it could help\n"
    )

    # First decision loop: Health status
    choice = "0"
    while choice not in ["1", "2"]:
        choice = input("What are you going to do? ").strip()

        if choice == "1":
            hp += 20
            if "first_aid_kit" in inventory:
                inventory.remove("first_aid_kit")
                print("\n💉 You use the First Aid kit to bandage your bleeding wounds.")
            else:
                print("\nYou don't have a first aid kit! You try your best to patch yourself up with large leaves.")
                
            print(f"You feel a lot better after a few minutes. [HP: {hp}]. But you still need to find food and clean water.")

        elif choice == "2":
            print("\n🤢 Should have taken those herb classes seriously. It was highly poisonous! DEATH!!!!")
            hp = 0
            return "game_over", hp, inventory

        else:
            print("\nGod abeg... That's not an option. Try again!")

    # Second decision loop: Survival and Destination
    print(
        "\n🎵 While resting, you hear the distant sound of rushing water. You follow it and find a clear stream!\n"
        "Looking around, you see some fruit trees and a deer grazing a few yards away.\n"
        "Are you feeling lucky?\n\n"
        "1. Try hunting the deer\n"
        "2. Try your luck at fishing in the stream\n"
        "3. Climb the trees to gather fruits and get a better view\n"
    )

    has_fished = False

    while True:
        choice = input("What's your decision? ").strip()
        
        if choice == "1":
            print(
                "\n🐻 While tracking the deer, a massive, territorial bear ambushes you!\n"
                "Weak and weaponless, you stand no chance. DEATH!!!!!"
            )
            hp = 0
            return "game_over", hp, inventory
            
        elif choice == "2":
            if not has_fished:
                print(
                    "\n🐟 You construct a makeshift fishing tool using your wire string and get lucky!\n"
                    "You catch 3 fish before your line snaps. You cook and eat them over a small fire.\n"
                    "Your hunger is satisfied! Restored 15 HP."
                )
                hp += 15
                has_fished = True
                print(f"[HP: {hp}] You are fed, but you still need to find a path out of here. What next?")
            else:
                print("\nYour fishing line is already broken! You need to choose another option.")
                
        elif choice == "3":
            print(
                "\n🐒 You climb a tall tree and gather plenty of wild fruits.\n"
                "From the high canopy, you spot a lighthouse far in the distance!\n"
                "To head toward it, you must descend into a dark, rocky chasm leading to a cave system..."
            )
            # Instantly transitions to the cave level smoothly
            return "cave", hp, inventory
            
        else:
            print("\nGod abeg... That's not a valid survival choice. Choose 1, 2, or 3.")
