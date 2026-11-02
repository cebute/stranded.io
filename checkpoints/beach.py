def beach(
    character_name, 
    hp
):
    print(
        "You try to salvage what you can from the wreckage and you find this items\n"
        "1. Backpack\n"
        "2. First Aid kit\n"
        "3. Empty water bottle\n"
        "You pick em all up"
    )

    backpack = {"first_aid_kit", "empty_water_bottle", "wire_string", "lighter"}

    print(
        "I'm really thirsty, hungry and have to treat these injuries as i feel myself getting weaker. What do i do now?\n"
        "1. Get some sea water to drink. Should quench your thirst right?\n"
        "2. Head towards the jungle and find food and shade fromthe swealtering heat?\n"
        "What do i do?\n"
    )

    choice = input("Make a choice? ")

    if choice == "1":
        hp -= hp
        print(f"INSTANT DEATH... {hp}")
        return "game_over"
    elif choice == "2":
        print("You head towards the jungle tired and exhausted...")
        hp -= 20
        return "jungle", backpack