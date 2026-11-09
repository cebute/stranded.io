from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent.parent/"db"
DATA_FILE = DATA_DIR/"data.json"

def initialize():
    DATA_DIR.mkdir(exist_ok=True, parents=True)

def save_game(character_name, hp, inventory, checkpoint):
    game_data = {
        "character_name": character_name,
        "hp": hp,  
        "inventory": inventory,
        "checkpoint": checkpoint
    }
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(game_data, file, indent=4)
    except Exception:
        with open(DATA_FILE, "w") as file:
            json.dump({}, file, indent=4)

def load_game():
    initialize()
    try:
        with open(DATA_FILE, "r") as file:
            game_data=json.load(file)
    except Exception:
        return {
            "character_name": None,
            "hp": 40,  
            "inventory": [],
            "checkpoint": ""
        }
    return game_data