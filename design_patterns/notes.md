# OOP Design Patterns

## Creational

### Singleton

This design pattern ensures only one instance of a class can be created, providing global access to that instance.

This pattern is helpful when we need to control access to some shared resource like a file or database connection. Also helps limit concurrent access to a shared resource.

Just like a global variable, the Singleton pattern lets you access some object from anywhere in the program. However, it also protects that instance from being overwritten by other code.



#### Use cases

Use the Singleton pattern when you need stricter control over global variables.

Unlike global variables, the Singleton pattern guarantees that there’s just one instance of a class. Nothing, except for the Singleton class itself, can replace the cached instance.

Examples:
- file access
- database connections

#### PROS

#### CONS

1. Violates the single responsibility principle!
    - solves 2 problems at once: ensuring only one instance is allowed AND providing a global access point for it
2. Requires special treatment in multithreaded environments such that multiple threads don't create multiple instances
3. Difficult to test

### Relationship to other patterns

- Facade class can be transformed into a Singleton since a single facade object is often sufficient
- Flyweight would resemble Singleton if you somehow managed to reduce all shared states of the objects to just one flyweight object. But there are two fundamental differences between these patterns:
    - There should be only one Singleton instance, whereas a Flyweight class can have multiple instances with different intrinsic states.
    - The Singleton object can be mutable. Flyweight objects are immutable.

