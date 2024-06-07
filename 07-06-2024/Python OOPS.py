
### 1. Classes and Objects

#### Definition:
#- **Class**: A blueprint or template that defines the properties and behavior of an object.
#- **Object**: An instance of a class, which has its own set of attributes (data) and methods (functions).

#### Example:

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def start(self):
        print(f"Starting the {self.color} {self.model}.")

# Create objects
my_car1 = Car("Red", "Toyota")
my_car2 = Car("Blue", "Honda")

# Use methods
my_car1.start()  # Output: Starting the Red Toyota.
my_car2.start()  # Output: Starting the Blue Honda.


### 2. Constructors and Destructors

#### Definition:
#- **Constructor**: A special method that is automatically called when an object is created.
#- **Destructor**: A special method that is automatically called when an object is destroyed.

#### Example:

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def __del__(self):
        print(f"Destroying {self.color} {self.model}.")

# Create objects
my_car1 = Car("Red", "Toyota")
my_car2 = Car("Blue", "Honda")

# Use methods
my_car1.start()  # Output: Starting the Red Toyota.
my_car2.start()  # Output: Starting the Blue Honda.

# Destroy objects
del my_car1
del my_car2


### 3. Inheritance

#### Definition:
#- **Inheritance**: A mechanism where a new class can inherit properties and behavior from an existing class.

#### Example:

class Vehicle:
    def __init__(self, color):
        self.color = color

    def start(self):
        print(f"Starting the {self.color} vehicle.")

class Car(Vehicle):
    def __init__(self, color, model):
        super().__init__(color)
        self.model = model

    def start(self):
        print(f"Starting the {self.color} {self.model}.")

# Create objects
my_car = Car("Red", "Toyota")

# Use methods
my_car.start()  # Output: Starting the Red Toyota.


### 4. Polymorphism

#### Definition:
#- **Polymorphism**: The ability of an object to take on multiple forms.

#### Example:

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create objects
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Use methods
print(circle.area())  # Output: 78.5
print(rectangle.area())  # Output: 24

### 5. Encapsulation

#### Definition:
#- **Encapsulation**: The concept of bundling data and methods that operate on that data within a single unit.

#### Example:

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Create objects
account = BankAccount(1000)

# Use methods
account.deposit(500)
print(account.get_balance())  # Output: 1500


### 6. Abstraction

#### Definition:
#- **Abstraction**: The concept of showing only essential features of an object and hiding its internal details.

#### Example:

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Create objects
account = BankAccount(1000)

# Use methods
account.deposit(500)
print(account.get_balance())  # Output: 1500


### 7. Composition

#### Definition:
#- **Composition**: The concept of creating objects from other objects.

#### Example:

class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

# Create objects
address = Address("Bulawayo", "CA", "12345")
person = Person("Scholar TN", address)

# Use methods
print(person.name)  # Output: Scholar TN
print(person.address.street)  # Bulawayo CA 12345

### 8. Operator Overloading

#### Definition:
#- **Operator Overloading**: The ability to redefine the behavior of operators for a class.

#### Example:

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Create objects
vector1 = Vector(1, 2)
vector2 = Vector(3, 4)

# Use methods
result = vector1 + vector2
print(result)  # Output: (4, 6)


### 9. Abstract Classes

#### Definition:
#- **Abstract Class**: A class that cannot be instantiated and is intended to be inherited by other classes.

#### Example:
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Create objects
circle = Circle(5)

# Use methods
print(circle.area())  # Output: 78.5

### 10. Interfaces

#### Definition:
#- **Interface**: A contract that specifies a set of methods that must be implemented 
#     by any class that implements it.

#### Example:

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Document(Printable):
    def print(self):
        print("Printing a document.")

class Image(Printable):
    def print(self):
        print("Printing an image.")

# Create objects
document = Document()
image = Image()

# Use methods
document.print()  # Output: Printing a document.
image.print()  # Output: Printing an image.

### 11. Singleton

#### Definition:
#- **Singleton**: A design pattern that ensures a class has only one instance and provides 
#     a global point of access to that instance.

#### Example:

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            print("Singleton initialized.")

# Create objects
singleton1 = Singleton()
singleton2 = Singleton()

# Use methods
print(singleton1 is singleton2)  # Output: True


### 12. Factory Method

#### Definition:
#- **Factory Method**: A design pattern that provides a way to create objects without specifying the 
#    exact class of object that will be created.

#### Example:

class VehicleFactory:
    def create_vehicle(self, type):
        if type == "car":
            return Car()
        elif type == "truck":
            return Truck()
        else:
            raise ValueError("Invalid vehicle type.")

class Car:
    def __init__(self):
        print("Creating a car.")

class Truck:
    def __init__(self):
        print("Creating a truck.")

# Create objects
factory = VehicleFactory()
car = factory.create_vehicle("car")
truck = factory.create_vehicle("truck")

# Use methods
car  # Output: Creating a car.
truck  # Output: Creating a truck.


### 13. Observer

