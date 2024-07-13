# SOLID Principles

[Back to main](./README.md)

## Definition

### SINGLE RESPONSIBILITY PRINCIPLE

A class should have one and only one reason to change, meaning that a class should have only one job.

### OPEN CLOSED PRINCIPLE

A class should be open to extension but closed to modification
- This means that a class should be extendable without modifying the class itself.

### LISKOV SUBSTITUTION PRINCIPLE

Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T.
- This means that every subclass or derived class should be substitutable for their base or parent class.

### INTERFACE SEGREGATION PRINCIPLE

A client should never be forced to implement an interface that it doesn’t use, or clients shouldn’t be forced to depend on methods they do not use.

### DEPENDENCY INVERSION PRINCIPLE

Entities must depend on abstractions, not on concretions. It states that the high-level module must not depend on the low-level module, but they should depend on abstractions.

## Which design patterns match up with each principle
