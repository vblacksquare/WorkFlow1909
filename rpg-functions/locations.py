
import enemies


def location1():
    return {
        "name": "якась локація",
        "description": "пояснення",
        "enemies": [enemies.create_fat_slime(), enemies.create_small_slime()],
        "boss": [enemies.create_magma_cube_boss()]
    }


def location2():
    return {
        "name": "Поселище гоблінів та огрів",
        "description": "там живуть гобліни",
        "enemies": [
            enemies.create_strong_goblin(), enemies.create_weak_goblin(),
            enemies.create_baby_ogr(), enemies.create_ogr_mage(),
            enemies.create_big_ogr()
        ],
        "boss": [enemies.create_goblin_king_boss(), enemies.create_lord_of_ogrs_boss()]
    }


def location5():
    return {
        "name": "Пекло",
        "description": "Саме пекло світу в якому... доволі спекотно",
        "enemies": [enemies.create_runic_skeleton(), enemies.create_ruin_guardian(), enemies.create_ink_wolf()],
        "boss": [enemies.create_hell_boss()]
    }
