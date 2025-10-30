
from person import create_person


def create_weak_goblin():
    goblin = create_person("Слабкий гоблін")
    goblin["stats"]["health"] = 25

    return goblin


def create_goblin():
    goblin = create_person("Гоблін")
    goblin["stats"]["health"] = 35

    return goblin


def create_bat():
    bat = create_person("Кажан")
    bat["stats"]["health"] = 10

    return bat


def create_dragon():
    dragon = create_person("Дракон")
    dragon["stats"]["health"] = 110

    return dragon


def create_ghost():
    ghost = create_person("Привид")
    ghost["stats"]["health"] = 50

    return ghost


def create_hero(nickname):
    hero = create_person(nickname)
    return hero
