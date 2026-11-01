'''
Tuples in Python (tuple)

1. What tuples are
   - Tuples are ordered collections that cannot be changed after creation.
   - They can contain duplicate values and values of different types.
   - Parentheses are commonly used, but commas are what make a tuple.
2. Creating tuples and tuple packing
3. Single-element and empty tuples
4. Indexing, slicing, and iteration
5. Unpacking and swapping values
6. Immutability and mutable values inside tuples
7. Tuple comparison
8. Hashability and tuples as dictionary keys
9. Returning multiple values from functions
10. When tuples are useful
11. Tuple operations and methods
12. Built-in functions, sorting, and tuple construction
13. Practice problems
    - represent a coordinate as (x, y)
    - swap two values using unpacking
    - return several related values from a function
'''

# ==========================
# 1. What tuples are
# ==========================
student = ("Mina", 20, "Python")
repeated_values = (4, 4, 7)
mixed_values = ("score", 95, True)
empty_tuple = ()

print("student =", student)
print("repeated_values =", repeated_values)
print("mixed_values =", mixed_values)
print("empty_tuple =", empty_tuple)
print("Type:", type(student))

# Tuples preserve order and allow duplicates. The tuple itself cannot have
# items added, removed, or replaced after it has been created.

# ==========================
# 2. Creating tuples and tuple packing
# ==========================
# Commas pack values into a tuple. Parentheses are optional in many contexts.
point = 3, 8
also_a_point = (3, 8)
from_iterable = tuple(["red", "green", "blue"])

print("Packed tuple:", point)
print("Parenthesized tuple:", also_a_point)
print("Built with tuple():", from_iterable)

# tuple() with no arguments creates an empty tuple. Calling tuple() on an
# existing tuple returns an equivalent tuple; it does not add nesting.
empty_from_constructor = tuple()
print("tuple() =", empty_from_constructor)
print("tuple(point) =", tuple(point))

# ==========================
# 3. Single-element and empty tuples
# ==========================
single_item_tuple = (5,)
also_single_item_tuple = 5,
just_an_integer = (5)

print("Single-item tuple:", single_item_tuple, type(single_item_tuple))
print("Single-item tuple without parentheses:", also_single_item_tuple)
print("Parentheses around an integer:", just_an_integer, type(just_an_integer))

# The comma makes a one-element tuple. (5) is simply the integer 5.
one_item_string_tuple = ("Python",)
print("One-item string tuple:", one_item_string_tuple)

# ==========================
# 4. Indexing, slicing, and iteration
# ==========================
colors = ("red", "green", "blue", "yellow")

# Indexes start at 0; negative indexes count backward from the end.
print("First color:", colors[0])
print("Last color:", colors[-1])
print("Second-last color:", colors[-2])

# Slice form: items[start:stop:step]. The stop index is excluded.
# Slicing a tuple produces another tuple.
print("First two:", colors[0:2])
print("From index 2:", colors[2:])
print("Copy as a slice:", colors[:])
print("Every second color:", colors[::2])
print("Reversed slice:", colors[::-1])

# An invalid index raises IndexError. Slices safely stop at the boundary.
print("Slice beyond the end:", colors[2:100])

# Iterate directly over tuple values.
for color in colors:
	print("Color:", color)

# enumerate() provides each index and its corresponding value.
for index, color in enumerate(colors):
	print(f"colors[{index}] = {color}")

# ==========================
# 5. Unpacking and swapping values
# ==========================
# Unpacking assigns tuple items to names in order. The number of targets
# must match the number of items unless starred unpacking is used.
coordinates = (12, 7)
x, y = coordinates
print("x =", x)
print("y =", y)

first, *middle, last = (10, 20, 30, 40, 50)
print("first =", first)
print("middle =", middle)
print("last =", last)

# Assignment evaluates the right-hand side before assigning the names,
# so Python can swap values without a temporary variable.
left = "A"
right = "B"
left, right = right, left
print("After swapping: left =", left, ", right =", right)

# Unpacking is useful for looping over pairs or other fixed-size records.
for name, score in (("Asha", 88), ("Noah", 94)):
	print(f"{name} scored {score}")

# ==========================
# 6. Immutability and mutable values inside tuples
# ==========================
fixed_point = (2, 5)
print("Original point:", fixed_point)

# Assigning to an item, deleting an item, or appending to a tuple is not
# allowed. For example, fixed_point[0] = 9 raises TypeError.
# To make a changed tuple, build a new tuple instead.
updated_point = (9,) + fixed_point[1:]
print("New tuple with a changed first coordinate:", updated_point)
print("Original tuple remains:", fixed_point)

# Immutability applies to the tuple's references, not to the state of
# objects stored inside it. A nested mutable object can still be changed.
container = ("tasks", ["read", "practice"])
container[1].append("review")
print("Tuple containing a changed list:", container)

# The list reference in container cannot be replaced with another value.
# A tuple is therefore not necessarily deeply immutable.

# ==========================
# 7. Tuple comparison
# ==========================
# Equality checks whether corresponding items are equal.
print("(1, 2) == (1, 2):", (1, 2) == (1, 2))
print("(1, 2) == (2, 1):", (1, 2) == (2, 1))

