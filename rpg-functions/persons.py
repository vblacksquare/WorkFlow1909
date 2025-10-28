
from items import create_fist


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
        "inventory": [create_fist()]
    }


def create_hero(nickname):
    hero_person = create_person(nickname)
    return hero_person


def create_weak_goblin():
    goblin_person = create_person("слабкий гоблін")
    goblin_person["stats"]["health"] = 25
    return goblin_person
