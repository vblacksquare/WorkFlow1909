
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


def create_peter_griffin():
    peter = create_person("Пітер Гріффін")
    peter["stats"]["health"] = 100000000
    peter["stats"]["defense"] = 10000000
    peter["stats"]["level"] = 10000000000000000

    return peter


def create_bum():
    bum = create_person("бомж, як він тут оказався :()")
    bum["stats"]["health"] = 999

    return bum


def create_weak_blob():
    blob = create_person("Слайм")
    blob["stats"]["health"] = 25

    return blob


def create_map():
    _map = create_person("я карта " * 10)
    _map["stats"]["health"] = 57

    return _map