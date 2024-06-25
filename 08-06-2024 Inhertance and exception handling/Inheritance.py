#SINGLE LEVEL
class Parent:
    def __init__(self):
        self.value = "Parent"
        
    def show(self):
        print(self.value)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = "Child"

obj = Child()
obj.show()  # Output: Child

#Multiple Inheritance
class Parent1:
    def __init__(self):
        self.value = "Parent1"
        
    def show1(self):
        print(self.value)

class Parent2:
    def __init__(self):
        self.value = "Parent2"
        
    def show2(self):
        print(self.value)

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)

obj = Child()
obj.show1()  # Output: Parent1
obj.show2()  # Output: Parent2


#Multilevel Inheritance
class GrandParent:
    def __init__(self):
        self.value = "GrandParent"
        
    def show(self):
        print(self.value)

class Parent(GrandParent):
    def __init__(self):
        super().__init__()
        self.value = "Parent"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = "Child"

obj = Child()
obj.show()  # Output: Child

#Hierarchical inheritance
class Parent:
    def __init__(self):
        self.value = "Parent"
        
    def show(self):
        print(self.value)

class Child1(Parent):
    def __init__(self):
        super().__init__()
        self.value = "Child1"

class Child2(Parent):
    def __init__(self):
        super().__init__()
        self.value = "Child2"

obj1 = Child1()
obj1.show()  # Output: Child1

obj2 = Child2()
obj2.show()  # Output: Child2




#Create a class Animal with attributes name and species. Create a derived class Mammal that inherits from Animal.
#  Add a new attribute mammal_type to the Mammal class. Create an instance of the Mammal class
#  and print its attributes.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Mammal(Animal):
    def __init__(self, name, species, mammal_type):
        super().__init__(name, species)
        self.mammal_type = mammal_type

# Create an instance of the Mammal class
mammal = Mammal("Lion", "Feline", "Carnivore")

# Print the attributes
print(f"Name: {mammal.name}")
print(f"Species: {mammal.species}")
print(f"Mammal Type: {mammal.mammal_type}")

""" EXPECTED OUTPUT"""
# Name: Lion
# Species: Feline
# Mammal Type: Carnivore



