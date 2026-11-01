'''
Sets in Python (set and frozenset)

1. What sets are
   - Sets contain unique, hashable elements.
   - A set is mutable; a frozenset is immutable.
   - Sets are unordered collections and do not support indexing or slicing.
2. Creating sets
3. Hashability and uniqueness
4. Membership testing and iteration
5. Adding, updating, and removing elements
6. Set operations
   - union (|), intersection (&), difference (-)
   - symmetric difference (^)
7. Subsets, supersets, and disjoint sets
8. Mutable set vs. immutable frozenset
9. In-place operations and method/operator differences
10. Set comprehensions and removing duplicates
11. Practical set problems
12. When to use sets
13. Practice problems
'''

# ==========================
# 1. What sets are
# ==========================
colors = {"red", "green", "blue"}
empty_set = set()
empty_dictionary = {}

print("colors =", colors)
print("Type:", type(colors))
print("empty_set =", empty_set)
print("Type of empty_set:", type(empty_set))
print("An empty {} creates a dictionary:", type(empty_dictionary))

# A set stores each distinct element at most once. Sets are mutable, but
# they are unordered: do not rely on a particular iteration or display order.
# Sets do not support positional indexing or slicing.

# ==========================
# 2. Creating sets
# ==========================
# Braces create a non-empty set. Duplicate values are removed.
number_set = {1, 2, 2, 3, 3, 3}
print("Duplicates removed when creating a set:", number_set)

# set(iterable) builds a set from an iterable such as a list, tuple, or string.
from_list = set([1, 2, 2, 3])
from_tuple = set((3, 4, 4, 5))
letters = set("hello")
print("From a list:", from_list)
print("From a tuple:", from_tuple)
print("Unique letters in 'hello':", letters)

# An empty set must be created with set(), because {} means an empty dict.

# ==========================
# 3. Hashability and uniqueness
# ==========================
# Set elements must be hashable. Common hashable elements include integers,
# strings, and tuples whose own elements are all hashable.
valid_elements = {10, "Python", (2, 5)}
print("Set with hashable elements:", valid_elements)

# Lists, dictionaries, and sets are mutable and unhashable, so they cannot
# be elements of a set. For example, { [1, 2] } raises TypeError.
# Convert a list to a tuple when an immutable pair is appropriate:
coordinate_set = {(2, 5), (8, 1)}
print("Coordinates as set elements:", coordinate_set)

# Equal values are treated as the same set element. For example, True and 1
# compare equal and have compatible hashes, so a set stores only one of them.
equal_values = {True, 1, 2}
print("True and 1 count as one set element:", equal_values)

# ==========================
# 4. Membership testing and iteration
# ==========================
allowed_extensions = {".py", ".txt", ".md"}

# Membership testing with in is a common and efficient use of sets.
print("'.py' is allowed:", ".py" in allowed_extensions)
print("'.csv' is allowed:", ".csv" in allowed_extensions)
print("'.csv' is not allowed:", ".csv" not in allowed_extensions)

# Iterate over elements without assuming a specific order.
for extension in allowed_extensions:
	print("Allowed extension:", extension)

# A set cannot be indexed: allowed_extensions[0] raises TypeError.
# If an ordered sequence is needed, sort or convert the values explicitly.
ordered_extensions = sorted(allowed_extensions)
print("Sorted extensions:", ordered_extensions)

# ==========================
# 5. Adding, updating, and removing elements
# ==========================
tools = {"editor", "terminal"}

# add(element) inserts one element. Adding an existing element has no effect.
tools.add("debugger")
tools.add("terminal")
print("After add():", tools)

# update(iterable, ...) adds elements from one or more iterables.
tools.update(["formatter", "linter"])
tools.update(("tester", "formatter"))
print("After update():", tools)

# remove(element) deletes an element and raises KeyError if it is absent.
tools.remove("linter")
print("After remove():", tools)

# discard(element) deletes an element if present and does nothing otherwise.
tools.discard("debugger")
tools.discard("not-installed")
print("After discard():", tools)

# pop() removes and returns an arbitrary element; it is not a way to get a
# predictable first or last item. Calling pop() on an empty set raises KeyError.
removed_tool = tools.pop()
print("Arbitrary element returned by pop():", removed_tool)
print("After pop():", tools)

# clear() removes all elements. copy() makes a shallow copy.
tools_copy = tools.copy()
tools_copy.add("documentation")
print("Original tools:", tools)
print("Copy after adding an item:", tools_copy)
tools_copy.clear()
print("Cleared copy:", tools_copy)

# Do not add or remove elements from a set while iterating over that same set.
# Iterate over a copy or create a new set instead.
positive_numbers = {1, 2, 3, 4, 5}
even_numbers = {number for number in positive_numbers if number % 2 == 0}
print("Even numbers selected into a new set:", even_numbers)

