
from logic import fight
from enemies import create_hero, create_weak_goblin


hero = create_hero("punk")
goblin = create_weak_goblin()

fight(hero, goblin)
