"""
Strategy.
Разные способы оплаты.
"""


class PaymentStrategy:
    """Стратегия"""

    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    """Оплата картой"""

    def pay(self, amount):
        print(f"[КАРТА] Оплачено {amount} руб.")


class PayPalPayment(PaymentStrategy):
    """Оплата PayPal"""

    def pay(self, amount):
        print(f"[PAYPAL] Оплачено {amount} руб.")


class CryptoPayment(PaymentStrategy):
    """Оплата криптовалютой"""

    def pay(self, amount):
        print(f"[КРИПТО] Оплачено {amount} USDT")


class ShoppingCart:
    """Контекст"""

    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        print(f"\nОформление заказа на {amount} руб.:")
        self.payment_strategy.pay(amount)


# Использование
def main():
    print("=== Strategy: Оплата ===\n")

    # Разные стратегии оплаты
    cart1 = ShoppingCart(CreditCardPayment())
    cart1.checkout(5000)

    cart2 = ShoppingCart(PayPalPayment())
    cart2.checkout(3000)

    cart3 = ShoppingCart(CryptoPayment())
    cart3.checkout(2000)


if __name__ == "__main__":
    main()