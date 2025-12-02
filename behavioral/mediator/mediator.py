"""
Mediator.
Чат-комната как посредник между пользователями.
"""


class ChatRoom:
    """Посредник"""

    def send_message(self, user, message):
        print(f"[ЧАТ] {user}: {message}")


class User:
    """Коллега"""

    def __init__(self, name, chat_room):
        self.name = name
        self.chat_room = chat_room

    def send(self, message):
        self.chat_room.send_message(self.name, message)


# Использование
def main():
    print("=== Mediator: Чат-комната ===\n")

    # Создаем посредника
    chat = ChatRoom()

    # Создаем пользователей
    alice = User("Алиса", chat)
    bob = User("Боб", chat)
    charlie = User("Чарли", chat)

    # Общаемся через посредника
    alice.send("Привет всем!")
    bob.send("Привет, Алиса!")
    charlie.send("Как дела?")


if __name__ == "__main__":
    main()