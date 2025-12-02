"""
Chain of Responsibility.
Обработка заявок разных уровней.
"""


class Handler:
    """Обработчик"""

    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if self.successor:
            self.successor.handle(request)


class Manager(Handler):
    """Менеджер (обрабатывает до 1000)"""

    def handle(self, request):
        if request <= 1000:
            print(f"[МЕНЕДЖЕР] Одобрена заявка на {request} руб.")
        else:
            super().handle(request)


class Director(Handler):
    """Директор (обрабатывает до 5000)"""

    def handle(self, request):
        if request <= 5000:
            print(f"[ДИРЕКТОР] Одобрена заявка на {request} руб.")
        else:
            super().handle(request)


class President(Handler):
    """Президент (обрабатывает все)"""

    def handle(self, request):
        print(f"[ПРЕЗИДЕНТ] Одобрена заявка на {request} руб.")


# Использование
def main():
    print("=== Chain of Responsibility: Заявки ===\n")

    # Создаем цепочку
    president = President()
    director = Director(president)
    manager = Manager(director)

    # Обрабатываем заявки
    requests = [500, 1500, 4500, 10000]

    for amount in requests:
        print(f"\nЗаявка на {amount} руб.:")
        manager.handle(amount)


if __name__ == "__main__":
    main()