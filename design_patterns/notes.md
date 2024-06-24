# OOP Design Patterns

## Creational Patterns
----------------------

### Singleton
-------------

This design pattern ensures only one instance of a class can be created, providing global access to that instance.

- Helpful when we need to control access to some shared resource like a file or database connection. Also helps limit concurrent access to a shared resource
- Just like a global variable, the Singleton pattern lets you access some object from anywhere in the program
    - it also protects that instance from being overwritten by other code
        - meaning that somewhere else in the program, you wont be able to create a new instance and "override" the old one because only one can exist

#### [Sample Implementation](./creational/singleton.py)

#### Use cases

Use the Singleton pattern when you need stricter control over global variables.

Unlike global variables, the Singleton pattern guarantees that there’s just one instance of a class. Nothing, except for the Singleton class itself, can replace the cached instance.

Dicrector (optional):
- You can go further and extract a series of calls to the builder steps you use to construct a product into a separate class called director. The director class defines the order in which to execute the building steps, while the builder provides the implementation for those steps.
- Having a director class in your program isn’t strictly necessary. You can always call the building steps in a specific order directly from the client code. However, the director class might be a good place to put various construction routines so you can reuse them across your program.
- In addition, the director class completely hides the details of product construction from the client code. The client only needs to associate a builder with a director, launch the construction with the director, and get the result from the builder.

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

### Builder
----------

Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

A builder doesn’t expose the unfinished product while running construction steps. This prevents the client code from fetching an incomplete result.

#### [Sample Implementation](./creational/builder.py)

#### Use cases

- When an a complex object has many optional fields in constructor
- Creation of the complex object can be divided into a series of steps
    - Also if these steps require validation, then it is algo a good reason to outsource the building steps to a Builder as opposed to having that logic in the object itself
- when you want your code to be able to create different representations of some product (for example, stone and wooden houses)
- when construction of various representations of the product involves similar steps that differ only in the details.
    -The base builder interface defines all possible construction steps, and concrete builders implement these steps to construct particular representations of the product. Meanwhile, the director class (optional) guides the order of construction.
- to construct Composite trees or other complex objects.
    - The Builder pattern lets you construct products step-by-step. You could defer execution of some steps without breaking the final product. You can even call steps recursively, which comes in handy when you need to build an object tree.

A builder doesn’t expose the unfinished product while running construction steps. This prevents the client code from fetching an incomplete result.

Example Use Cases:


### Pros and Cons

| Pros  | Cons |
|-------|-------|
| Step by step construction ofg complex objects | Complexity of the code base can increase due to creating more classes |
| Can reuse same construction code for building different representation of products |  |
| Single responsibility principle is enabled since creation logic can be outsourced from the object/class itself |  |


### Relationship to other patterns

- Many designs start by using Factory Method (less complicated and more customizable via subclasses) and evolve toward Abstract Factory, Prototype, or Builder (more flexible, but more complicated)
    - Builder focuses on constructing complex objects step by step
    - Abstract Factory specializes in creating families of related objects
    - Abstract Factory returns the product immediately, whereas Builder lets you run some additional construction steps before fetching the product
- Can be implemented as a Singleton
- You can use Builder when creating complex Composite trees because you can program its construction steps to work recursively
- You can combine Builder with Bridge
    - the director class plays the role of the abstraction, while different builders act as implementations

### Prototype
-------------
The Prototype pattern delegates the cloning process to the actual objects that are being cloned.

The pattern declares a common interface for all objects that support cloning. This interface lets you clone an object without coupling your code to the class of that object. Usually, such an interface contains just a single clone method.

An object that supports cloning is called a prototype.

Prototype pattern provides a way to replicate an object.

- This is helpful because (in some languages) the fields needed to copy an object can be private/inaccessible.
- Additionally, this helps decouple your code from the class that you are trying to make a copy from.
    - What if you're trying to create a copy/clone of an object and so you write code to do that for all it's fields. Then the class of the copied object changes?
        - Your code is coupled and is now out of date
        - Therefore it is better for the class itself to provide an API for copying/cloning if it is necessary
- When your objects have dozens of fields and hundreds of possible configurations, cloning them might serve as an alternative to subclassing


#### [Sample Implementation](./creational/prototype.py)

Python provides its own interface of Prototype via `copy.copy` and `copy.deepcopy` functions. And any class that wants to implement custom implementations have to override `__copy__` and `__deepcopy__` member functions.

#### Use cases

- When your objects have dozens of fields and hundreds of possible configurations, cloning them might serve as an alternative to subclassing

#### Pros and Cons

| Pros  | Cons |
|-------|-------|
|  You can clone objects without coupling to their concrete classes. |  Cloning complex objects that have circular references might be very tricky. |
| You can get rid of repeated initialization code in favor of cloning pre-built prototypes.  | |
|  You can produce complex objects more conveniently. | |
| You get an alternative to inheritance when dealing with configuration presets for complex objects. | |


#### Relationship to other pattenrs

- Many designs start by using Factory Method (less complicated and more customizable via subclasses) and evolve toward Abstract Factory, Prototype, or Builder (more flexible, but more complicated).
- Abstract Factory classes are often based on a set of Factory Methods, but you can also use Prototype to compose the methods on these classes.
- Prototype can help when you need to save copies of Commands into history.
- Designs that make heavy use of Composite and Decorator can often benefit from using Prototype. Applying the pattern lets you clone complex structures instead of re-constructing them from scratch.
- Prototype isn’t based on inheritance, so it doesn’t have its drawbacks. On the other hand, Prototype requires a complicated initialization of the cloned object. Factory Method is based on inheritance but doesn’t require an initialization step.
- Sometimes Prototype can be a simpler alternative to Memento. This works if the object, the state of which you want to store in the history, is fairly straightforward and doesn’t have links to external resources, or the links are easy to re-establish.
- Abstract Factories, Builders and Prototypes can all be implemented as Singletons.
