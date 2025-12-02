"""
Prototype.
Клонирование документов с настройками.
"""

import copy


# Прототип
class Document:
    def __init__(self, text="", font="Arial", size=12):
        self.text = text
        self.font = font
        self.size = size
        self.settings = {"margins": "normal", "spacing": 1.0}

    def __str__(self):
        return f"Документ: '{self.text[:20]}...' ({self.font} {self.size}pt)"

    def clone(self):
        """Создает копию документа"""
        print(f"[КЛОНИРОВАНИЕ] Создаем копию: {self}")
        return copy.deepcopy(self)


# Использование
def main():
    print("=== Prototype: Клонирование документов ===\n")

    # Создаем прототип (шаблонный документ)
    template = Document(
        text="Шаблонный текст для отчета",
        font="Times New Roman",
        size=14
    )
    template.settings = {"margins": "wide", "spacing": 1.5}

    print(f"Оригинал: {template}")
    print(f"Настройки: {template.settings}\n")

    # Клонируем документ
    report1 = template.clone()
    report1.text = "Отчет за январь 2024"
    report1.settings["header"] = "Ежемесячный отчет"

    report2 = template.clone()
    report2.text = "Отчет за февраль 2024"
    report2.font = "Calibri"
    report2.settings["footer"] = "Страница"

    print(f"\nКлон 1: {report1}")
    print(f"Настройки: {report1.settings}")

    print(f"\nКлон 2: {report2}")
    print(f"Настройки: {report2.settings}")

    print(f"\nОригинал (не изменился): {template}")
    print(f"Настройки оригинала: {template.settings}")


if __name__ == "__main__":
    main()