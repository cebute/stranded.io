def beach(character_name, hp):
    print("\n" + "="*50)
    print("📍 CHECKPOINT: THE BEACH")
    print("="*50)
    print(
        "You try to salvage what you can from the wreckage and you find these items:\n"
        " 🎒 1. Backpack\n"
        " 🩹 2. First Aid kit\n"
        " 🍾 3. Empty water bottle\n"
        " 🪢 4. Wire string\n"
        " 🔥 5. Lighter\n"
        "You pick them all up and pack them away."
    )

    # Creating a list of items for the player's inventory
    inventory = ["first_aid_kit", "empty_water_bottle", "wire_string", "lighter"]

    print(
        f"\n[{character_name} - HP: {hp}]\n"
        "I'm really thirsty, hungry and have to treat these injuries as I feel myself getting weaker.\n"
        "What do I do now?\n\n"
        "1. Get some sea water to drink. Should quench your thirst right?\n"
        "2. Head towards the jungle and find food and shade from the sweltering heat?\n"
    )

    choice = input("Make a choice (1 or 2): ").strip()

    if choice == "1":
        hp = 0
        print(f"\n🤢 INSTANT DEATH... You drank saltwater! Your organs shut down rapidly. [HP: {hp}]")
        return "game_over", hp, inventory
        
    elif choice == "2":
        print("\n🌴 You head towards the jungle, tired and exhausted...")
        hp -= 20
        print(f"The blazing sun beats down on you as you trudge through the sand. [HP: {hp}]")
        return "jungle", hp, inventory
        
    else:
        print("\n🌀 Indecision costs you time. You stumble into the jungle aimlessly out of exhaustion.")
        hp -= 25
        return "jungle", hp, inventory
