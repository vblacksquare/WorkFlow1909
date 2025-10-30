
def create_item(name, _type, description, action):
    return {
        "name": name,
        "description": description,
        "type": _type,
        "action": action
    }


def create_weapon(name, description, damage):
    item = create_item(
        name=name,
        _type="weapon",
        description=description,
        action=f"{name} наніс {{damage}} шкоди"
    )
    item["damage"] = damage

    return item


def create_armor(name, description, defense, piece):
    item = create_item(
        name=name,
        _type="armor",
        description=description,
        action=""
    )
    item["defense"] = defense
    item["piece"] = piece

    return item


def create_utility(name, description, target, increase):
    item = create_item(
        name=name,
        _type="utility",
        description=description,
        action=f"{name} збільшив {target} до {{value}}"
    )
    item["target"] = target
    item["increase"] = increase

    return item
