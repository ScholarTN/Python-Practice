
### 1. Lists
#1.Create a list and append elements to it:

l = []
l.append(5)
l.append(10)
print("List after appending:", l)


#2.Pop an element from a list:

l = [5, 10]
l.pop()
print("List after popping:", l)


### 2. Tuples
#1.Create a tuple and access its elements:

t = (5, 10)
print("Tuple:", t)
print("Accessing elements:", t[0], t[1])


#2.Create a tuple from a list:
l = [5, 10]
t = tuple(l)
print("Tuple from list:", t)


### 3. Sets
#1.Create a set and add elements to it:

s = set()
s.add(5)
s.add(10)
print("Set after adding:", s)


#2.Remove an element from a set:

s = {5, 10}
s.remove(5)
print("Set after removing:", s)


### 4. Dictionaries
#1.Create a dictionary and add key-value pairs:
   
d = {}
d["Five"] = 5
d["Ten"] = 10
print("Dictionary:", d)
   

#2.Remove a key-value pair from a dictionary:
d = {"Five": 5, "Ten": 10}
del d["Five"]
print("Dictionary after removing:", d)


### 5. Comprehensions
#1.Use a list comprehension to double the elements of a list:

l = [4, 6, 7, 3, 2, 10, 4]
new_list = [item * 2 for item in l]
print("New list:", new_list)
   

#2.Use a dictionary comprehension to create a dictionary from two lists:

names = ["James", "Mary", "Kate"]
numbers = [10, 20, 15]
some_dictionary = {key: value for key, value in zip(names, numbers)}
print("Dictionary:", some_dictionary)


### 6. Tuple Unpacking
#1. Unpack a tuple into individual variables:
  
details = ("John", 28, "New York")
name, age, city = details
print("Name:", name)
print("Age:", age)
print("City:", city)


#2. Swap two numbers using a tuple:
a, b = 10, 20
print("Before swap:", a, b)
a, b = b, a
print("After swap:", a, b)
   


























