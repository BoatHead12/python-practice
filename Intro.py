"""
Python Introduction
Key Important Concepts:
1. Python is an interpreted, high-level, general-purpose programming language.
2. Python's design philosophy emphasizes code readability with its notable use of significant whitespace.
3. Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
4. Python has a large standard library that provides tools suited to many tasks.
"""

# Python program that prints 'Hello, World!' to the console:
print("Hello, World!")

# Python program that takes user input and prints it:
user_input = input("Enter something: ")
print("You entered:", user_input)  # >> You entered: <user_input>

# Python program that demonstrates basic arithmetic operations:
a = 10
b = 5
print("Addition:", a + b)  # >> Addition: 15
print("Subtraction:", a - b)  # >> Subtraction: 5
print("Multiplication:", a * b)  # >> Multiplication: 50
print("Division:", a / b)  # >> Division: 2.0


# Python program that demonstrates a simple function:
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))  # >> Hello, Alice!


# Python program that demonstrates a simple class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


person1 = Person("Bob", 30)
print(person1.introduce())  # >> My name is Bob and I am 30 years old.

# class : Explaination: A class is a blueprint for creating objects (instances) that have similar attributes and methods.
# class is a fundamental concept in object-oriented programming (OOP) that allows you to define your own data types and encapsulate related data and behavior.
# class is a way to create user-defined data structures that can hold both data (attributes) and functions (methods) that operate on that data.


# Python program that demonstrates a simple loop:
for i in range(5):
    print(i)  # >> 0, 1, 2, 3, 4

# Python program that demonstrates a simple conditional statement:
x = 10
if x > 5:
    print("x is greater than 5")  # >> x is greater than 5

# Python program that demonstrates a simple list:
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)  # >> List: [1, 2, 3, 4, 5]

# Python program that demonstrates a simple dictionary:
my_dict = {"name": "Alice", "age": 25}
print("Dictionary:", my_dict)  # >> Dictionary: {'name': 'Alice', 'age': 25}

# Python program that demonstrates a simple tuple:
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)  # >> Tuple: (1, 2, 3)

# Python program that demonstrates a simple set:
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)  # >> Set: {1, 2, 3, 4, 5}

# Python program that demonstrates a simple string manipulation:
my_string = "Hello, World!"
print("Uppercase:", my_string.upper())  # >> Uppercase: HELLO, WORLD!
print("Lowercase:", my_string.lower())  # >> Lowercase: hello, world!

# Python program that demonstrates a simple file operation:
with open("example.txt", "w") as file:
    file.write("This is an example file.")

with open("example.txt", "r") as file:
    content = file.read()
    print("File content:", content)  # >> File content: This is an example file.

# Python program that demonstrates exception handling:
try:
    result = 10 / 0
except ZeroDivisionError:
    print(
        "Error: Division by zero is not allowed."
    )  # >> Error: Division by zero is not allowed.

# Python program that demonstrates importing a module:
import math

print("Square root of 16:", math.sqrt(16))  # >> Square root of 16: 4.0

# Python program that demonstrates a simple list comprehension:
squared_numbers = [x**2 for x in range(5)]
print("Squared numbers:", squared_numbers)  # >> Squared numbers: [0, 1, 4, 9, 16]

# Python program that demonstrates a simple lambda function:
add = lambda x, y: x + y
print("Addition using lambda:", add(5, 3))  # >> Addition using lambda: 8


# Python program that demonstrates a simple generator:
def simple_generator():
    yield 1
    yield 2
    yield 3


gen = simple_generator()
for value in gen:
    print(value)  # >> 1, 2, 3


# Python program that demonstrates a simple decorator:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


print("Decorator Example:")


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
# >> Something is happening before the function is called.
# >> Hello!
# >> Something is happening after the function is called.


# Python program that demonstrates a simple recursion:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))  # >> Factorial of 5: 120

# Python program that demonstrates a simple regular expression:
import re

pattern = r"\d+"
text = "There are 123 apples and 456 oranges."
matches = re.findall(pattern, text)
print("Matches:", matches)  # >> Matches: ['123', '456']


# Python program that demonstrates a simple context manager:
class MyContextManager:
    def __enter__(self):
        print("Entering the context.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context.")


with MyContextManager() as cm:
    print("Inside the context.")
# >> Entering the context.
# >> Inside the context.
# >> Exiting the context.    ##Explanation: A context manager is a Python object that defines the runtime context to be established when executing a with statement. It allows you to allocate and release resources precisely when you want to. The most widely used example of context managers is the open() function, which is used for file handling.

# Python program that demonstrates a simple multithreading:
import threading


def print_numbers():
    for i in range(5):
        print(i)


# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()
thread2.join()