#### Definition:
#- **Observer**: A design pattern that allows objects to be notified of changes to other objects 
#    without having a direct reference to them.

#### Example:

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

class Observer:
    def update(self):
        pass

class ConcreteObserver(Observer):
    def update(self):
        print("Observer updated.")

# Create objects
subject = Subject()
observer = ConcreteObserver()

# Attach observer
subject.attach(observer)

# Notify observer
subject.notify()  # Output: Observer updated.


### 14. Decorator

#### Definition:
#- **Decorator**: A design pattern that allows behavior to be added to an object, either statically or 
#      dynamically, without affecting the object's external interface.

#### Example:

class Coffee:
    def cost(self):
        return 1.00

    def ingredients(self):
        return "Coffee"

class Milk(Coffee):
    def cost(self):
        return super().cost() + 0.50

    def ingredients(self):
        return super().ingredients() + ", Milk"

class Sugar(Coffee):
    def cost(self):
        return super().cost() + 0.25

    def ingredients(self):
        return super().ingredients() + ", Sugar"

# Create objects
coffee = Coffee()
milk = Milk()
sugar = Sugar()

# Use methods
print(coffee.cost())  # Output: 1.0
print(milk.ingredients())  # Output: Coffee, Milk
print(sugar.ingredients())  # Output: Coffee, Sugar


### 15. Command

#### Definition:
#- **Command**: A design pattern that encapsulates a request as an object,
#      thereby letting you parameterize clients with queues, logs, and so on.

#### Example:

class Command:
    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receiver, action):
        self.receiver = receiver
        self.action = action

    def execute(self):
        self.receiver.action()

class Receiver:
    def action(self):
        print("Action performed.")

# Create objects
receiver = Receiver()
command = ConcreteCommand(receiver, receiver.action)

# Use methods
command.execute()  # Output: Action performed.

### 16. Iterator

#### Definition:
#- **Iterator**: A design pattern that allows you to traverse a collection of objects without exposing
#         its underlying representation.

#### Example:

class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection)

    def next(self):
        result = self.collection[self.index]
        self.index += 1
        return result

class Collection:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return Iterator(self.items)

# Create objects
collection = Collection([1, 2, 3, 4, 5])

# Use methods
for item in collection:
    print(item)  # Output: 1, 2, 3, 4, 5


### 17. State

#### Definition:
#- **State**: A design pattern that allows an object to change its behavior when its internal state changes.

#### Example:

class State:
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("Handling state A.")

class ConcreteStateB(State):
    def handle(self):
        print("Handling state B.")

class Context:
    def __init__(self):
        self.state = ConcreteStateA()

    def change_state(self, state):
        self.state = state

    def handle(self):
        self.state.handle()

# Create objects
context = Context()

# Use methods
context.handle()  # Output: Handling state A.
context.change_state(ConcreteStateB())
context.handle()  # Output: Handling state B.

### 18. Strategy

#### Definition:
#- **Strategy**: A design pattern that defines a family of algorithms, encapsulates each one,
#       and makes them interchangeable.

#### Example:

class Strategy:
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Executing strategy A.")

class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Executing strategy B.")

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self):
        self.strategy.execute()

# Create objects
strategy_a = ConcreteStrategyA()
strategy_b = ConcreteStrategyB()
context = Context(strategy_a)

# Use methods
context.execute()  # Output: Executing strategy A.
context.strategy = strategy_b
context.execute()  # Output: Executing strategy B.


### 19. Template Method

#### Definition:
##- **Template Method**: A design pattern that defines the skeleton of an algorithm in the superclass
#      but lets subclasses override specific steps of the algorithm without changing its structure.

#### Example:
class TemplateMethod:
    def template_method(self):
        self.step1()
        self.step2()

    def step1(self):
        pass

    def step2(self):
        pass

class ConcreteTemplateMethodA(TemplateMethod):
    def step1(self):
        print("Step 1 A.")

    def step2(self):
        print("Step 2 A.")

class ConcreteTemplateMethodB(TemplateMethod):
    def step1(self):
        print("Step 1 B.")

    def step2(self):
        print("Step 2 B.")

# Create objects
template_method_a = ConcreteTemplateMethodA()
template_method_b = ConcreteTemplateMethodB()

# Use methods
template_method_a.template_method()  # Output: Step 1 A., Step 2 A.
template_method_b.template_method()  # Output: Step 1 B., Step 2 B.


### 20. Visitor

#### Definition:
###- **Visitor**: A design pattern that allows you to perform operations on a collection of objects without 
#        modifying the classes of the objects themselves.

#### Example:
class Visitor:
    def visit(self, element):
        pass

class ConcreteVisitor(Visitor):
    def visit(self, element):
        print(f"Visiting {element}.")

class Element:
    def accept(self, visitor):
        visitor.visit(self)

class ConcreteElement(Element):
    def accept(self, visitor):
        visitor.visit(self)

# Create objects
element = ConcreteElement()
visitor = ConcreteVisitor()

# Use methods
element.accept(visitor)  # Output: Visiting ConcreteElement.