from checkpoints.beach import beach
from checkpoints.jungle import jungle
from checkpoints.cave import cave
from checkpoints.bridge import bridge
from ui.intro_ui import show_intro

def stranded_io_runner():
    show_intro()

    character_name = input("My name is: ").strip() or "Survivor"
    hp = 40
    inventory = []

    # Game starts at the beach
    checkpoint = "beach"

    while True:
        # Check for game over or death conditions first
        if checkpoint == "game_over" or hp <= 0:
            print("\n💀 GAME OVER 💀")
            print("Your journey ends here. The island claims another soul.")
            break

        # 1. BEACH LEVEL
        if checkpoint == "beach":
            # Expecting beach to return: (next_checkpoint, updated_hp, updated_inventory)
            # or just a single string if nothing changes
            level_payload = beach(character_name, hp)
            if isinstance(level_payload, tuple):
                checkpoint, hp, inventory = level_payload
            else:
                checkpoint = level_payload

        # 2. JUNGLE LEVEL
        elif checkpoint == "jungle":
            level_payload = jungle(character_name, hp, inventory)
            if isinstance(level_payload, tuple):
                checkpoint, hp, inventory = level_payload
            else:
                checkpoint = level_payload
            
        # 3. CAVE LEVEL
        elif checkpoint == "cave":
            level_payload = cave(character_name, hp, inventory)
            if isinstance(level_payload, tuple):
                checkpoint, hp, inventory = level_payload
            else:
                checkpoint = level_payload
            
        # 4. BRIDGE LEVEL
        elif checkpoint == "bridge":
            level_payload = bridge(character_name, hp, inventory)
            if isinstance(level_payload, tuple):
                checkpoint, hp, inventory = level_payload
            else:
                checkpoint = level_payload
            
        # 5. LIGHTHOUSE LEVEL
        elif checkpoint == "lighthouse":
            print(f"\n{character_name} sees a towering, abandoned lighthouse...")
            break
            
        # Catch-all safety net for typos or unhandled areas
        else:
            print("\nWhoops, God abeg... Something went wrong with the island paths.")
            break

    print("\nGo and rest.\n")

if __name__ == "__main__":
    stranded_io_runner()
