"""
Flyweight.
Много одинаковых деревьев с разными координатами.
"""


class TreeType:
    """Легковес - общие данные"""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def draw(self, x, y):
        print(f"🌲 {self.name} ({self.color}) на позиции ({x}, {y})")


class TreeFactory:
    """Фабрика легковесов"""
    _tree_types = {}

    @staticmethod
    def get_tree_type(name, color):
        key = (name, color)
        if key not in TreeFactory._tree_types:
            print(f"[СОЗДАНО] Новый тип дерева: {name}")
            TreeFactory._tree_types[key] = TreeType(name, color)
        return TreeFactory._tree_types[key]


class Tree:
    """Контекст - уникальные данные"""

    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.type = tree_type

    def draw(self):
        self.type.draw(self.x, self.y)


# Использование
def main():
    print("=== Flyweight: Лес ===\n")

    forest = []

    # Создаем деревья (всего 2 типа, но много экземпляров)
    types = [
        ("Дуб", "зеленый"),
        ("Береза", "белый"),
        ("Дуб", "зеленый"),  # Повтор - используем существующий
        ("Сосна", "зеленый"),
        ("Береза", "белый"),  # Повтор
    ]

    for i, (name, color) in enumerate(types):
        tree_type = TreeFactory.get_tree_type(name, color)
        tree = Tree(x=i * 10, y=i * 5, tree_type=tree_type)
        forest.append(tree)

    # Рисуем лес
    print("\nРисуем лес:")
    for tree in forest:
        tree.draw()

    print(f"\nВсего деревьев: {len(forest)}")
    print(f"Типов деревьев: {len(TreeFactory._tree_types)}")


if __name__ == "__main__":
    main()