# ==========================
# 6. Set operations
# ==========================
python_students = {"Asha", "Mina", "Noah", "Ravi"}
art_students = {"Mina", "Ravi", "Sofia"}

# Union: all elements found in either set (duplicates appear only once).
all_students = python_students | art_students
print("Students in either group (union):", all_students)
print("Union with union():", python_students.union(art_students))

# Intersection: elements shared by both sets.
students_in_both = python_students & art_students
print("Students in both groups (intersection):", students_in_both)
print("Intersection with intersection():",
	  python_students.intersection(art_students))

# Difference: elements in the left set that are not in the right set.
python_only = python_students - art_students
art_only = art_students - python_students
print("Python students only:", python_only)
print("Art students only:", art_only)

# Difference is directional: A - B is not generally the same as B - A.
print("A - B:", {1, 2, 3} - {2, 3, 4})
print("B - A:", {2, 3, 4} - {1, 2, 3})

# Symmetric difference: elements in either set, but not in both.
students_in_exactly_one = python_students ^ art_students
print("Students in exactly one group:", students_in_exactly_one)
print("Symmetric difference with symmetric_difference():",
	  python_students.symmetric_difference(art_students))

# The operators |, &, -, and ^ produce new sets and leave their operands
# unchanged. The named methods also accept other iterables as arguments.
print("Original Python group remains:", python_students)
print("Intersection with a list:",
	  python_students.intersection(["Mina", "Ravi", "Tariq"]))

# ==========================
# 7. Subsets, supersets, and disjoint sets
# ==========================
core_topics = {"variables", "loops"}
all_topics = {"variables", "loops", "functions"}
other_topics = {"classes", "modules"}

# <= checks subset-or-equal; < checks a proper subset (subset, but unequal).
print("core_topics <= all_topics:", core_topics <= all_topics)
print("core_topics < all_topics:", core_topics < all_topics)
print("all_topics < all_topics:", all_topics < all_topics)
print("Using issubset():", core_topics.issubset(all_topics))

# >= checks superset-or-equal; > checks a proper superset.
print("all_topics >= core_topics:", all_topics >= core_topics)
print("all_topics > core_topics:", all_topics > core_topics)
print("Using issuperset():", all_topics.issuperset(core_topics))

# Disjoint sets have no shared elements.
print("core_topics and other_topics are disjoint:",
	  core_topics.isdisjoint(other_topics))
print("core_topics and all_topics are disjoint:",
	  core_topics.isdisjoint(all_topics))

# Empty set is a subset of every set. A set is both a subset and superset
# of itself, but is not a proper subset or proper superset of itself.
print("Empty set is a subset of core_topics:", set() <= core_topics)

# ==========================
# 8. Mutable set vs. immutable frozenset
# ==========================
mutable_tags = {"python", "beginner"}
immutable_tags = frozenset(["python", "beginner", "collections"])

print("Mutable set:", mutable_tags, type(mutable_tags))
print("Frozenset:", immutable_tags, type(immutable_tags))

# A set supports changes; a frozenset does not have add(), remove(), or
# other in-place element-changing methods.
mutable_tags.add("practice")
print("Set after adding a tag:", mutable_tags)
# immutable_tags.add("practice") would raise AttributeError.

# Set operations on frozensets produce a frozenset when the operation is
# performed between frozensets.
frozenset_a = frozenset({1, 2, 3})
frozenset_b = frozenset({3, 4})
frozenset_union = frozenset_a | frozenset_b
print("Frozenset union:", frozenset_union, type(frozenset_union))
print("Frozenset intersection:", frozenset_a & frozenset_b)

# Because a frozenset is immutable and hashable, it can be a set element or
# dictionary key. A mutable set is unhashable and cannot be used that way.
set_of_groups = {frozenset({"read", "write"}), frozenset({"read"})}
permissions_by_group = {frozenset({"read", "write"}): "editor"}
print("Set containing frozensets:", set_of_groups)
print("Lookup by frozenset key:",
	  permissions_by_group[frozenset({"read", "write"})])

# A frozenset can only be created from hashable elements, just like a set.
# It is shallowly immutable: if an element itself were mutable, it could not
# be included because mutable objects such as lists are unhashable.

# ==========================
# 9. In-place operations and method/operator differences
# ==========================
languages = {"Python", "Java"}
additional_languages = {"Rust", "Java"}

# Augmented operators update a mutable set in place.
languages |= additional_languages
print("After |= (in-place union):", languages)

languages &= {"Python", "Rust"}
print("After &= (in-place intersection):", languages)

languages -= {"Rust"}
print("After -= (in-place difference):", languages)

