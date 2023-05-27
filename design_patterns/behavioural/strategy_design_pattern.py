'''
Imagine you are developing a payment processing system that needs to support multiple payment gateways such as PayPal, 
Stripe, and Square. Each payment gateway has its own API and unique implementation details. In this scenario, you can
apply the Strategy design pattern to handle different payment gateways interchangeably.
'''

class PaymentGateway:
    def process_payment(self, amount):
        raise NotImplementedError()


class PayPalGateway(PaymentGateway):
    def process_payment(self, amount):
        # Code to process payment via PayPal API
        print(f"Processing payment of {amount} USD using PayPal")


class StripeGateway(PaymentGateway):
    def process_payment(self, amount):
        # Code to process payment via Stripe API
        print(f"Processing payment of {amount} USD using Stripe")


class SquareGateway(PaymentGateway):
    def process_payment(self, amount):
        # Code to process payment via Square API
        print(f"Processing payment of {amount} USD using Square")


class PaymentProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount):
        self.payment_gateway.process_payment(amount)


# Implementation
payment_processor = PaymentProcessor(PayPalGateway())
payment_processor.process_payment(100)

payment_processor.payment_gateway = StripeGateway()
payment_processor.process_payment(50)

# Explanation
'''
In the code above, we have a PaymentGateway abstract base class that defines the interface for processing payments. 
It declares the process_payment method, which should be implemented by concrete gateway classes.

The PayPalGateway, StripeGateway, and SquareGateway are concrete implementations of the PaymentGateway class. 
Each gateway provides its own implementation of the process_payment method, specific to the corresponding API.

The PaymentProcessor class represents the context or the client that uses the payment gateways. It has a reference to 
the current payment gateway and provides a process_payment method, which delegates the payment processing to the 
selected gateway.
'''