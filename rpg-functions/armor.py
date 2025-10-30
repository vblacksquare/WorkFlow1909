
from items import create_armor


def create_iron_helmet():
    return create_armor(
        name="Залізний шолом",
        description="Голова буде цілою...",
        defense=3,
        piece="helmet"
    )


def create_iron_chestplate():
    return create_armor(
        name="Залізний нагрудник",
        description="Тяжкий нагрудник з кованого заліза",
        defense=6,
        piece="chestplate"
    )


def create_iron_leggings():
    return create_armor(
        name="Залізні штани",
        description="Залізні поножі для захисту самого головного",
        defense=4,
        piece="leggings"
    )


def create_iron_boots():
    return create_armor(
        name="Залізні чоботи",
        description="Важкі чоботи з заліза",
        defense=2,
        piece="boots"
    )


def create_helmet_leather():
    return create_armor(
        name="Шолом",
        defense = 5,
        description="Шкіряний шолом на голову",
        piece="helmet"
    )


def create_chestplate_leather():
    return create_armor(
        name="Нагрудник",
        defense = 10,
        description="Шкіряний нагрудник на тіло",
        piece="chestplate"
    )


def create_leggings_leather():
    return create_armor(
        name="Штани",
        defense = 7,
        description="Шкіряні щтани на ноги",
        piece="leggings"
    )


def create_boots_leather():
    return create_armor(
        name="Взуття",
        defense = 5,
        description="Шкіряне взуття на ноги",
        piece="boots"
    )


def armor_diamond_chestplate():
    return create_armor(
        name="Фольговий Нагрудник",
        description="її справжнє походження невідоме",
        defense=1000,
        piece="chestplate"
    )
