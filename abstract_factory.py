from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """Base class for Payment Processors."""

    @abstractmethod
    def make_payment(self, amount: float):
        """Process a payment."""
        ...

class RefundProcessor(ABC):
    """Base class for Refund Processors."""

    @abstractmethod
    def make_refund(self, amount: float):
        """Process a refund."""
        ...


class StripePaymentProcessor(PaymentProcessor):
    """Payment processor for making Stripe payments."""

    def make_payment(self, amount: float):
        """Process a Stripe payment."""
        print(f"Made a Stripe payment of {amount}")


class StripeRefundProcessor(RefundProcessor):
    """Refund processor for making Stripe refunds."""

    def make_refund(self, amount: float):
        """Process a Stripe refund."""
        print(f"Made a Stripe refund of {amount}")


class AdyenPaymentProcessor(PaymentProcessor):
    """Payment processor for making Adyen payments."""

    def make_payment(self, amount: float):
        """Process a Adyen payment."""
        print(f"Made an Adyen payment of {amount}")

class AdyenRefundProcessor(RefundProcessor):
    """Refund processor for making Adyen refunds."""

    def make_refund(self, amount: float):
        """Process a Adyen refund."""
        print(f"Made an Adyen refund of {amount}")


class PaymentService(ABC):
    """An abstract service to handle the making of payments."""

    @abstractmethod
    def create_payment_processor(self):
        """Factory method to create a concrete PaymentProcessor."""
        ...
    
    @abstractmethod
    def create_refund_processor(self):
        """Factory method to create a concrete RefundProcessor."""
        ...

    def make_payment(self, amount: float):
        """Make a payment with the PaymentProcessor"""
        self.verify_config()
        payment_processor = self.create_payment_processor()
        payment_processor.make_payment(amount)
    
    def make_refund(self, amount: float):
        """Make a refund with the RefundProcessor"""
        self.verify_config()
        payment_processor = self.create_refund_processor()
        payment_processor.make_refund(amount)
    
    def verify_config(self):
        """
        Perform some business logic around verifying if the user has
        payments setup.
        """
        print("Verified payment configuration.")


class StripePaymentService(PaymentService):
    """
    A Stripe payment service that instantiates a StripePaymentProcessor
    to handle payments.
    """

    def create_payment_processor(self):
        return StripePaymentProcessor()
    
    def create_refund_processor(self):
        return StripeRefundProcessor()


class AdyenPaymentService(PaymentService):
    """
    An Adyen payment service that instantiates an AdyenPaymentProcessor 
    to handle payments.
    """

    def create_payment_processor(self):
        return AdyenPaymentProcessor()
    
    def create_refund_processor(self):
        return AdyenRefundProcessor()


PAYMENT_SERVICE_MAP = {
        "adyen": AdyenPaymentService,
        "stripe": StripePaymentService,
    }


def get_provider():
    provider = None
    while True:
        provider = input("Use Stripe or Adyen? ").lower()
        if provider in PAYMENT_SERVICE_MAP.keys():
            return provider

def get_function():
    func = None
    while True:
        func = input("Make a payment (p) or a refund (r)? ").lower()
        if func in ('p', 'r'):
            return func


def get_amount():
    amount = None
    while True:
        amount = input("Enter transaction amount: ")
        try:
            amount = float(amount)
            return amount
        except ValueError:
            ...


def main():
    provider = get_provider()
    func = get_function()
    amount = get_amount()

    payment_service = PAYMENT_SERVICE_MAP.get(provider)()

    if func == 'p':
        payment_service.make_payment(amount)
    else:
        payment_service.make_refund(amount)


if __name__ == "__main__":
    main()
