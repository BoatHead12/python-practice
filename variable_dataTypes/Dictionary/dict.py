'''
Dictionaries in Python (dict)

1. What dictionaries are
   - A dictionary stores key-value pairs and is written with braces.
   - Keys are unique; assigning an existing key updates its value.
   - Dictionaries preserve insertion order in modern Python.
2. Creating dictionaries and accessing entries
3. get(), keys(), values(), and items()
4. Adding, updating, and deleting entries
5. Key uniqueness and hashability
6. Dictionary comprehensions
7. Nested dictionaries
8. Searching, iterating, and transforming dictionaries
9. Frequency maps and grouping data
10. Practice problems
    - character frequencies
    - repeated elements
    - group words by anagram
    - build lookup tables
'''

# ==========================
# 1. What dictionaries are
# ==========================
student = {
	"name": "Asha",
	"age": 21,
	"course": "Python",
}

empty_dictionary = {}
also_empty = dict()

print("student =", student)
print("Type:", type(student))
print("empty_dictionary =", empty_dictionary)
print("also_empty =", also_empty)

# A dictionary maps each unique key to one value. Values may be duplicated
# and may have any type, including another dictionary or a list.
student["favorite_language"] = "Python"
student["level"] = "beginner"
print("After adding entries:", student)

# dict() can build a dictionary from keyword arguments or key-value pairs.
contact = dict(name="Mei", city="Toronto")
coordinates = dict([("x", 10), ("y", 20)])
print("Created with keyword arguments:", contact)
print("Created from pairs:", coordinates)

# ==========================
# 2. Accessing entries
# ==========================
profile = {"name": "Ravi", "score": 88}

# Square brackets retrieve a value. A missing key raises KeyError.
print("Name:", profile["name"])

# get() returns None for a missing key by default, instead of raising KeyError.
missing_value = profile.get("email")
score = profile.get("score")
print("Missing email:", missing_value)
print("Score:", score)

# Provide a default for keys that may be absent.
email = profile.get("email", "not provided")
print("Email:", email)

# get() reads a value; it does not add a missing key to the dictionary.
print("Dictionary after get():", profile)

# ==========================
# 3. keys(), values(), and items()
# ==========================
inventory = {"apples": 5, "oranges": 3, "pears": 7}

keys_view = inventory.keys()
values_view = inventory.values()
items_view = inventory.items()

print("Keys:", keys_view)
print("Values:", values_view)
print("Key-value pairs:", items_view)

# These methods return views, not separate lists. A view reflects later
# additions and removals from its dictionary.
inventory["bananas"] = 4
print("Keys view after adding bananas:", keys_view)

# Convert a view to a list if a separate snapshot is needed.
key_snapshot = list(inventory.keys())
print("Key snapshot:", key_snapshot)

# Unpacking items() gives a key and its corresponding value.
for fruit, quantity in inventory.items():
	print(f"{fruit}: {quantity}")

# ==========================
# 4. Adding, updating, and deleting entries
# ==========================
settings = {"theme": "light", "font_size": 14}

# Assigning a new key adds an entry; assigning an existing key replaces it.
settings["language"] = "en"
settings["theme"] = "dark"
print("After assignment:", settings)

# update() adds entries or replaces matching keys.
settings.update({"font_size": 16, "notifications": True})
settings.update(language="en-GB")
print("After update():", settings)

# The | operator creates a merged dictionary (Python 3.9+).
# For duplicate keys, the value from the right-hand dictionary wins.
defaults = {"theme": "light", "font_size": 12}
user_settings = {"theme": "dark"}
merged_settings = defaults | user_settings
print("Merged settings:", merged_settings)
print("Defaults are unchanged:", defaults)

# |= updates the dictionary in place with entries from the right.
defaults |= user_settings
print("Defaults after |=:", defaults)

# pop(key) removes and returns the value. Missing keys raise KeyError unless
# a default is supplied.
removed_font_size = settings.pop("font_size")
optional_entry = settings.pop("unknown", "not found")
print("Popped font size:", removed_font_size)
print("Popped optional entry:", optional_entry)

# del removes a named entry and raises KeyError if that key is absent.
del settings["notifications"]
print("After del:", settings)

# popitem() removes and returns the last inserted pair (LIFO behavior).
last_pair = settings.popitem()
print("Popped last pair:", last_pair)
print("After popitem():", settings)

# clear() removes all entries from the existing dictionary.
temporary = {"active": True}
temporary.clear()
print("After clear():", temporary)

# setdefault() returns an existing value; otherwise it inserts and returns
# the supplied default value.
cache = {"language": "Python"}
existing_language = cache.setdefault("language", "Java")
new_version = cache.setdefault("version", 3)
print("Existing language:", existing_language)
print("Inserted version:", new_version)
print("Cache after setdefault():", cache)

