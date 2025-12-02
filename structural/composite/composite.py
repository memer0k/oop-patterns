"""
Composite.
Папки и файлы в файловой системе.
"""


class FileSystemComponent:
    def show(self, indent=0):
        pass


class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print("  " * indent + f"📄 {self.name}")


class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def show(self, indent=0):
        print("  " * indent + f"📁 {self.name}")
        for child in self.children:
            child.show(indent + 1)


# Использование
def main():
    print("=== Composite: Файловая система ===\n")

    # Создаем структуру
    root = Folder("Документы")

    work = Folder("Работа")
    work.add(File("отчет.docx"))
    work.add(File("план.xlsx"))

    photos = Folder("Фото")
    photos.add(File("отпуск.jpg"))
    photos.add(File("семья.png"))

    root.add(work)
    root.add(photos)
    root.add(File("заметки.txt"))

    # Показываем
    root.show()


if __name__ == "__main__":
    main()