
from persons import create_person


def create_weak_goblin():
    goblin = create_person("goblin")
    goblin["stats"]["health"] = 25

    return goblin


def create_hero(nickname):
    hero = create_person(nickname)
    return hero
