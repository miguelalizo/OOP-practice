from __future__ import annotations
from enum import Enum


class PayPalGateway:
    def process_payment(self, amount):
        return f"PayPal: ${amount} payment processed:"


class StripeGateway:
    def process_payment(self, amount):
        return f"Stripe: ${amount} payment processed:"


class CryptoGateway:
    def process_payment(self, amount):
        return f"Crypto: ${amount} payment processed:"


class PaymentGateway(Enum):
    Stripe = 0
    PayPal = 1
    Crypto = 2


class PaymentFacade:
    def __init__(self):
        self._paypal = PayPalGateway()
        self._stripe = StripeGateway()
        self._crypto = CryptoGateway()

    def process_payment(self, amount: float, gateway: PaymentGateway):
        if gateway == PaymentGateway.Stripe:
            return self._stripe.process_payment(amount)
        if gateway == PaymentGateway.PayPal:
            return self._stripe.process_payment(amount)
        if gateway == PaymentGateway.Crypto:
            return self._crypto.process_payment(amount)
        raise Exception(f"Gateway {gateway} not supported")


if __name__ == "__main__":
    payment_processor = PaymentFacade()
    print(payment_processor.process_payment(32.49, PaymentGateway.Stripe))
    print(payment_processor.process_payment(63.02, PaymentGateway.PayPal))
    print(payment_processor.process_payment(10.11, PaymentGateway.Crypto))
