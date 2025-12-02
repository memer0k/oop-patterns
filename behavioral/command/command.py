"""
Command.
Команды для управления светом.
"""


class Light:
    """Получатель команды"""

    def turn_on(self):
        print("[СВЕТ] Включен")

    def turn_off(self):
        print("[СВЕТ] Выключен")


class Command:
    """Абстрактная команда"""

    def execute(self):
        pass


class LightOnCommand(Command):
    """Конкретная команда: включить свет"""

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    """Конкретная команда: выключить свет"""

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class RemoteControl:
    """Инициатор (пульт)"""

    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()


# Использование
def main():
    print("=== Command: Управление светом ===\n")

    # Создаем объекты
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()

    # Включаем свет
    print("Нажимаем кнопку ВКЛ:")
    remote.set_command(light_on)
    remote.press_button()

    # Выключаем свет
    print("\nНажимаем кнопку ВЫКЛ:")
    remote.set_command(light_off)
    remote.press_button()


if __name__ == "__main__":
    main()