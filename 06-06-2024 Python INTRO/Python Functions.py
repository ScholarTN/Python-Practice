
### Functions with Default Arguments

"""1. Define a function `greet` that takes a name as an argument and prints a greeting message.
      The function should have a default argument for the name, so that if no name is provided,
       it defaults to `"World"`."""


def greet(name = "World"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, World!
greet("SCHOLAR")  # Output: Hello, SCHOLAR!


"""2. Define a function `add_numbers` that takes two numbers as arguments and returns their sum.
      The function should have default arguments for both numbers, so that if no numbers are
       provided, it defaults to `0`."""


def add_numbers(a = 0, b = 0):
    return a + b

print(add_numbers())  # Output: 0
print(add_numbers(2, 3))  # Output: 5


### Functions with Variable Number of Arguments

"""1. Define a function `print_numbers` that takes a variable number of arguments and 
      prints each number."""


def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4, 5)  # Output: 1, 2, 3, 4, 5


"""2. Define a function `average` that takes a variable number of arguments 
      and returns their average."""


def average(*args):
    return sum(args) / len(args)

print(average(1, 2, 3, 4, 5))  # Output: 3.0


### Functions with Keyword Arguments

"""1. Define a function `greet` that takes a name and a greeting message as keyword arguments.
   The function should print the greeting message with the provided name."""

def greet(name, message = "Hello"):
    print(f"{message}, {name}!")

greet("Thubalami", "Hi")  # Output: Hi, Thubalami!
greet("Nkomazana", message = "Goodbye")  # Output: Goodbye, Nkomazana!


"""2. Define a function `calculate_area` that takes the length 
      and width of a rectangle as keyword arguments and returns their product."""


def calculate_area(length, width, unit = "square meters"):
    return length * width

print(calculate_area(length = 2, width = 3))  # Output: 6
print(calculate_area(length = 4, width = 5, unit = "square feet"))  # Output: 20


### Functions with Return Values

"""1. Define a function `add_numbers` that takes two numbers as arguments and returns their sum."""


def add_numbers(a, b):
    return a + b

result = add_numbers(2, 3)
print(result)  # Output: 5


"""2. Define a function `get_max` that takes a list of numbers as an argument 
       and returns the maximum number."""


def get_max(numbers):
    return max(numbers)

numbers = [1, 2, 3, 4, 5]
print(get_max(numbers))  # Output: 5


### Functions with Lambda Functions

"""1. Define a function `double_numbers` that takes a list of numbers as an argument 
      and returns a new list with each number doubled."""


double_numbers = lambda numbers: [num * 2 for num in numbers]
numbers = [1, 2, 3, 4, 5]
print(double_numbers(numbers))  # Output: [2, 4, 6, 8, 10]

"""2. Define a function `filter_even_numbers` that takes a list of numbers as an argument
      and returns a new list with only the even numbers."""


filter_even_numbers = lambda numbers: [num for num in numbers if num % 2 == 0]
numbers = [1, 2, 3, 4, 5]
print(filter_even_numbers(numbers))  # Output: [2, 4]
