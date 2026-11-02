from checkpoints.beach import beach
from checkpoints.jungle import jungle

def stranded_io_runner():
    print(
        "Welcome to Stranded IO. May God be with you...\n"
        "You wake up a forsaken island.\n"
        "Parched, hungry and bleeding amongst ship wreckage.\n"
        "you try to recall you name...\n"
    )

    character_name = input("My name is: ")
    hp = 40
    inventory = []

    checkpoint = "beach"

    checkpoint_options = {
        "1": "beach",
        "2": "jungle",
        "3": "cave",
        "4": "bridge",
        "5": "lighthouse",
        "6": "game_over"
    }

    while True:
        if checkpoint == "beach":
            level_payload = beach(character_name, hp)
            if isinstance(level_payload, tuple):
                checkpoint, inventory = level_payload
            else:
                checkpoint = level_payload

        elif checkpoint == "jungle":
            checkpoint = jungle(
                character_name,
                hp,
                inventory
            )
            
        elif checkpoint == "3":
            print("In the cave")
            break
        elif checkpoint == "4":
            print("Hope this is broken somewhere")
            break
        elif checkpoint == "5":
            print("There a'int no light in there")
            break
        elif checkpoint == "game_over":
            print("GAME OVER\n")
            break
        # else:
        #     print("Whoops, God abeg...")

    print("Go and rest\n")

stranded_io_runner()