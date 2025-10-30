
def create_person(nickname):
    return {
        "nickname": nickname.capitalize(),
        "stats": {
            "health": 100,
            "strength": 0,
            "agility": 0,
            "intelligence": 0,
            "level": 0,
            "experience": 100
        },
        "equipment": {
            "helmet": None,
            "chestplate": None,
            "leggings": None,
            "boots": None,
            "left_arm": None,
            "right_arm": 0
        },
        "inventory": []
    }
