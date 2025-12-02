"""
Template Method.
Процесс приготовления напитков.
"""

from abc import ABC, abstractmethod


class Beverage(ABC):
    """Абстрактный класс с шаблонным методом"""

    def prepare(self):
        """Шаблонный метод"""
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("[ОБЩЕЕ] Кипятим воду")

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        print("[ОБЩЕЕ] Наливаем в чашку")

    @abstractmethod
    def add_condiments(self):
        pass


class Tea(Beverage):
    """Чай"""

    def brew(self):
        print("[ЧАЙ] Завариваем чайные листья")

    def add_condiments(self):
        print("[ЧАЙ] Добавляем лимон")


class Coffee(Beverage):
    """Кофе"""

    def brew(self):
        print("[КОФЕ] Завариваем кофейные зерна")

    def add_condiments(self):
        print("[КОФЕ] Добавляем молоко и сахар")


# Использование
def main():
    print("=== Template Method: Напитки ===\n")

    print("Готовим чай:")
    tea = Tea()
    tea.prepare()

    print("\nГотовим кофе:")
    coffee = Coffee()
    coffee.prepare()


if __name__ == "__main__":
    main()