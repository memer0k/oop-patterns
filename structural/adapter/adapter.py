"""
Adapter.
Адаптируем старый принтер к новому интерфейсу.
"""


# Старый принтер (несовместимый интерфейс)
class OldPrinter:
    def print_document(self, text):
        print(f"[СТАРЫЙ ПРИНТЕР] Печатаю: {text}")


# Новый интерфейс (к которому хотим адаптироваться)
class NewPrinterInterface:
    def print_text(self, content):
        pass


# Адаптер
class PrinterAdapter(NewPrinterInterface):
    def __init__(self, old_printer: OldPrinter):
        self.old_printer = old_printer

    def print_text(self, content):
        # Адаптируем вызов
        self.old_printer.print_document(content)


# Клиентский код (работает только с новым интерфейсом)
class Computer:
    def print_document(self, printer: NewPrinterInterface, text: str):
        print("[КОМПЬЮТЕР] Отправляю на печать...")
        printer.print_text(text)


# Использование
def main():
    print("=== Adapter: Старый принтер в новой системе ===\n")

    # Старый принтер
    old_printer = OldPrinter()

    # Адаптер для старого принтера
    adapter = PrinterAdapter(old_printer)

    # Компьютер (работает только с новым интерфейсом)
    computer = Computer()

    # Печатаем через адаптер
    computer.print_document(adapter, "Мой важный документ")

    # Прямой вызов (для сравнения)
    print("\n--- Без адаптера ---")
    old_printer.print_document("Прямой вызов")


if __name__ == "__main__":
    main()