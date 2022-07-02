# Abstract Factory Design Pattern

The Abstract Factory pattern is similar to the Factory Method pattern.
The difference is that it lets you create groups of related objects without specifying their concrete classes.

It helps you to adhere to:
- Single Responsibility Principle
- Open/Closed Principle

Use it when:
- Your code must work with related groups of products but you don't want to couple it to their specific concrete classes
- You want your code to be highly extensible
- You want to maintain and reuse a pool of resources


## The example:
This example centres around two payment processors; Stripe and Adyen.

Imagine we have a system that must support many different payment processors. The processor used is based on a user's payment configuration.

We will use the Abstract Factory for several reasons:
- We can separate both payment processor and refund processor creation logic from where they will be used. This allows us to decouple our business logic from specific payment processors.
- We can consider Stripe/Adyen payment and refund processors to be within the same group and thus share factories.
- We can very easily add new payment processor groups in the future, without modifying our existing logic.

## Class Diagram:

![Class Diagram](./class_diagrams.png?raw=true "Class Diagram")