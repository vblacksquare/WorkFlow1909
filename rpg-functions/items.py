
def create_weapon(name, base_damage):
    return {
        "name": name,
        "damage": [base_damage * 0.8, base_damage * 1.2],
        "info": f"~{base_damage} шкоди",
        "type": "weapon"
    }


def create_fist():
    return create_weapon("Кулак", 5)
