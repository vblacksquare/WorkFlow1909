
import random


def fight(hero_person, enemy_person):
    print(f"<---- {hero_person['nickname']} VS {enemy_person['nickname']} ---->")

    turn = "hero"

    while True:
        if hero_person["stats"]["health"] <= 0:
            print(f"{enemy_person['nickname']} вбив {hero_person['nickname']} :((((")
            exit()

        elif enemy_person["stats"]["health"] <= 0:
            print(f"{hero_person['nickname']} вбив {enemy_person['nickname']}")
            return

        if turn == "hero":
            options = [
                hero_person["inventory"][hero_person["equipment"]["right_arm"]]
            ]

            print()
            for i, option in enumerate(options):
                option_action = option['action'].format(damage=option['damage'])
                print(f"{i+1}. {option_action}")

            option = int(input("Оберіть варіант: ")) - 1
            chosen_option = options[option]

            if chosen_option['type'] == "weapon":
                random_damage = random.randint(chosen_option["damage"] * 8, chosen_option["damage"] * 12) / 10
                enemy_person['stats']['health'] -= random_damage

                print()
                print(f"Ви використали '{chosen_option['name']}'")
                print(f"{enemy_person['nickname']} втратив {random_damage} хп: {enemy_person['stats']['health']}")

        else:
            options = [
                enemy_person["inventory"][enemy_person["equipment"]["right_arm"]]
            ]
            option = random.randint(0, len(options)-1)
            chosen_option = options[option]

            if chosen_option['type'] == "weapon":
                random_damage = random.randint(chosen_option["damage"] * 8, chosen_option["damage"] * 12) / 10
                hero_person['stats']['health'] -= random_damage

                print()
                print(f"Ворог використав '{chosen_option['name']}'")
                print(f"{hero_person['nickname']} втратив {random_damage} хп: {hero_person['stats']['health']}")

        if turn == "hero":
            turn = "enemy"

        else:
            turn = "hero"
