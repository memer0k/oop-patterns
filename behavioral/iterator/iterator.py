"""
Iterator - короткий пример.
Итерация по книгам в библиотеке.
"""


class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


class Library:
    """Коллекция книг"""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        return LibraryIterator(self.books)


class LibraryIterator:
    """Итератор для библиотеки"""

    def __init__(self, books):
        self.books = books
        self.index = 0

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        raise StopIteration


# Использование
def main():
    print("=== Iterator: Библиотека ===\n")

    # Создаем библиотеку
    library = Library()
    library.add_book(Book("Война и мир"))
    library.add_book(Book("Преступление и наказание"))
    library.add_book(Book("Мастер и Маргарита"))

    # Итерируемся
    print("Книги в библиотеке:")
    for book in library:
        print(f"  📚 {book}")

    # Вручную
    print("\nИтерация вручную:")
    iterator = iter(library)
    try:
        while True:
            book = next(iterator)
            print(f"  📖 {book}")
    except StopIteration:
        print("  Конец списка")


if __name__ == "__main__":
    main()