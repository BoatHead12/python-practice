'''
Lists in Python (list)

1. What lists are
   - Lists are ordered, mutable collections that can contain duplicate values.
   - A list can contain values of different types, though related values are
     usually easier to work with.
2. Indexing, slicing, and iteration
3. Adding, changing, and removing items
   - append(), extend(), insert(), pop(), remove()
4. Sorting and reversing
   - sort() vs. sorted()
   - reverse() vs. reversed()
5. List comprehensions
6. Mutability, references, aliasing, and copying
7. Nested lists
8. Searching, filtering, and transforming lists
9. Practice problems
   - second-largest distinct element
   - remove duplicates
   - rotate a list
   - frequency counting
   - two-sum
'''

# ==========================
# 1. What lists are
# ==========================
numbers = [10, 20, 30, 20]
mixed_values = ["Python", 3, True]
empty_list = []

print("numbers =", numbers)
print("mixed_values =", mixed_values)
print("empty_list =", empty_list)
print("Type:", type(numbers))

# Lists preserve item order, allow duplicates, and can be changed in place.
numbers[0] = 99
print("After changing the first item:", numbers)

# ==========================
# 2. Indexing, slicing, and iteration
# ==========================
colors = ["red", "green", "blue", "yellow"]

# Indexes start at 0; negative indexes count backward from the end.
print("First color:", colors[0])
print("Last color:", colors[-1])
print("Second-last color:", colors[-2])

# Slice form: items[start:stop:step]. The stop index is excluded.
print("First two:", colors[0:2])
print("From index 2:", colors[2:])
print("Copy as a slice:", colors[:])
print("Every second item:", colors[::2])
print("Reversed slice:", colors[::-1])

# An out-of-range index raises IndexError. Slices safely stop at the boundary.
print("Slice beyond the end:", colors[2:100])

# Iterate over values when the index is not needed.
for color in colors:
	print("Color:", color)

# enumerate() provides both the index and value.
for index, color in enumerate(colors):
	print(f"colors[{index}] = {color}")

# ==========================
# 3. Adding, changing, and removing items
# ==========================
items = ["pen", "book"]

# append() adds one item at the end.
items.append("pencil")

# extend() adds each item from an iterable.
items.extend(["ruler", "eraser"])

# insert(index, value) adds an item before the given index.
items.insert(1, "notebook")
print("After adding items:", items)

# Assignment replaces an existing item.
items[0] = "marker"
print("After assignment:", items)

# pop() removes and returns an item; without an index it removes the last one.
last_item = items.pop()
first_item = items.pop(0)
print("Popped last item:", last_item)
print("Popped first item:", first_item)
print("Remaining items:", items)

# remove(value) removes the first matching value and returns None.
# It raises ValueError if the value is not present.
items.remove("book")
print("After remove():", items)

# Use membership to check before removing if absence is expected.
if "folder" in items:
	items.remove("folder")

# ==========================
# 4. Sorting and reversing
# ==========================
scores = [72, 95, 68, 95, 81]

# sorted() returns a new sorted list and leaves the original unchanged.
ascending_scores = sorted(scores)
descending_scores = sorted(scores, reverse=True)
print("Original scores:", scores)
print("sorted(scores):", ascending_scores)
print("Descending:", descending_scores)

# sort() sorts the list in place and returns None.
scores.sort()
print("After scores.sort():", scores)
scores.sort(reverse=True)
print("After descending sort():", scores)

# reverse() reverses a list in place and returns None; it does not sort.
letters = ["c", "a", "b"]
letters.reverse()
print("After reverse():", letters)

# reversed() returns an iterator and leaves the original list unchanged.
reversed_letters = list(reversed(letters))
print("list(reversed(letters)):", reversed_letters)
print("Original letters:", letters)

# Use key= to choose the value used for sorting.
words = ["pear", "fig", "watermelon", "plum"]
words_by_length = sorted(words, key=len)
print("Words sorted by length:", words_by_length)

# ==========================
# 5. List comprehensions
# ==========================
source_numbers = [1, 2, 3, 4, 5, 6]

# [expression for item in iterable]
squares = [number ** 2 for number in source_numbers]

# Add a condition to include selected items.
even_numbers = [number for number in source_numbers if number % 2 == 0]
even_squares = [number ** 2 for number in source_numbers if number % 2 == 0]

# Conditional expressions choose the output value for each item.
labels = ["even" if number % 2 == 0 else "odd" for number in source_numbers]

print("Squares:", squares)
print("Even numbers:", even_numbers)
print("Squares of even numbers:", even_squares)
print("Parity labels:", labels)

# A comprehension creates a new list; it does not modify the source list.

# ==========================
# 6. Mutability, references, aliasing, and copying
# ==========================
original = [1, 2, 3]
alias = original
alias.append(4)

# Both names refer to the same list, so a change through either name is visible.
print("original after alias.append(4):", original)
print("alias is original:", alias is original)

# A shallow copy makes a new outer list.
shallow_copy = original.copy()
another_copy = original[:]
shallow_copy.append(5)
print("Original after changing shallow copy:", original)
print("Shallow copy:", shallow_copy)
print("Slice copy:", another_copy)
print("shallow_copy is original:", shallow_copy is original)

# A shallow copy does not copy nested mutable items.
nested_original = [[1, 2], [3, 4]]
nested_copy = nested_original.copy()
nested_copy[0].append(99)
print("Nested original after inner-list change:", nested_original)
print("Nested shallow copy:", nested_copy)

