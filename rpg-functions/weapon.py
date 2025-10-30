
from items import create_weapon


def create_fist():
    return create_weapon(
        name="Кулак",
        description="Це просто кулак",
        damage=5
    )


def create_sword():
    return create_weapon(
        name="Меч",
        description="Це просто меч",
        damage=10
    )
