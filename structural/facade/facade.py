"""
Facade.
Один вызов вместо многих.
"""


class CPU:
    def start(self):
        print("[CPU] Запущен")


class Memory:
    def load(self):
        print("[Память] Загружена")


class HardDrive:
    def read(self):
        print("[Диск] Данные прочитаны")


# Фасад
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hdd = HardDrive()

    def start(self):
        print("Запуск компьютера:")
        self.cpu.start()
        self.memory.load()
        self.hdd.read()
        print("✅ Компьютер готов!")


# Использование
def main():
    print("=== Facade: Компьютер ===\n")

    # Без фасада
    print("Без фасада:")
    cpu = CPU()
    memory = Memory()
    hdd = HardDrive()

    cpu.start()
    memory.load()
    hdd.read()

    print("\nС фасадом:")
    # С фасадом
    computer = Computer()
    computer.start()


if __name__ == "__main__":
    main()