# For fully independent copies of nested data, use copy.deepcopy().
import copy

deep_copy = copy.deepcopy(nested_original)
deep_copy[0].append(100)
print("Nested original after deep-copy change:", nested_original)
print("Deep copy:", deep_copy)

# Repetition duplicates references to an inner list, not the inner list itself.
shared_rows = [[0] * 3] * 2
shared_rows[0][0] = 1
print("Rows created by repetition share an inner list:", shared_rows)

# A comprehension creates independent inner lists.
independent_rows = [[0] * 3 for _ in range(2)]
independent_rows[0][0] = 1
print("Rows created by comprehension:", independent_rows)

# Avoid adding/removing items from a list while iterating over that same list;
# items can be skipped. Build a new list or iterate over a copy instead.

# ==========================
# 7. Searching, filtering, and transforming
# ==========================
values = [4, 7, 2, 7, 9, 2]

# in checks membership; index() finds the first position and raises
# ValueError when there is no match.
print("7 in values:", 7 in values)
print("First index of 7:", values.index(7))
print("Number of 2s:", values.count(2))

# Filter items into a new list with a comprehension.
large_values = [value for value in values if value >= 7]
print("Values at least 7:", large_values)

# Transform each item into a new list with a comprehension.
doubled_values = [value * 2 for value in values]
print("Doubled values:", doubled_values)

# ==========================
# 8. Practice problems
# ==========================

def second_largest(numbers):
	"""Return the second-largest distinct number, or None if it does not exist."""
	distinct_numbers = set(numbers)
	if len(distinct_numbers) < 2:
		return None
	return sorted(distinct_numbers)[-2]


def remove_duplicates(items):
	"""Return unique items in first-occurrence order (items must be hashable)."""
	return list(dict.fromkeys(items))


def rotate_right(items, steps):
	"""Return a new list rotated right by steps; empty lists stay empty."""
	if not items:
		return []
	steps %= len(items)
	if steps == 0:
		return items.copy()
	return items[-steps:] + items[:-steps]


def frequency_count(items):
	"""Return a dictionary mapping each hashable item to its number of occurrences."""
	frequencies = {}
	for item in items:
		frequencies[item] = frequencies.get(item, 0) + 1
	return frequencies


def two_sum(numbers, target):
	"""Return indices of two distinct values adding to target, or None."""
	seen_indices = {}
	for index, number in enumerate(numbers):
		complement = target - number
		if complement in seen_indices:
			return seen_indices[complement], index
		seen_indices[number] = index
	return None


print("Second-largest:", second_largest([10, 5, 8, 10, 3]))
print("Remove duplicates:", remove_duplicates([3, 1, 3, 2, 1]))
print("Rotate right by 2:", rotate_right([1, 2, 3, 4, 5], 2))
print("Frequency count:", frequency_count(["red", "blue", "red"]))
print("Two-sum indices:", two_sum([2, 7, 11, 15], 9))

# Practice notes:
# - second_largest() looks for the second-largest distinct value.
# - remove_duplicates() preserves first-occurrence order; its items must be
#   hashable (for example, numbers and strings, but not lists).
# - rotate_right() handles steps larger than the list length using modulo.
# - frequency_count() uses dict.get() to start an item's count at zero.
# - two_sum() returns the first matching pair of indices, or None if absent.

# ==========================
# 9. More everyday list operations
# ==========================

# list() converts an iterable to a list. A string becomes a list of characters.
converted_range = list(range(1, 5))
characters = list("cat")
print("List from range:", converted_range)
print("List from string:", characters)

# + concatenates lists and * repeats their contents into a new list.
combined_numbers = [1, 2] + [3, 4]
repeated_numbers = [0, 1] * 3
print("Concatenated lists:", combined_numbers)
print("Repeated list:", repeated_numbers)

# Unpacking assigns list elements to variables. The number of targets must
# match the number of values unless a starred target collects the remainder.
first, second, third = [10, 20, 30]
head, *middle, tail = [1, 2, 3, 4, 5]
print("Unpacked values:", first, second, third)
print("Head, middle, tail:", head, middle, tail)

# del removes an item or slice by index; clear() removes all items in place.
editable = ["a", "b", "c", "d"]
del editable[1]
del editable[1:3]
print("After del:", editable)
editable.clear()
print("After clear():", editable)

# Useful built-ins work with numeric lists: len(), min(), max(), and sum().
measurements = [12, 8, 15, 10]
print("Count:", len(measurements))
print("Minimum:", min(measurements))
print("Maximum:", max(measurements))
print("Total:", sum(measurements))

# all() and any() test conditions across an iterable.
all_positive = all(number > 0 for number in measurements)
has_large_value = any(number > 14 for number in measurements)
print("All measurements positive:", all_positive)
print("Any measurement above 14:", has_large_value)

# zip() pairs values by position. By default, it stops at the shortest iterable.
names = ["Asha", "Ravi", "Mei"]
ages = [21, 24]
name_age_pairs = list(zip(names, ages))
print("Paired names and ages:", name_age_pairs)

# In-place methods such as append(), extend(), insert(), sort(), reverse(),
# and clear() modify the existing list and return None. Do not assign their
# return value when you want to keep the list.
in_place_example = [3, 1, 2]
sort_result = in_place_example.sort()
print("Sorted in place:", in_place_example)
print("Return value of sort():", sort_result)