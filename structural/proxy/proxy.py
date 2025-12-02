"""
Proxy.
Заместитель для изображения (ленивая загрузка).
"""


class RealImage:
    """Настоящее изображение (тяжелое)"""

    def __init__(self, filename):
        self.filename = filename
        self._load()

    def _load(self):
        print(f"[ЗАГРУЗКА] Загружаем изображение: {self.filename}")

    def display(self):
        print(f"[ОТОБРАЖЕНИЕ] Показываем: {self.filename}")


class ImageProxy:
    """Заместитель (ленивая загрузка)"""

    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()


# Использование
def main():
    print("=== Proxy: Изображения ===\n")

    # Создаем заместители (изображения не загружаются)
    images = [
        ImageProxy("photo1.jpg"),
        ImageProxy("photo2.jpg"),
        ImageProxy("photo3.jpg")
    ]

    print("Создали прокси, но изображения не загружены\n")

    # Загружаем только при необходимости
    print("Первое изображение:")
    images[0].display()

    print("\nВторое изображение:")
    images[1].display()

    print("\nПервое снова (уже загружено):")
    images[0].display()


if __name__ == "__main__":
    main()