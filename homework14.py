
def hello():
    name = input("Your name: ")
    print(f"Hello, {name}!")


def is_even(n):
    if n % 2 == 0:
        print("Парне")

    else:
        print("Непарне")


def min_num(a, b, c):
    numbers = [a, b, c]
    return min(numbers)


hello()
is_even(3)
min_num(1, 2, 3)
