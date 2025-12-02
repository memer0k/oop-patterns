"""
Decorator - короткий пример.
Добавляем опции к кофе.
"""


class Coffee:
    def cost(self):
        return 100

    def description(self):
        return "Кофе"


class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 30

    def description(self):
        return self.coffee.description() + " с молоком"


class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 10

    def description(self):
        return self.coffee.description() + " с сахаром"


# Использование
def main():
    print("=== Decorator: Кофе с добавками ===\n")

    coffee = Coffee()
    print(f"{coffee.description()}: {coffee.cost()} руб.")

    coffee_with_milk = MilkDecorator(coffee)
    print(f"{coffee_with_milk.description()}: {coffee_with_milk.cost()} руб.")

    coffee_with_all = SugarDecorator(MilkDecorator(coffee))
    print(f"{coffee_with_all.description()}: {coffee_with_all.cost()} руб.")


if __name__ == "__main__":
    main()