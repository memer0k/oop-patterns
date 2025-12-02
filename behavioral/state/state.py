"""
State.
Плеер с разными состояниями.
"""


class PlayerState:
    """Состояние"""

    def play(self, player):
        pass

    def pause(self, player):
        pass


class PlayingState(PlayerState):
    """Состояние: играет"""

    def play(self, player):
        print("[ПЛЕЕР] Уже играет")

    def pause(self, player):
        print("[ПЛЕЕР] Пауза")
        player.state = PausedState()


class PausedState(PlayerState):
    """Состояние: на паузе"""

    def play(self, player):
        print("[ПЛЕЕР] Возобновление")
        player.state = PlayingState()

    def pause(self, player):
        print("[ПЛЕЕР] Уже на паузе")


class StoppedState(PlayerState):
    """Состояние: остановлен"""

    def play(self, player):
        print("[ПЛЕЕР] Начинаем воспроизведение")
        player.state = PlayingState()

    def pause(self, player):
        print("[ПЛЕЕР] Нельзя поставить на паузу, сначала воспроизведите")


class Player:
    """Контекст"""

    def __init__(self):
        self.state = StoppedState()

    def play(self):
        self.state.play(self)

    def pause(self):
        self.state.pause(self)


# Использование
def main():
    print("=== State: Аудиоплеер ===\n")

    player = Player()

    # Пытаемся поставить на паузу (нельзя)
    player.pause()

    # Воспроизводим
    player.play()

    # Ставим на паузу
    player.pause()

    # Возобновляем
    player.play()

    # Снова ставим на паузу
    player.pause()


if __name__ == "__main__":
    main()