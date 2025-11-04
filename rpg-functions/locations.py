
import enemies


def location1():
    return {
        "name": "якась локація",
        "description": "пояснення",
        "enemies": [enemies.create_fat_slime(), enemies.create_bat(), enemies.create_small_slime()],
        "boss": [enemies.create_magma_cube_boss()]
    }
