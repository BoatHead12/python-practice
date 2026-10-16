'''
1. Variables and Data Types
'''

#Variable Defination: it's 

# Variable Declaration
# In Python, you don't need to declare the type of a variable explicitly.
# You can simply assign a value to a variable, and Python will infer its type.
x = 5  # x is an integer
y = "Hello, World!"  # y is a string
z = [1, 2, 3]  # z is a list
w = (4, 5, 6)  # w is a tuple
v = {7, 8, 9}  # v is a set
u = {"name": "Alice", "age": 30}  # u is a dictionary

#Data Types

# Python has several built-in data types, including:
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Text Type: str
# Set Types: set, frozenset
# Mapping Type: dict
# Boolean Type: bool
# None Type: NoneType
# Binary Type: bytes, bytearray, memoryview


#Examples of Data Types
# Numeric Types >>Used to represent numbers.
dt_int = 25
dt_float = 3.14
dt_complex = 2 + 5j

print(type(dt_int))  # <class 'int'>
print(type(dt_float))  # <class 'float'>
print(type(dt_complex))  # <class 'complex'>


#Boolean Type >>Represents logical truth values.
is_valid = True  #Note: True and False must start with capital letters in Python.
is_empty = False

print(type(is_valid))  # <class 'bool'>
print(type(is_empty))  # <class 'bool'>  


#Text Type >>to store text and characters.
name = "Python"
message = 'Hello World'

print(type(name))  # <class 'str'>


#Sequence types >> to store ordered sequence of values

# list >>Ordered collection that allows duplicate values and changes.
numbers = [10, 20, 30, 20]
numbers[0] = 99
print(type(numbers))  #>> <class 'list'>

#Tuple: Ordered collection that allows duplicates but cannot be modified in place.
values = (10, 20, 30, 20)
print("\n")
print(type(values))  #>> <class 'tuple'>

#Range: Represents a sequence of integers, commonly used in loops.
dt_range = range(1, 6)
print(list(dt_range))  # [1, 2, 3, 4, 5]

print(type(dt_range)) #>> <class 'range'>


#Mapping type >> A mapping stores data as key-value pairs.

#Dict >> Mutable mapping of keys to values
student = {
    "name": "Raj",      #Dictionary keys must be hashable, and each key is unique
    "age": 20,
    "marks": 85
}

print(student["name"])  # Raj
print(type(student))    # <class 'dict'>


#Set types >>store unique elements

# set	>>Mutable collection of unique elements
# frozenset	>>Immutable set
dt_set = {10, 20, 10, 30}  # noqa: B033
print(dt_set)  # {10, 20, 30} (display order may vary)

dt_frozenset = frozenset([10, 20, 30])
print(type(dt_set)) #< >> class 'set'>
print(type(dt_frozenset)) #>> <class 'frozenset'>

#Sets do not support indexing like lists or tuples.
#empty set is created using set(), not {}, because {} creates an empty dictionary.


#Binary Type
#bytes	    >> Immutable sequence of bytes
#bytearray	>> Mutable sequence of bytes
#memoryview	>> Provides access to binary data without copying it just to create the view

dt_bytes = b"ABC"
dt_bytearray = bytearray([65, 66, 67])
dt_bytearray[0] = 90

dt_memoryview = memoryview(b"ABC")

print(dt_bytes)  # b'ABC'
print(dt_bytearray)  # bytearray(b'ZBC')
print(dt_memoryview) # <memory at 0x762e5b146b00>

print(type(dt_bytes)) # >><class 'bytes'>
print(type(dt_bytearray)) #>> <class 'bytearray'>
print(type(dt_memoryview))#>>  <class 'memoryview'>


#None type >>Represents the absence of a value.

dt_nonetype = None

print(dt_nonetype)       # None
print(type(dt_nonetype)) # <class 'NoneType'>
#None is commonly used to indicate that a function has no meaningful return value or that a value is currently unavailable.


#**********************
'''
Mutable vs immutable data types

A. Mutable:
            1. list
            2. dict
            3. set
            4. bytearray

B. Immutable:
            1. int
            2. float
            3. complex
            4. bool
            5. str
            6. tuple*       >>*A tuple cannot be modified in place, but it can contain mutable objects, such as lists. Those contained objects may still change.
            7. range
            8. bytes
            9. frozenset
            10. NoneType
'''
# Mutable
dt_mutable = [10, 20, 30]
dt_mutable[0] = 100

# Immutable
dt_immutable = "Python"
# dt_immutable[0] = "J"  # TypeError


'''
Quick revision:
int         10
float       10.5
complex     2 + 3j
bool        True
str         "Hello"
list        [1, 2, 3]
tuple       (1, 2, 3)
range       range(5)
dict        {"a": 1}
set         {1, 2, 3}
frozenset   frozenset({1, 2})
bytes       b"ABC"
bytearray   bytearray([65, 66])
memoryview  memoryview(b'ABC')
NoneType    None
'''
