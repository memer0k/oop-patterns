"""
Observer.
Подписка на новости.
"""


class NewsPublisher:
    """Издатель"""

    def __init__(self):
        self.subscribers = []
        self.news = None

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def publish_news(self, news):
        self.news = news
        print(f"[ИЗДАТЕЛЬ] Опубликована новость: {news}")
        self.notify_subscribers()

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(self.news)


class Subscriber:
    """Подписчик"""

    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"[{self.name}] Получил новость: {news}")


# Использование
def main():
    print("=== Observer: Новости ===\n")

    # Создаем издателя
    publisher = NewsPublisher()

    # Создаем подписчиков
    alice = Subscriber("Алиса")
    bob = Subscriber("Боб")

    # Подписываемся
    publisher.subscribe(alice)
    publisher.subscribe(bob)

    # Публикуем новость
    publisher.publish_news("Вышел новый Python 3.12!")

    # Отписываемся
    print("\nБоб отписался")
    publisher.unsubscribe(bob)

    # Еще новость
    publisher.publish_news("Новый курс по паттернам!")


if __name__ == "__main__":
    main()