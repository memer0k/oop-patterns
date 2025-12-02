"""
Bridge.
Разные фигуры и разные цвета.
"""


# Реализация
class Color:
    def fill(self):
        pass


class Red(Color):
    def fill(self):
        return "красный"


class Blue(Color):
    def fill(self):
        return "синий"


# Абстракция
class Shape:
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        return f"Рисуем круг {self.color.fill()} цвета"


class Square(Shape):
    def draw(self):
        return f"Рисуем квадрат {self.color.fill()} цвета"


# Использование
def main():
    print("=== Bridge: Фигуры и цвета ===\n")

    red = Red()
    blue = Blue()

    shapes = [
        Circle(red),
        Circle(blue),
        Square(red),
        Square(blue)
    ]

    for shape in shapes:
        print(shape.draw())


if __name__ == "__main__":
    main()