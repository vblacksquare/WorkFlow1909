
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


def create_baby_ogr():
    ogr = create_person("Огр")
    ogr["stats"]["health"] = 20

    return ogr

def create_big_ogr():
    ogr = create_person("Великий огр")
    ogr["stats"]["health"] = 50

    return ogr

def create_ogr_mage():
    ogr = create_person("Огр маг")
    ogr["stats"]["health"] = 30

    return ogr

def create_lord_of_ogrs_boss():
    ogr = create_person("Принц Огрів")
    ogr["stats"]["health"] = 250

    return ogr

def create_goblin_king_boss():
    goblin = create_person("король гоблінів")
    goblin["stats"]["health"] = 190
    goblin["stats"]["level"] = 10

    return goblin


#: level 5
def create_runic_skeleton():
    s = create_person("Рунический скелет")
    s["stats"]["health"] = 35
    s["stats"]["strength"] = 10
    s["stats"]["agility"] = 6
    s["stats"]["intelligence"] = 8
    s["stats"]["level"] = 7

    return s

def create_ruin_guardian():
    g = create_person("Страж руїн")
    g["stats"]["health"] = 45
    g["stats"]["strength"] = 12
    g["stats"]["agility"] = 4
    g["stats"]["intelligence"] = 6
    g["stats"]["level"] = 10

    return g


def create_ink_wolf():
    wolf = create_person("Чорнильний вовк")
    wolf["stats"]["health"] = 35
    wolf["stats"]["strength"] = 6
    wolf["stats"]["agility"] = 12
    wolf["stats"]["intelligence"] = 2
    wolf["stats"]["level"] = 4

    return wolf


def create_hell_boss():
    b = create_person("Адський повелитель")
    b["stats"]["health"] = 100
    b["stats"]["strength"] = 25
    b["stats"]["agility"] = 10
    b["stats"]["intelligence"] = 14
    b["stats"]["level"] = 25

    return b


#: hero
def create_hero(nickname):
    hero = create_person(nickname)
    return hero
