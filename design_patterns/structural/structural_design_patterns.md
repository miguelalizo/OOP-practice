# Structural Design Patterns

## Adapter


The Adapter pattern is a structural design pattern that facilitates the interaction between two interfaces that are incompatible or cannot work together directly. It acts as a bridge, allowing objects with different interfaces to collaborate.

The primary goal of the Adapter pattern is to ensure that client code can work with classes it was not initially designed to support. It achieves this without altering the source code of either the client or the adaptee (the class with the incompatible interface).

- An adapter is a special object that converts the interface of one object so that another object can understand it.
- An adapter wraps one of the objects to hide the complexity of conversion happening behind the scenes. The wrapped object isn’t even aware of the adapter. For example, you can wrap an object that operates in meters and kilometers with an adapter that converts all of the data to imperial units such as feet and miles.
- Adapters can not only convert data into various formats but can also help objects with different interfaces collaborate. Here’s how it works:
    - The adapter gets an interface, compatible with one of the existing objects.
    - Using this interface, the existing object can safely call the adapter’s methods.
    - Upon receiving a call, the adapter passes the request to the second object, but in a format and order that the second object expects.
- Sometimes it’s even possible to create a two-way adapter that can convert the calls in both directions.

- this is like impl From in rust adapting one format `into` another

![adapter](./static/adapter.png)

- Client: Contains program logic.
- Client Interface: Defines collaboration rules.
- Service: A useful, but incompatible, class.
- Adapter: Bridges client and service, translating calls.
- Decoupling: Client code remains adaptable without changes.

Use the Adapter class when you want to use some existing class, but its interface isn’t compatible with the rest of your code.
- The Adapter pattern lets you create a middle-layer class that serves as a translator between your code and a legacy class, a 3rd-party class or any other class with a weird interface.

Use the pattern when you want to reuse several existing subclasses that lack some common functionality that can’t be added to the superclass.
- You could extend each subclass and put the missing functionality into new child classes. **However, you’ll need to duplicate the code across all of these new classes, which smells really bad.**
- The much more elegant solution would be to put the missing functionality into an adapter class. Then you would wrap objects with missing features inside the adapter, gaining needed features dynamically. For this to work, the target classes must have a common interface, and the adapter’s field should follow that interface. This approach looks very similar to the Decorator pattern.

### Key components

1. Target Interface: The target interface defines the contract that the client code expects. It is the interface the adapter will conform to, allowing the client to interact with the adaptee seamlessly.
2. Adaptee: The adaptee is the class or component with an incompatible interface. It’s the object you want to make use of but cannot interact with directly from the client. Usually a 3rd party or legacy service.
3. Adapter: The intermediary that bridges the gap between the target interface and the adaptee. It translates calls from the client in a way that the adaptee can understand and respond to.

### [Sample implementation](./adapter.py)

### How to implement

1. Make sure that you have at least two classes with incompatible interfaces:
    - A useful service class, which you can’t change (often 3rd-party, legacy or with lots of existing dependencies).
    - One or several client classes that would benefit from using the service class.
2. Declare the client interface and describe how clients communicate with the service.
3. Create the adapter class and make it follow the client interface. Leave all the methods empty for now.
4. Add a field to the adapter class to store a reference to the service object. The common practice is to initialize this field via the constructor, but sometimes it’s more convenient to pass it to the adapter when calling its methods.
5. One by one, implement all methods of the client interface in the adapter class. The adapter should delegate most of the real work to the service object, handling only the interface or data format conversion.
6. Clients should use the adapter via the client interface. This will let you change or extend the adapters without affecting the client code.

### Examples:
Usage examples: The Adapter pattern is pretty common in Python code. It’s very often used in systems based on some legacy code. In such cases, Adapters make legacy code work with modern classes.

Identification: Adapter is recognizable by a constructor which takes an instance of a different abstract/interface type. When the adapter receives a call to any of its methods, it translates parameters to the appropriate format and then directs the call to one or several methods of the wrapped object.

### Pros and Cons

| Pros  | Cons |
|-------|-------|
| Single responsibility principle: separates the interface or data conversion code from the primary business logic  |  The overall complexity of the code increases because you need to introduce a set of new interfaces and classes. Sometimes it’s simpler just to change the service class so that it matches the rest of your code. |
| Open close principle: You can introduce new types of adapers into the program without vbreaking the existing client code as long as they work with the adapters through the client interface |  |

### Relationship to other patterns
- Bridge is usually designed up-front, letting you develop parts of an application independently of each other. On the other hand, Adapter is commonly used with an existing app to make some otherwise-incompatible classes work together nicely.
- Adapter provides a completely different interface for accessing an existing object. On the other hand, with the Decorator pattern the interface either stays the same or gets extended. In addition, Decorator supports recursive composition, which isn’t possible when you use Adapter.
- With Adapter you access an existing object via different interface. With Proxy, the interface stays the same. With Decorator you access the object via an enhanced interface.
- Facade defines a new interface for existing objects, whereas Adapter tries to make the existing interface usable. Adapter usually wraps just one object, while Facade works with an entire subsystem of objects.
- Bridge, State, Strategy (and to some degree Adapter) have very similar structures. Indeed, all of these patterns are based on composition, which is delegating work to other objects. However, they all solve different problems. A pattern isn’t just a recipe for structuring your code in a specific way. It can also communicate to other developers the problem the pattern solves.
