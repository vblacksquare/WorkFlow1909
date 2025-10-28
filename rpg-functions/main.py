
from persons import create_hero, create_weak_goblin
from logic import fight


hero = create_hero("punk_lord")
enemy = create_weak_goblin()

fight(hero, enemy)
