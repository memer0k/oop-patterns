"""
Visitor.
Посетитель для разных типов документов.
"""


class Document:
    """Элемент"""

    def accept(self, visitor):
        pass


class PDFDocument(Document):
    def accept(self, visitor):
        visitor.visit_pdf(self)


class WordDocument(Document):
    def accept(self, visitor):
        visitor.visit_word(self)


class Visitor:
    """Посетитель"""

    def visit_pdf(self, pdf):
        pass

    def visit_word(self, word):
        pass


class PrinterVisitor(Visitor):
    """Посетитель для печати"""

    def visit_pdf(self, pdf):
        print("[ПЕЧАТЬ] Печатаем PDF документ")

    def visit_word(self, word):
        print("[ПЕЧАТЬ] Печатаем Word документ")


class ExporterVisitor(Visitor):
    """Посетитель для экспорта"""

    def visit_pdf(self, pdf):
        print("[ЭКСПОРТ] Экспортируем PDF в HTML")

    def visit_word(self, word):
        print("[ЭКСПОРТ] Экспортируем Word в PDF")


# Использование
def main():
    print("=== Visitor: Документы ===\n")

    # Создаем документы
    pdf = PDFDocument()
    word = WordDocument()

    # Создаем посетителей
    printer = PrinterVisitor()
    exporter = ExporterVisitor()

    # Применяем посетителей
    print("Печать документов:")
    pdf.accept(printer)
    word.accept(printer)

    print("\nЭкспорт документов:")
    pdf.accept(exporter)
    word.accept(exporter)


if __name__ == "__main__":
    main()