
import random


def throw(item, user_power, direction="вверх"):
    power = random.randint(user_power - 5, user_power + 5)
    print(f"Ви кинули {item} {direction} із силою {power}")


for i in range(10):
    throw(
        item="Яблуко",
        user_power=10,
        direction="прямо"
    )
