'''
Control Flow in Python

1. What control flow is
2. if statements
3. if / else statements
4. if / elif / else chains
5. Conditions, comparisons, and truthiness
6. for loops
7. while loops
8. break and continue
9. Loop else clauses
10. Nested loops
11. pass
12. match / case
13. Choosing a control-flow structure
14. Common mistakes
15. Practice problems
'''

# ==========================
# 1. What control flow is
# ==========================
# Control flow is the order in which Python executes statements.
# By default, statements run from top to bottom. Conditions and loops let
# a program choose between paths or repeat a block of code.

# ==========================
# 2. if statements
# ==========================
temperature = 24

# An if block runs only when its condition is truthy.
# The colon starts the block; indentation defines its body.
if temperature > 20:
	print("The temperature is above 20.")

# A condition can use comparisons, membership, or function results.
language = "Python"
if language in ("Python", "Java"):
	print(language, "is in the supported languages.")

# ==========================
# 3. if / else statements
# ==========================
number = 7

# Exactly one branch is selected: the if block when its condition is true,
# otherwise the else block.
if number % 2 == 0:
	print(number, "is even.")
else:
	print(number, "is odd.")

# ==========================
# 4. if / elif / else chains
# ==========================
score = 84

# elif means "else if". Python checks conditions from top to bottom and
# executes only the first matching branch. else is optional and catches
# all remaining cases.
if score >= 90:
	grade = "A"
elif score >= 80:
	grade = "B"
elif score >= 70:
	grade = "C"
else:
	grade = "Needs improvement"

print("Grade:", grade)

# Order conditions from most specific/highest threshold to least, or an
# earlier branch may capture cases intended for a later one.

# ==========================
# 5. Conditions, comparisons, and truthiness
# ==========================
age = 21
has_ticket = True

# Combine conditions with and, or, and not. Use parentheses to make
# compound expressions easier to understand.
if age >= 18 and has_ticket:
	print("Entry is allowed.")

if age < 13 or age >= 65:
	print("Discount may apply.")
else:
	print("Standard age category.")

if not has_ticket:
	print("A ticket is required.")

# Many values can be used directly as conditions. Empty strings and
# collections, numeric zero, None, and False are falsy; non-empty values
# are generally truthy.
user_name = ""
if user_name:
	print("Welcome,", user_name)
else:
	print("No user name was provided.")

items = [0]
if items:
	print("The list has at least one item.")

# Truthiness tests emptiness/zero-like values, not whether a value has a
# particular meaning. Use "is None" when specifically checking for None.
optional_count = 0
if optional_count is None:
	print("No count was supplied.")
else:
	print("Count supplied:", optional_count)

# Comparison operators include ==, !=, <, <=, >, and >=.
# Membership uses in / not in; identity checks use is / is not.
allowed_users = {"Asha", "Noah"}
current_user = "Asha"
if current_user in allowed_users:
	print(current_user, "is allowed.")

# Chained comparisons are useful for inclusive ranges.
value = 8
if 1 <= value <= 10:
	print(value, "is between 1 and 10.")

# ==========================
# 6. for loops
# ==========================
# A for loop visits each item in an iterable, such as a string, list,
# tuple, set, dictionary, or range.
for color in ("red", "green", "blue"):
	print("Color:", color)

# range(stop) produces integers starting at 0 and ending before stop.
for index in range(3):
	print("Index:", index)

# range(start, stop, step) controls the start and increment; stop is excluded.
for number in range(2, 11, 2):
	print("Even number:", number)

# A negative step can count backward.
for countdown in range(3, 0, -1):
	print("Countdown:", countdown)

# enumerate() provides an index and item without manually tracking a counter.
names = ["Mina", "Ravi", "Asha"]
for index, name in enumerate(names):
	print(f"{index}: {name}")

# Give enumerate() a starting index when zero-based indexing is not wanted.
for position, name in enumerate(names, start=1):
	print(f"{position}. {name}")

# zip() iterates over corresponding items from multiple iterables.
# By default, it stops when the shortest iterable is exhausted.
subjects = ("Math", "Science", "History")
marks = (92, 85, 88)
for subject, mark in zip(subjects, marks):
	print(f"{subject}: {mark}")

# Use strict=True (Python 3.10+) when different iterable lengths should be
# treated as an error instead of silently stopping at the shortest.
# list(zip((1, 2), ("a",), strict=True)) raises ValueError.

# Iterating over a dictionary visits its keys by default. Use items() to
# unpack keys and values.
prices = {"book": 12, "pen": 2}
for product, price in prices.items():
	print(f"{product}: ${price}")

# ==========================
# 7. while loops
# ==========================
# A while loop repeats as long as its condition is truthy. Change state
# inside the loop so the condition eventually becomes false.
count = 1
while count <= 3:
	print("Count:", count)
	count += 1