languages ^= {"Go", "Python"}
print("After ^= (in-place symmetric difference):", languages)

# The corresponding named methods also update the set in place and return
# None; do not assign their result back to the set.
method_set = {1, 2, 3}
method_result = method_set.intersection_update({2, 3, 4})
print("After intersection_update():", method_set)
print("Return value of intersection_update():", method_result)

# Other in-place methods are update(), difference_update(), and
# symmetric_difference_update(). clear() also mutates the set and returns None.

# Set operation methods accept arbitrary iterables as arguments, such as a
# list. The corresponding operators require set/frozenset operands:
method_intersection = {1, 2, 3}.intersection([2, 3, 4])
print("Method with a list argument:", method_intersection)
# {1, 2, 3} & [2, 3, 4] raises TypeError; convert the list to a set first.

# Comparisons have their own rules: issubset(), issuperset(), and
# isdisjoint() accept iterables, while <, <=, >, and >= compare sets.
print("issubset() with a list:", {1, 2}.issubset([1, 2, 3]))

# ==========================
# 10. Set comprehensions and removing duplicates
# ==========================
source_numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(source_numbers)
print("Unique numbers:", unique_numbers)

# Set comprehensions use braces and produce a set of unique results.
squares_of_even_numbers = {
	number ** 2 for number in source_numbers if number % 2 == 0
}
print("Squares of even numbers:", squares_of_even_numbers)

# Sets remove duplicates but do not preserve the original order. If stable
# first-occurrence order matters, use dict.fromkeys() instead:
words = ["pear", "apple", "pear", "plum", "apple"]
unique_words_in_order = list(dict.fromkeys(words))
print("Unique words in first-seen order:", unique_words_in_order)

# ==========================
# 11. Practical set problems
# ==========================
# Problem A: find common items between two lists.
reading_list = ["poetry", "history", "science", "art"]
available_books = ["science", "art", "music"]
common_books = set(reading_list) & set(available_books)
print("Books in both lists:", common_books)

# Problem B: compare two groups to find shared and exclusive members.
team_red = {"Ari", "Bo", "Cam"}
team_blue = {"Bo", "Dee"}
shared_members = team_red & team_blue
red_only = team_red - team_blue
blue_only = team_blue - team_red
either_team_but_not_both = team_red ^ team_blue
print("Shared members:", shared_members)
print("Red only:", red_only)
print("Blue only:", blue_only)
print("Exactly one team:", either_team_but_not_both)

# Problem C: find people who registered for every required workshop.
registrations = [
	{"Ari", "Bo", "Cam"},
	{"Bo", "Cam", "Dee"},
	{"Bo", "Cam", "Eli"},
]
registered_for_all = set.intersection(*registrations)
print("Registered for every workshop:", registered_for_all)

# If there are no input groups, intersection of all groups is ambiguous for
# an application. Handle that case explicitly instead of calling
# set.intersection(*empty_groups), which has no first set argument.
empty_groups = []
if empty_groups:
	common_to_empty_groups = set.intersection(*empty_groups)
else:
	common_to_empty_groups = set()
print("Common items when no groups were supplied:", common_to_empty_groups)

# Problem D: find values appearing in exactly one of several groups.
# Reduce symmetric difference across all sets for odd-occurrence membership.
groups = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
odd_occurrence_values = set()
for group in groups:
	odd_occurrence_values ^= group
print("Values present in an odd number of groups:", odd_occurrence_values)

# ==========================
# 12. When to use sets
# ==========================
# Use a set when you need:
# - uniqueness (for example, de-duplicating hashable values);
# - fast membership checks against many values;
# - union, intersection, difference, or symmetric difference;
# - an unordered collection where duplicates and positions do not matter.
#
# Use a frozenset when the collection must not change and needs to be
# hashable, such as a dictionary key or an element of another set.
#
# Use a list or tuple when order, indexing, or duplicate occurrences matter.

# Sets compare equal when they contain the same elements, regardless of
# iteration order. len() counts unique elements, and an empty set is false
# in a Boolean context.
print("Set equality ignores order:", {1, 2, 3} == {3, 2, 1})
print("Number of unique elements:", len({1, 1, 2, 3}))
print("bool(set()) =", bool(set()))

# ==========================
# 13. Practice problems
# ==========================
# 1. Remove duplicate words from a list. Is the resulting order important?
# 2. Given two lists of student IDs, find IDs present in both.
# 3. Compare two club rosters and report shared members and members exclusive
#    to each club.
# 4. Given three shopping lists, find the products appearing on all lists.
# 5. Given several sets, find values that occur in an odd number of sets.
# 6. Convert a group of permissions to a frozenset and use it as a
#    dictionary key.
