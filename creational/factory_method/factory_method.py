"""
Фабричный метод.
Создание разных типов уведомлений.
"""

from abc import ABC, abstractmethod


# 1. Продукт - Уведомление
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


# 2. Конкретные продукты
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"[ЭМУЛЯЦИЯ] Отправка email: {message}")


class SMSNotification(Notification):
    def send(self, message: str):
        print(f"[ЭМУЛЯЦИЯ] Отправка SMS: {message[:20]}...")


class PushNotification(Notification):
    def send(self, message: str):
        print(f"[ЭМУЛЯЦИЯ] Push-уведомление: {message}")


# 3. Создатель - Сервис уведомлений
class NotificationService(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def notify(self, message: str):
        notifier = self.create_notification()
        notifier.send(message)


# 4. Конкретные создатели
class EmailService(NotificationService):
    def create_notification(self) -> Notification:
        return EmailNotification()


class SMSService(NotificationService):
    def create_notification(self) -> Notification:
        return SMSNotification()


class PushService(NotificationService):
    def create_notification(self) -> Notification:
        return PushNotification()


# 5. Клиентский код
def main():
    print("=== Фабричный метод: Уведомления ===\n")

    # Создаем сервисы
    email_service = EmailService()
    sms_service = SMSService()
    push_service = PushService()

    # Отправляем уведомления (не знаем конкретные классы)
    services = [
        ("📧 Email", email_service),
        ("📱 SMS", sms_service),
        ("🔔 Push", push_service)
    ]

    for name, service in services:
        print(f"{name}: ", end="")
        service.notify("Ваш заказ №12345 готов!")

    print("\n✅ Все отправлено!")


if __name__ == "__main__":
    main()