# >> 0, 1, 2, 3, 4
##Explanation: Multithreading is a technique in programming that allows multiple threads (smaller units of a process) to run concurrently within a single program. In Python, the threading module provides a way to create and manage threads. Each thread can execute a function independently, allowing for parallel execution of tasks. However, due to Python's Global Interpreter Lock (GIL), true parallelism is limited in CPU-bound tasks, but multithreading can still be useful for I/O-bound tasks.
##In this example, we define a function print_numbers that prints numbers from 0 to 4. We create two threads (thread1 and thread2) that both execute the print_numbers function. When we start the threads, they run concurrently, and the output may interleave, showing numbers from both threads. Finally, we use join() to wait for both threads to complete before the program exits.

# Python program that demonstrates a simple multiprocessing:
import multiprocessing


def print_numbers():
    for i in range(5):
        print(i)

if __name__ == "__main__":
    # Create two processes
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_numbers)

    # Start the processes
    process1.start()
    process2.start()

    # Wait for the processes to complete
    process1.join()
    process2.join()

# >> 0, 1, 2, 3, 4
##Explanation: Multiprocessing is a technique in programming that allows multiple processes to run concurrently, each with its own memory space. In Python, the multiprocessing module provides a way to create and manage processes. Each process can execute a function independently, allowing for true parallelism, especially in CPU-bound tasks. This is because each process runs in its own Python interpreter and memory space, bypassing the Global Interpreter Lock (GIL) that limits multithreading in Python. In this example, we define a function print_numbers that prints numbers from 0 to 4. We create two processes (process1 and process2) that both execute the print_numbers function. When we start the processes, they run concurrently, and the output may interleave, showing numbers from both processes. Finally, we use join() to wait for both processes to complete before the program exits.   

#List of All the concepts to master Python one by one are as follow:
# 1. Variables and Data Types
# 2. Operators
# 3. Control Flow (if statements, loops)
# 4. Functions
# 5. Modules and Packages
# 6. Exception Handling
# 7. File Handling
# 8. Object-Oriented Programming (Classes and Objects)
# 9. Inheritance and Polymorphism
# 10. Decorators and Generators
# 11. Regular Expressions
# 12. Context Managers
# 13. Multithreading and Multiprocessing
#14. List Comprehensions and Lambda Functions
#15. Data Structures (Lists, Tuples, Sets, Dictionaries)
#16. String Manipulation
#17. Standard Library and Built-in Functions
#18. Virtual Environments and Package Management (pip, venv)
#19. Testing and Debugging
#20. Web Development (Flask, Django)
#21. Data Analysis and Visualization (Pandas, Matplotlib, Seaborn)
#22. Machine Learning and AI (Scikit-learn, TensorFlow, PyTorch)
#23. Networking and APIs (Requests, Flask, FastAPI)
#24. Asynchronous Programming (asyncio, aiohttp)
#25. Best Practices and Code Style (PEP 8)
#26. Version Control (Git, GitHub)
#27. Deployment and DevOps (Docker, CI/CD)
#28. Security and Authentication (JWT, OAuth)
#29. Performance Optimization and Profiling
#30. Advanced Topics (Metaclasses, Descriptors, Context Managers)
#31. Contributing to Open Source Projects
#32. Continuous Learning and Staying Updated with Python Ecosystem
#33. Community Engagement and Networking (Python Conferences, Meetups, Forums)
#34. Building Real-world Projects and Portfolio Development
#35. Exploring Python Libraries and Frameworks (NumPy, SciPy, TensorFlow, Django, Flask, etc.)
#36. Understanding Python's Global Interpreter Lock (GIL) and its Implications
#37. Exploring Python's Memory Management and Garbage Collection Mechanisms
#38. Understanding Python's Object Model and Data Model
#39. Exploring Python's Standard Library Modules and their Usage
#40. Understanding Python's Type Hinting and Annotations
#41. Exploring Python's Async/Await Syntax and Asynchronous Programming Paradigms
#42. Understanding Python's Packaging and Distribution Mechanisms (setuptools, wheel, PyPI)
#43. Exploring Python's Testing Frameworks and Best Practices (unittest, pytest, doctest)
#44. Understanding Python's Logging and Debugging Mechanisms (logging module, pdb)
#45. Exploring Python's Internationalization and Localization Support (gettext, locale)
#46. Understanding Python's Memory Profiling and Performance Optimization Techniques (memory_profiler, cProfile)
#47. Exploring Python's Networking and Socket Programming Capabilities (socket module, asyncio)
#48. Understanding Python's Security Best Practices and Vulnerability Mitigation Techniques (OWASP, secure coding practices)
#49. Exploring Python's Web Development Frameworks and Best Practices (Django, Flask, FastAPI)
#50. Understanding Python's Data Science and Machine Learning Ecosystem (NumPy, Pandas, Scikit-learn, TensorFlow, PyTorch)
#51. Exploring Python's GUI Development Frameworks and Best Practices (Tkinter, PyQt, Kivy)

#Total Time to master python: 6-12 months (depending on prior programming experience and dedication to learning)
#Start with the basics and gradually progress to more advanced topics, practicing regularly and building projects along the way.