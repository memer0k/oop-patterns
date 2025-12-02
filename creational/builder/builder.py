"""
Builder - короткий пример.
Создание заказа пиццы.
"""


# Продукт
class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False

    def __str__(self):
        return (f"Пицца {self.size}: "
                f"{'сыр ' if self.cheese else ''}"
                f"{'пепперони ' if self.pepperoni else ''}"
                f"{'грибы ' if self.mushrooms else ''}")


# Строитель
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def build(self):
        return self.pizza


# Использование
def main():
    print("=== Builder: Создание пиццы ===\n")

    # Строим пиццу шаг за шагом
    pizza1 = (PizzaBuilder()
              .set_size("большая")
              .add_cheese()
              .add_pepperoni()
              .build())

    print(f"1. {pizza1}")

    pizza2 = (PizzaBuilder()
              .set_size("средняя")
              .add_cheese()
              .add_mushrooms()
              .build())

    print(f"2. {pizza2}")

    # Можно создавать по-разному
    builder = PizzaBuilder()
    builder.set_size("маленькая")
    builder.add_cheese()
    pizza3 = builder.build()

    print(f"3. {pizza3}")


if __name__ == "__main__":
    main()