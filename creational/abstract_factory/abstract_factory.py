"""
Абстрактная фабрика - простой пример.
Разные кухни в кафе.
"""

from abc import ABC, abstractmethod


# ========== ПРОДУКТЫ ==========

# 1. Основное блюдо
class MainCourse(ABC):
    @abstractmethod
    def serve(self):
        pass


class Pizza(MainCourse):
    def serve(self):
        print("[КУХНЯ] Подаем пиццу 'Маргарита'")


class Sushi(MainCourse):
    def serve(self):
        print("[КУХНЯ] Подаем сет 'Филадельфия'")


# 2. Напиток
class Drink(ABC):
    @abstractmethod
    def pour(self):
        pass


class Wine(Drink):
    def pour(self):
        print("[КУХНЯ] Наливаем красное вино")


class GreenTea(Drink):
    def pour(self):
        print("[КУХНЯ] Завариваем зеленый чай")


# ========== ФАБРИКИ ==========
class KitchenFactory(ABC):
    """Абстрактная кухня"""

    @abstractmethod
    def make_main(self) -> MainCourse:
        pass

    @abstractmethod
    def make_drink(self) -> Drink:
        pass


class ItalianKitchen(KitchenFactory):
    """Итальянская кухня"""

    def make_main(self) -> MainCourse:
        return Pizza()

    def make_drink(self) -> Drink:
        return Wine()


class JapaneseKitchen(KitchenFactory):
    """Японская кухня"""

    def make_main(self) -> MainCourse:
        return Sushi()

    def make_drink(self) -> Drink:
        return GreenTea()


# ========== КЛИЕНТ ==========
class Cafe:
    """Кафе, которое готовит заказ"""

    def __init__(self, kitchen: KitchenFactory):
        self.kitchen = kitchen

    def prepare_order(self):
        """Готовим заказ целиком из одной кухни"""
        print("\n🧑‍🍳 Готовим ваш заказ...")

        main = self.kitchen.make_main()
        drink = self.kitchen.make_drink()

        main.serve()
        drink.pour()

        print("✅ Заказ готов! Все блюда сочетаются.")


def main():
    print("=== Абстрактная фабрика: Разные кухни ===\n")

    print("1. Заказ в итальянском ресторане:")
    italian = ItalianKitchen()
    cafe = Cafe(italian)
    cafe.prepare_order()

    print("\n2. Заказ в японском ресторане:")
    japanese = JapaneseKitchen()
    cafe = Cafe(japanese)
    cafe.prepare_order()


if __name__ == "__main__":
    main()