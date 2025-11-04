
from person import create_person


#: level 1
def create_fat_slime():
    blob = create_person("Товстий слайм")
    blob["stats"]["health"] = 25

    return blob

def create_small_slime():
    blob = create_person("Маленький слайм")
    blob["stats"]["health"] = 25

    return blob

def create_pink_slime():
    blob = create_person("Рожевий слайм")
    blob["stats"]["health"] = 25

    return blob

def create_magma_cube_boss():
    blob = create_person("Магма куб")
    blob["stats"]["health"] = 25

    return blob


#: level 2
def create_weak_goblin():
    goblin = create_person("Слабкий гоблін")
    goblin["stats"]["health"] = 25

    return goblin

def create_strong_goblin():
    goblin = create_person("Сильний гоблін")
    goblin["stats"]["health"] = 35

    return goblin

def create_bat():
    goblin = create_person("Кажан")
    goblin["stats"]["health"] = 35

    return goblin


#: hero
def create_hero(nickname):
    hero = create_person(nickname)
    return hero
