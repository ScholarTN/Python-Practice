
try:
    # Code that might raise an exception
    ...
except ExceptionType1:
    # Code to handle ExceptionType1
    ...
except ExceptionType2:
    # Code to handle ExceptionType2
    ...
except:
    # Code to handle any other exception
    ...
else:
    # Code to be executed if no exception is raised
    ...
finally:
    # Code to be executed regardless of whether an exception was raised or not
    ...



# Write a function that takes two numbers as input and returns their division. Handle the case when the divisor is zero.


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {result}")

divide_numbers(10, 2)  # Output: Result: 5.0
divide_numbers(5, 0)   # Output: Error: Division by zero is not allowed.



# Write a program that reads a file and prints its contents. Handle the case when the file doesn't exist.


try:
    with open("file.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: File not found.")


# Write a function that takes a list of numbers and returns their sum.
#  Handle the case when a non-numeric value is present in the list.


def sum_numbers(numbers):
    total = 0
    try:
        for num in numbers:
            total += num
    except TypeError:
        print("Error: Non-numeric value found in the list.")
    else:
        print(f"Sum: {total}")

sum_numbers([1, 2, 3, 4, 5])  # Output: Sum: 15
sum_numbers([1, 2, 'a', 4, 5])  # Output: Error: Non-numeric value found in the list.


# Write a program that takes user input for a number and raises a custom exception if the number is negative.


class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise NegativeNumberError("Error: Negative numbers are not allowed.")
except NegativeNumberError as e:
    print(e)
else:
    print(f"You entered: {num}")