# ==========================
# 5. Key uniqueness and hashability
# ==========================
# Keys must be hashable (and have stable equality/hash behavior). Common
# hashable keys include strings, integers, and tuples of hashable values.
key_examples = {
	"name": "Asha",
	7: "seven",
	(2, 3): "coordinate",
}
print("Dictionary with different key types:", key_examples)
print("Tuple key value:", key_examples[(2, 3)])

# Lists and dictionaries are mutable and unhashable, so they cannot be keys.
# Uncommenting these examples raises TypeError:
# invalid_list_key = {[1, 2]: "value"}
# invalid_dict_key = {{"a": 1}: "value"}

# A tuple can be a key only if all of its elements are hashable.
valid_tuple_key = {(1, "x"): "valid"}
print("Tuple key:", valid_tuple_key[(1, "x")])
# invalid_tuple_key = {(1, [2]): "invalid"}  # TypeError: list is unhashable

# Repeating a key in a dictionary literal keeps the last value.
duplicate_key = {"mode": "basic", "mode": "advanced"}
print("Repeated key keeps the last value:", duplicate_key)

# Keys that compare equal address the same dictionary entry. For example,
# True == 1, so True and 1 cannot be separate keys in the same dictionary.
equal_key_example = {True: "first", 1: "second"}
print("True and 1 share a key:", equal_key_example)

# ==========================
# 6. Dictionary comprehensions
# ==========================
source_numbers = [1, 2, 3, 4, 5]

# Basic form: {key_expression: value_expression for item in iterable}
number_squares = {number: number ** 2 for number in source_numbers}

# Add a condition to include only selected items.
even_squares = {
	number: number ** 2
	for number in source_numbers
	if number % 2 == 0
}

# Transform an existing mapping with items().
prices = {"apple": 1.25, "bread": 2.50, "milk": 3.00}
discounted_prices = {
	product: round(price * 0.9, 2)
	for product, price in prices.items()
}

print("Number squares:", number_squares)
print("Even squares:", even_squares)
print("Discounted prices:", discounted_prices)

# If multiple source items produce the same key, later values overwrite
# earlier ones. A dictionary comprehension does not preserve duplicate keys.

# ==========================
# 7. Nested dictionaries
# ==========================
classroom = {
	"student_101": {"name": "Asha", "grade": 92},
	"student_102": {"name": "Ravi", "grade": 85},
}

# Access nested values by chaining keys.
print("Student 101 name:", classroom["student_101"]["name"])
print("Student 102 grade:", classroom["student_102"]["grade"])

# Update a nested value.
classroom["student_102"]["grade"] = 89

# Add another field to an existing nested dictionary.
classroom["student_101"]["city"] = "Delhi"

# Add a new nested dictionary.
classroom["student_103"] = {"name": "Mei", "grade": 96}
print("Updated classroom:", classroom)

# Use get() at each level when a key might be absent.
student_999 = classroom.get("student_999", {})
unknown_name = student_999.get("name", "unknown student")
print("Missing nested student:", unknown_name)

# ==========================
# 8. Searching, iterating, and transforming
# ==========================
person = {"name": "Asha", "city": "Delhi", "active": True}

# in checks keys, not values. Use .values() to search values.
print('"name" in person:', "name" in person)
print('"Asha" in person:', "Asha" in person)
print('"Asha" in person.values():', "Asha" in person.values())

# Iterate over keys by default, or explicitly with keys().
for key in person:
	print("Key:", key)

# Iterate over key-value pairs with items().
for key, value in person.items():
	print(f"{key} -> {value}")

# Build a new dictionary from selected entries.
active_fields = {
	key: value
	for key, value in person.items()
	if key != "city"
}
print("Selected fields:", active_fields)

# Dictionary equality compares key-value contents, not insertion order.
first_mapping = {"a": 1, "b": 2}
second_mapping = {"b": 2, "a": 1}
print("Mappings equal:", first_mapping == second_mapping)

# ==========================
# 9. Frequency maps and grouping data
# ==========================

def character_frequencies(text):
	"""Return counts for each character, including spaces and punctuation."""
	frequencies = {}
	for character in text:
		frequencies[character] = frequencies.get(character, 0) + 1
	return frequencies


def repeated_elements(items):
	"""Return each repeated hashable item once, in its second-seen order."""
	counts = {}
	repeated = []
	for item in items:
		counts[item] = counts.get(item, 0) + 1
		if counts[item] == 2:
			repeated.append(item)
	return repeated


def group_words_by_anagram(words):
	"""Group words by letters, ignoring case but retaining original spelling."""
	groups = {}
	for word in words:
		key = tuple(sorted(word.casefold()))
		groups.setdefault(key, []).append(word)
	return list(groups.values())


def build_lookup(records, key_field, value_field):
	"""Build a lookup from record fields; later duplicate keys replace earlier."""
	lookup = {}
	for record in records:
		lookup[record[key_field]] = record[value_field]
	return lookup


sample_text = "banana"
sample_items = ["red", "blue", "red", "green", "blue", "red"]
sample_words = ["listen", "Silent", "enlist", "rat", "tar", "art", "dog"]
employees = [
	{"id": 101, "name": "Asha"},
	{"id": 102, "name": "Ravi"},
	{"id": 103, "name": "Mei"},
]

