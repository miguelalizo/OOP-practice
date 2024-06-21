# OOP Design Patterns

## Creational Patterns

### Singleton
-------------

This design pattern ensures only one instance of a class can be created, providing global access to that instance.

- Helpful when we need to control access to some shared resource like a file or database connection. Also helps limit concurrent access to a shared resource
- Just like a global variable, the Singleton pattern lets you access some object from anywhere in the program
    - it also protects that instance from being overwritten by other code
        - meaning that somewhere else in the program, you wont be able to create a new instance and "override" the old one because only one can exist

### [Sample Implementation](./creational/singleton.py)

#### Use cases

Use the Singleton pattern when you need stricter control over global variables.

Unlike global variables, the Singleton pattern guarantees that there’s just one instance of a class. Nothing, except for the Singleton class itself, can replace the cached instance.

Example Use Cases:
- file access
- database connections

### Pros and Cons

| Pros  | Cons |
|-------|-------|
| Ensures class has a single instance  | Violates the single responsibility principle! |
| Provides global access point to that instance  | Requires special treatment in multithreaded environments such that multiple threads don't create multiple instances |
| Singleton object is initialized only when it is requested for the fitst time | Difficult to test |


### Relationship to other patterns

- Facade class can be transformed into a Singleton since a single facade object is often sufficient
- Flyweight would resemble Singleton if you somehow managed to reduce all shared states of the objects to just one flyweight object. But there are two fundamental differences between these patterns:
    - There should be only one Singleton instance, whereas a Flyweight class can have multiple instances with different intrinsic states.
    - The Singleton object can be mutable. Flyweight objects are immutable.