# Ordering comparisons are lexicographic: Python compares corresponding
# items from left to right and decides at the first difference.
print("(1, 9) < (2, 0):", (1, 9) < (2, 0))
print("(3, 4) < (3, 8):", (3, 4) < (3, 8))
print("(1, 2) < (1, 2, 0):", (1, 2) < (1, 2, 0))

# If all compared items match, the shorter tuple sorts before the longer one.
# Ordering comparisons require the items reached during comparison to be
# comparable with each other; for example, 1 < "one" raises TypeError.

# ==========================
# 8. Hashability and tuples as dictionary keys
# ==========================
# A tuple can be used as a dictionary key when all of its items are hashable.
# Integers and strings are hashable, so coordinate pairs work well as keys.
city_by_coordinate = {
	(40, 74): "Example City A",
	(34, 118): "Example City B",
}

lookup_coordinate = (40, 74)
print("City at", lookup_coordinate, ":", city_by_coordinate[lookup_coordinate])
print("All coordinate keys:", list(city_by_coordinate.keys()))

# A tuple that contains a list is not hashable, because lists are mutable.
# Using such a tuple as a dictionary key raises TypeError.
unhashable_tuple = ("location", [40, 74])
print("Tuple containing a list can be created:", unhashable_tuple)

# Use a tuple of immutable values, such as (40, 74), as a key instead.

# ==========================
# 9. Returning multiple values from functions
# ==========================
def get_min_max(numbers):
	"""Return the smallest and largest values as a tuple."""
	return min(numbers), max(numbers)


minimum, maximum = get_min_max((8, 3, 12, 5))
print("Minimum:", minimum)
print("Maximum:", maximum)

# A function can return several comma-separated values. Python packs them
# into one tuple, which can be stored whole or unpacked by the caller.
result = get_min_max((8, 3, 12, 5))
print("Returned tuple:", result)


def describe_point(x, y):
	"""Return a coordinate and its distance from the origin."""
	distance_squared = x ** 2 + y ** 2
	return (x, y), distance_squared


coordinate, distance_squared = describe_point(3, 4)
print("Coordinate:", coordinate)
print("Distance squared:", distance_squared)

# ==========================
# 10. When tuples are useful
# ==========================
# Use a tuple for a fixed-size record whose items belong together:
# coordinates = (x, y)
# rgb_color = (red, green, blue)
# date_parts = (year, month, day)
#
# Tuples are often a good choice when:
# - the collection should not be structurally changed;
# - a function should return a small group of related values;
# - an immutable, hashable group of values is needed as a dictionary key.
#
# Choose a list when you need to add, remove, or replace items frequently.

# ==========================
# 11. Tuple operations and methods
# ==========================
measurements = (12, 18, 12, 25)

# The in operator checks whether an item is present.
print("18 in measurements:", 18 in measurements)
print("99 not in measurements:", 99 not in measurements)

# Tuples provide count(value) and index(value). index() returns the first
# matching position and raises ValueError when the value is absent.
print("Count of 12:", measurements.count(12))
print("First position of 12:", measurements.index(12))

# Tuples support concatenation (+) and repetition (*). These operations
# create new tuples; they do not modify either original tuple.
base_tuple = ("a", "b")
joined_tuple = base_tuple + ("c",)
repeated_tuple = base_tuple * 3
print("Concatenated tuple:", joined_tuple)
print("Repeated tuple:", repeated_tuple)
print("Original tuple:", base_tuple)

# The repeated items are references to the same objects. Repetition does
# not copy nested mutable objects.
shared_list_tuple = ([],) * 2
shared_list_tuple[0].append("changed")
print("Repeated tuple shares its nested list:", shared_list_tuple)

# ==========================
# 12. Built-in functions, sorting, and tuple construction
# ==========================
scores = (72, 95, 68, 81)

# Common sequence and numeric built-ins work with tuples.
print("Number of scores:", len(scores))
print("Smallest score:", min(scores))
print("Largest score:", max(scores))
print("Total score:", sum(scores))

# sorted() accepts an iterable and returns a new list, not a tuple.
# Use tuple(sorted(...)) when a sorted tuple is specifically required.
ascending_scores = sorted(scores)
descending_scores = tuple(sorted(scores, reverse=True))
print("sorted(scores):", ascending_scores, type(ascending_scores))
print("Sorted tuple, descending:", descending_scores)
print("Original scores:", scores)

# tuple() takes one iterable argument, not several separate items.
# A generator expression in parentheses is a generator, not a tuple.
number_generator = (number ** 2 for number in range(1, 5))
squares_tuple = tuple(number_generator)
print("Tuple built from a generator:", squares_tuple)

# Tuple unpacking can also happen in function parameters with *args:
# the function receives the extra positional arguments in a tuple.
def show_arguments(*arguments):
	"""Print the tuple that collects positional arguments."""
	print("Collected arguments:", arguments)
	print("Type of arguments:", type(arguments))


show_arguments("red", "green", "blue")

# ==========================
# 13. Practice problems
# ==========================
# 1. Create a tuple for a 2D coordinate, then unpack it into x and y.
# 2. Swap two variables using a single unpacking assignment.
# 3. Write a function that accepts a tuple of numbers and returns the
#    smallest value, largest value, and number of values as a tuple.
# 4. Store names by coordinate using a dictionary whose keys are tuples.
# 5. Count how many times a value appears and find its first index.
# 6. Sort a tuple of numbers and compare the types returned by sorted()
#    and tuple(sorted(...)).