# A sentinel value can stop a loop when it is encountered.
responses = ["yes", "yes", "stop", "yes"]
response_index = 0
while response_index < len(responses):
	response = responses[response_index]
	if response == "stop":
		print("Stop command received.")
		break
	print("Response:", response)
	response_index += 1

# Be careful not to create an infinite loop: ensure the condition can
# become false, or include a deliberate break condition.

# ==========================
# 8. break and continue
# ==========================
# break immediately exits the nearest enclosing loop.
for number in range(1, 6):
	if number == 4:
		break
	print("Before break:", number)

# continue skips the rest of the current iteration and begins the next one.
for number in range(1, 6):
	if number % 2 == 0:
		continue
	print("Odd number:", number)

# break and continue affect only the nearest loop. In nested loops, the
# inner loop's break does not automatically exit the outer loop.

# ==========================
# 9. Loop else clauses
# ==========================
# A loop's else block runs when the loop finishes normally, including when
# it has zero iterations. It does not run when that loop exits via break.
for candidate in (2, 3, 5, 7):
	if candidate < 0:
		print("Found a negative number.")
		break
else:
	print("No negative number found.")

# A practical use: search for a target and report only if it was not found.
target = "Mina"
for name in names:
	if name == target:
		print("Found:", target)
		break
else:
	print("Not found:", target)

# continue does not suppress the loop's else clause; only break does.

# ==========================
# 10. Nested loops
# ==========================
# A loop can be placed inside another loop. The inner loop runs fully for
# each outer-loop iteration unless it is interrupted.
for row in range(1, 4):
	for column in range(1, 3):
		print(f"({row}, {column})")

# Nested loops are useful for grids and pairs, but their work can grow
# quickly. Here the inner operation runs 3 * 2 times.

# ==========================
# 11. pass
# ==========================
# pass is a no-operation statement. It is useful as a temporary placeholder
# where Python syntax requires a statement.
needs_implementation = False
if needs_implementation:
	pass  # Replace with the intended behavior when it is known.
else:
	print("No placeholder branch is needed right now.")

# ==========================
# 12. match / case
# ==========================
# match / case performs structural pattern matching (Python 3.10+).
# It can make dispatch on a value clearer than a long equality chain.
command = "start"

match command:
	case "start":
		print("Starting...")
	case "stop":
		print("Stopping...")
	case "pause":
		print("Pausing...")
	case _:
		print("Unknown command.")

# _ is the wildcard pattern and matches anything. Cases are tested in order;
# the first matching case is selected.

# Patterns can match and unpack structured values.
point = (0, 5)
match point:
	case (0, y):
		print("Point lies on the vertical axis at y =", y)
	case (x, 0):
		print("Point lies on the horizontal axis at x =", x)
	case (x, y):
		print(f"Point coordinates: x={x}, y={y}")

# A guard adds a condition to a pattern. The case is selected only when
# both the pattern and guard match.
match score:
	case value if value >= 90:
		print("Excellent result.")
	case value if value >= 50:
		print("Passing result.")
	case _:
		print("Keep practicing.")

# ==========================
# 13. Choosing a control-flow structure
# ==========================
# Use:
# - if / elif / else to choose among branches;
# - for to visit items in an iterable or repeat a known number of times;
# - while to repeat until a condition changes;
# - break to exit a loop early and continue to skip an iteration;
# - match / case to dispatch on structured patterns (Python 3.10+).
#
# Prefer direct iteration (for item in items) over indexes when the index
# is not needed. Use enumerate() when both item and index are needed.

# ==========================
# 14. Common mistakes
# ==========================
# - Forgetting the colon after if, elif, else, for, while, or match/case.
# - Incorrect indentation; indentation defines the statement blocks.
# - Using = (assignment) where == (comparison) is intended.
# - Writing conditions in an order that makes later branches unreachable.
# - Creating a while loop whose condition never changes.
# - Assuming a for loop includes the stop value in range(); it does not.
# - Modifying a collection while iterating over it; iterate over a copy or
#   build a new collection instead.
# - Assuming loop else runs after break; it runs only after normal completion.
# - Using truthiness when None needs to be distinguished from 0 or "".

# ==========================
# 15. Practice problems
# ==========================
# 1. Given an integer, print whether it is positive, negative, or zero.
# 2. Convert a numeric score into a grade using if / elif / else.
# 3. Print the multiplication table for a chosen number using for and range.
# 4. Sum the integers from 1 through n using a loop.
# 5. Keep processing a sequence until a sentinel value is encountered.
# 6. Search for a name in a list and use a loop else clause when it is absent.
# 7. Print all coordinate pairs in a small grid using nested loops.
# 8. Use match / case to handle simple commands such as "start", "stop",
#    and "help".
