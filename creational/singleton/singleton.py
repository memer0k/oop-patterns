"""
Singleton.
Единственный логгер для всего приложения.
"""


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("[СОЗДАНИЕ] Создаем единственный логгер")
            cls._instance = super().__new__(cls)
            cls._instance.messages = []
        return cls._instance

    def log(self, message):
        self.messages.append(message)
        print(f"[ЛОГ] {message}")

    def show_logs(self):
        print("\n=== Все логи ===")
        for msg in self.messages:
            print(f"- {msg}")


# Использование
def main():
    print("=== Singleton: Единый логгер ===\n")

    # Пытаемся создать два "разных" логгера
    logger1 = Logger()
    logger2 = Logger()

    print(f"logger1 is logger2: {logger1 is logger2}")
    print(f"ID logger1: {id(logger1)}")
    print(f"ID logger2: {id(logger2)}\n")

    # Пишем в один, читаем из другого
    logger1.log("Приложение запущено")
    logger2.log("Пользователь вошел")
    logger1.log("Запрос к базе данных")

    # Все логи в одном месте
    logger2.show_logs()


if __name__ == "__main__":
    main()