print("Character frequencies:", character_frequencies(sample_text))
print("Repeated elements:", repeated_elements(sample_items))
print("Anagram groups:", group_words_by_anagram(sample_words))
print("Employee lookup:", build_lookup(employees, "id", "name"))

# ==========================
# 10. Common patterns and cautions
# ==========================

# Count values with get() or setdefault().
word_counts = {}
for word in ["python", "lists", "python", "dicts"]:
	word_counts[word] = word_counts.get(word, 0) + 1
print("Word counts:", word_counts)

# defaultdict is useful when a missing key should start with an empty list.
from collections import defaultdict

students_by_grade = defaultdict(list)
grade_records = [("Asha", "A"), ("Ravi", "B"), ("Mei", "A")]
for name, grade in grade_records:
	students_by_grade[grade].append(name)
print("Students by grade:", dict(students_by_grade))

# Avoid changing a dictionary's size while iterating over it. Iterate over a
# list of keys or build a new dictionary instead.
scores = {"Asha": 90, "Ravi": 72, "Mei": 84}
passing_scores = {
	name: score
	for name, score in scores.items()
	if score >= 80
}
print("Passing scores:", passing_scores)

# Practical notes:
# - Keys must be hashable; dictionary values do not need to be hashable.
# - A missing key with [] raises KeyError; use get() or check membership.
# - Use `key in mapping` to check keys, and `value in mapping.values()` to
#   check values.
# - keys(), values(), and items() are dynamic views of the dictionary.
# - update() changes the dictionary in place; | creates a merged dictionary.
# - Nested lookups may raise KeyError at any missing level; use get() when
#   missing data is an expected case.

# ==========================
# 11. Additional dictionary patterns
# ==========================

# copy() creates a shallow copy: the outer dictionary is new, but nested
# mutable values are still shared.
original_profile = {"name": "Asha", "scores": [85, 92]}
profile_copy = original_profile.copy()
profile_copy["name"] = "Mei"
profile_copy["scores"].append(98)
print("Original profile:", original_profile)
print("Shallow profile copy:", profile_copy)

# Build nested dictionaries with a comprehension so each value is independent.
independent_defaults = {name: [] for name in ["Asha", "Ravi"]}
independent_defaults["Asha"].append("Python")
print("Independent nested defaults:", independent_defaults)

# Be careful with dict.fromkeys() and mutable values: every key refers to the
# same value object when one shared list is supplied.
shared_defaults = dict.fromkeys(["Asha", "Ravi"], [])
shared_defaults["Asha"].append("Python")
print("fromkeys() shared mutable value:", shared_defaults)

# Sorting a dictionary directly sorts its keys. Use sorted(items()) when
# key-value pairs need to be ordered, and construct a dict if a mapping is wanted.
unsorted_prices = {"pear": 2.0, "apple": 1.5, "plum": 2.5}
sorted_product_names = sorted(unsorted_prices)
sorted_price_pairs = sorted(unsorted_prices.items(), key=lambda pair: pair[1])
prices_by_cost = dict(sorted_price_pairs)
print("Sorted product names:", sorted_product_names)
print("Pairs sorted by price:", sorted_price_pairs)
print("Dictionary in price order:", prices_by_cost)

# keys() views support set operations when keys are hashable.
available_sizes = {"small": 3, "medium": 0, "large": 5}
requested_sizes = {"medium": 2, "large": 1, "extra-large": 4}
common_sizes = available_sizes.keys() & requested_sizes.keys()
all_sizes = available_sizes.keys() | requested_sizes.keys()
only_available_sizes = available_sizes.keys() - requested_sizes.keys()
print("Sizes in both dictionaries:", common_sizes)
print("All sizes:", all_sizes)
print("Only in available inventory:", only_available_sizes)

# Dictionary unpacking creates a new dictionary. Later entries override earlier
# entries when keys overlap.
base_config = {"host": "localhost", "port": 8000}
local_config = {"port": 9000, "debug": True}
combined_config = {**base_config, **local_config}
print("Combined config:", combined_config)

# **kwargs uses dictionary keys as keyword argument names; those keys must be
# strings that are valid parameter names for the called function.
def describe_person(name, city):
	"""Return a short description from keyword arguments."""
	return f"{name} lives in {city}."


person_details = {"name": "Ravi", "city": "Pune"}
print("Keyword unpacking:", describe_person(**person_details))

# get() with a default of None cannot distinguish a missing key from a key
# explicitly mapped to None. Use membership when that distinction matters.
optional_values = {"present_none": None}
missing_key_value = optional_values.get("missing")
present_none_value = optional_values.get("present_none")
print("Both get() results are None:", missing_key_value is present_none_value)
print("'missing' is present:", "missing" in optional_values)
print("'present_none' is present:", "present_none" in optional_values)

# End of dictionary notes