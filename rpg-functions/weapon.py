
from items import create_weapon


def create_greatsword_of_artorias():
    return create_weapon(
        name="Дворучний меч першого хранителя безодні",
        description="Дворучний меч, що належав лицарю Арторіасу, лицарю з вовчою кров'ю та першому Хранителю Безодні. ",
        damage=30
    )


def create_fist():
    return create_weapon(
        name="Кулак",
        description="Це просто кулак",
        damage=5
    )


def create_axe():
    return create_weapon(
        name="Сокира",
        description="Це просто сокира",
        damage=15
    )


def create_gun():
    return create_weapon(
        name="Пістолет",
        description="Це просто пістолет",
        damage=50
    )


def create_sword():
    return create_weapon(
        name="Меч",
        description="Трохи іржавий меч",
        damage=10
    )


def create_bow():
    return create_weapon(
        name="Лук",
        description="Саморобний лук з міцною тятивою",
        damage=7
    )


def create_spear():
    return create_weapon(
        name="копіє",
        description="Це копіє",
        damage=25
    )


def create_shurikens():
    return create_weapon(
        name="shurikens",
        description="Це shurikens",
        damage=13
    )


def create_titanium_sword():
    return create_weapon(
        name="титановий меч",
        description="це меч зробленний із титана",
        damage=40
    )


def create_tree_sword():
    return create_weapon(
        name="дерев'яний меч",
        description="це меч зробленний із дерева",
        damage=5
    )


def create_strong_stick():
    return create_weapon(
        name="палка зі кропивою",
        description="дуже сильна палка",
        damage=80
    )
