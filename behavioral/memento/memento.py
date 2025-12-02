"""
Memento.
Сохранение и восстановление состояния текстового редактора.
"""


class TextEditor:
    """Создатель"""

    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def show(self):
        print(f"Текст: '{self.text}'")

    def save(self):
        return TextMemento(self.text)

    def restore(self, memento):
        self.text = memento.get_saved_text()


class TextMemento:
    """Снимок"""

    def __init__(self, text):
        self.saved_text = text

    def get_saved_text(self):
        return self.saved_text


class History:
    """Хранитель"""

    def __init__(self):
        self.history = []

    def save(self, memento):
        self.history.append(memento)

    def undo(self):
        if self.history:
            return self.history.pop()
        return None


# Использование
def main():
    print("=== Memento: Текстовый редактор ===\n")

    editor = TextEditor()
    history = History()

    # Пишем текст
    editor.write("Привет, ")
    editor.show()
    history.save(editor.save())

    editor.write("мир!")
    editor.show()
    history.save(editor.save())

    # Отменяем
    print("\nОтменяем последнее действие:")
    memento = history.undo()
    if memento:
        editor.restore(memento)
    editor.show()

    print("\nОтменяем еще раз:")
    memento = history.undo()
    if memento:
        editor.restore(memento)
    editor.show()


if __name__ == "__main__":
    main()