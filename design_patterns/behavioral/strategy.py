from __future__ import annotations
from abc import ABC, abstractmethod


# 1. Create strategy interface
class PaymentStrategy(ABC):
    """Strategy interface"""

    @abstractmethod
    def pay(self, amount):
        pass


# 2. Create concrete strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"CreditCardPayment: processed payment of ${amount}")


class PaypalPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"PaypalPayment: processed payment of ${amount}")


class BankTransferPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"BankTransferPayment: processed payment of ${amount}")


# 3. Create context class
class PaymentContext:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy: PaymentStrategy) -> None:
        self.payment_strategy = payment_strategy

    def make_payment(self, amount: float) -> None:
        self.payment_strategy.pay(amount)


if __name__ == "__main__":
    credit = CreditCardPayment()
    paypal = PaypalPayment()
    bank = BankTransferPayment()

    context = PaymentContext(credit)
    context.make_payment(10.0)

    context.set_payment_strategy(paypal)
    context.make_payment(15.0)

    context.set_payment_strategy(bank)
    context.make_payment(20.0)
