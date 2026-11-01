'''
Python Operators and Expressions

1. What operators do
2. Arithmetic operators
3. Comparison operators
4. Logical operators and truthiness
5. Assignment and augmented assignment
6. Membership operators
7. Identity operators
8. Bitwise operators
9. Conditional expressions and the walrus operator
10. Operator precedence and associativity
11. Common operator pitfalls
12. Practice problems
'''

# ==========================
# 1. What operators do
# ==========================
# An operator performs an operation on one or more values (operands).
# An expression combines values and operators and evaluates to a result.
total = 4 + 6
print("4 + 6 =", total)

# Some operators work with different types in different ways. For example,
# + adds numbers but concatenates strings or sequences.
print("Add numbers:", 4 + 6)
print("Join strings:", "py" + "thon")
print("Join lists:", [1, 2] + [3])

# ==========================
# 2. Arithmetic operators
# ==========================
first = 17
second = 5

print("Addition:", first + second)
print("Subtraction:", first - second)
print("Multiplication:", first * second)
print("True division:", first / second)
print("Floor division:", first // second)
print("Remainder:", first % second)
print("Exponentiation:", first ** second)

# / performs true division and normally returns a float, even when the
# quotient is whole. // rounds the quotient down toward negative infinity.
print("10 / 2 =", 10 / 2)
print("10 // 3 =", 10 // 3)
print("-10 // 3 =", -10 // 3)

# For integers, a = (a // b) * b + (a % b). The remainder has the sign of
# the divisor (or is zero), which explains negative-operand results.
print("-10 % 3 =", -10 % 3)
print("10 % -3 =", 10 % -3)
print("divmod(17, 5) =", divmod(17, 5))

# Division and remainder by zero raise ZeroDivisionError.
# For example: 5 / 0, 5 // 0, and 5 % 0 are invalid.

# Unary + and - indicate or change a numeric sign.
number = 8
print("Unary +:", +number)
print("Unary -:", -number)

# Repetition with * is also defined for sequences and an integer count.
print("Repeat a string:", "ha" * 3)
print("Repeat a list:", [1, 2] * 2)

# Floating-point arithmetic can have small representation errors because
# many decimal fractions cannot be represented exactly in binary.
print("0.1 + 0.2 =", 0.1 + 0.2)
print("Approximately equal:", abs((0.1 + 0.2) - 0.3) < 1e-9)

# ==========================
# 3. Comparison operators
# ==========================
left_value = 7
right_value = 10

print("Equal (==):", left_value == right_value)
print("Not equal (!=):", left_value != right_value)
print("Less than (<):", left_value < right_value)
print("Less than or equal (<=):", left_value <= right_value)
print("Greater than (>):", left_value > right_value)
print("Greater than or equal (>=):", left_value >= right_value)

# Comparisons normally produce bool values. They can be used directly
# in if statements and other conditions.
if left_value < right_value:
	print("left_value is smaller")

# Comparisons can be chained. This is equivalent to checking both
# comparisons, with the middle expression evaluated only once.
age = 20
print("Age in range:", 18 <= age < 65)
# Equivalent: 18 <= age and age < 65

# Strings compare lexicographically by Unicode code point; comparisons are
# case-sensitive. For language-aware sorting, use an appropriate library.
print("'apple' < 'banana':", "apple" < "banana")
print("'A' < 'a':", "A" < "a")

# Different unrelated types generally cannot be ordered in Python 3:
# 1 < "2" raises TypeError. Equality comparisons across types are allowed,
# and usually return False when the values are not equal.
print("1 == '1':", 1 == "1")

# ==========================
# 4. Logical operators and truthiness
# ==========================
# and, or, and not combine or invert truth values.
is_logged_in = True
has_permission = False
print("Can proceed:", is_logged_in and has_permission)
print("Either condition:", is_logged_in or has_permission)
print("Not logged in:", not is_logged_in)

# Values are considered false in a condition when they are False, None,
# numeric zero, or an empty built-in collection/string. Most other values
# are truthy. bool(value) returns the truth value explicitly.
print("bool(0):", bool(0))
print("bool(''):", bool(""))
print("bool([]):", bool([]))
print("bool('hello'):", bool("hello"))
print("bool([0]):", bool([0]))

# and and or short-circuit: they stop as soon as the result is determined.
# They return one of their operands, not necessarily True or False.
print("'first' and 'second':", "first" and "second")
print("'' or 'fallback':", "" or "fallback")
print("0 or 10:", 0 or 10)

# Use "is None" when None has a special meaning. A truthiness fallback
# such as value or default also replaces valid falsy values such as 0.
optional_limit = 0
limit_with_or = optional_limit or 10
limit_preserving_zero = (
	10 if optional_limit is None else optional_limit
)
print("Limit using or:", limit_with_or)
print("Limit preserving zero:", limit_preserving_zero)

# not has lower precedence than comparisons, so "not x == y" means
# "not (x == y)". Parentheses make complex conditions easier to read.
print("not (3 == 4):", not 3 == 4)

# ==========================
# 5. Assignment and augmented assignment
# ==========================
# = assigns a value to a name; it is not an equality comparison.
score = 10
print("Initial score:", score)

# Chained assignment assigns the same object/value to multiple names.
first_score = second_score = 0
print("Chained assignment:", first_score, second_score)

# Multiple assignment unpacks values from an iterable.
red, green, blue = (255, 128, 0)
print("RGB:", red, green, blue)

# Augmented assignment combines an operation with assignment.
score += 5
score -= 2
score *= 3
score //= 2
score %= 7
print("Score after augmented assignments:", score)

# Other augmented forms include /=, **=, &=, |=, ^=, <<=, >>=.
power = 2
power **= 3
print("After **=:", power)

# For mutable objects, an augmented operation may update the object in
# place. For immutable objects such as int and str, it binds the name to
# a resulting value. Do not rely on every custom type behaving identically.
items = [1, 2]
same_items = items
items += [3]
print("List after +=:", items)
print("Alias sees in-place list change:", same_items)

# ==========================
# 6. Membership operators
# ==========================
# in and not in test whether an item is contained in an object.
fruit_names = ["apple", "pear", "plum"]
print("'pear' in list:", "pear" in fruit_names)
print("'orange' not in list:", "orange" not in fruit_names)
print("'thon' in string:", "thon" in "python")

# For dictionaries, membership tests keys, not values.
profile = {"name": "Asha", "active": True}
print("'name' in dictionary:", "name" in profile)
print("'Asha' in dictionary:", "Asha" in profile)
print("'Asha' in dictionary values:", "Asha" in profile.values())

# Membership behavior depends on the type. For large numbers of repeated
# membership tests, a set is often more suitable than a list.
allowed_codes = {200, 201, 204}
print("200 is allowed:", 200 in allowed_codes)

# ==========================
# 7. Identity operators
# ==========================
# is and is not test whether two names refer to the very same object.
# They do not test whether two objects merely have equal contents.
original_list = [1, 2]
same_reference = original_list
separate_list = [1, 2]
print("Original is its alias:", original_list is same_reference)
print("Original equals separate list:", original_list == separate_list)
print("Original is separate list:", original_list is separate_list)

# Use == to compare values. Use is primarily for singleton checks such as
# None; do not use is to compare strings or numbers.
maybe_value = None
print("Value is None:", maybe_value is None)
print("Value is not None:", maybe_value is not None)

# ==========================
# 8. Bitwise operators
# ==========================
# Bitwise operators work on the binary digits of integers.
bit_a = 0b1100  # 12
bit_b = 0b1010  # 10

print("bit_a in binary:", bin(bit_a))
print("bit_b in binary:", bin(bit_b))
print("AND (&):", bin(bit_a & bit_b))
print("OR (|):", bin(bit_a | bit_b))
print("XOR (^):", bin(bit_a ^ bit_b))
print("NOT (~) of 12:", ~bit_a)
print("Left shift (<<):", bit_a << 1)
print("Right shift (>>):", bit_a >> 1)

# For non-negative integers, shifting left by n bits multiplies by 2**n;
# shifting right by n bits is like floor division by 2**n.
print("5 << 2 =", 5 << 2)
print("20 >> 2 =", 20 >> 2)

# Python bitwise operations on negative integers behave as though integers
# have an unbounded two's-complement representation.
print("-5 >> 1 =", -5 >> 1)
print("~5 =", ~5)

# Bitwise operators are distinct from logical operators:
# & and | operate on integer bits (or can be overloaded by types);
# and and or perform truth testing and short-circuit.
print("True and False:", True and False)
print("True & False:", True & False)

# ==========================
# 9. Conditional expressions and the walrus operator
# ==========================
# A conditional expression selects one of two values:
# value_if_true if condition else value_if_false
temperature = 16
weather_label = "warm" if temperature >= 20 else "cool"
print("Weather label:", weather_label)

# The assignment expression := ("walrus operator", Python 3.8+) assigns
# a value as part of a larger expression. Parentheses are often required
# for clarity and in certain contexts.
message = "Python"
if (message_length := len(message)) > 5:
	print("Length greater than five:", message_length)

# Use assignment expressions sparingly; a separate assignment can be
# easier to read when the expression becomes complex.

'''
==========================
10. Operator precedence and associativity
==========================
Precedence determines which operators group first. Parentheses can make
the intended grouping explicit. From higher to lower, common operators:
1. Parentheses, indexing, attribute access, function calls
2. Exponentiation **
3. Unary +, -, ~
4. *, /, //, %, and @
5. + and -
6. << and >>
7. Bitwise &, ^, |
8. Comparisons, in, not in, is, is not
9. not
10. and
11. or
12. Conditional expression: x if condition else y
Assignment expressions and lambda expressions have lower precedence.
'''
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

# ** groups from right to left: 2 ** 3 ** 2 means 2 ** (3 ** 2).
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)

# Exponentiation binds more tightly than a unary minus on its left:
print("-2 ** 2 =", -2 ** 2)
print("(-2) ** 2 =", (-2) ** 2)

# Comparisons can chain, but mixing logical operators and comparisons can
# still be hard to scan. Use parentheses for clarity.
value = 8
print("In range:", 0 <= value < 10)
print("Explicit grouping:", (value > 0) and (value < 10))


'''
==========================
11. Common operator pitfalls
==========================
= assigns; == compares values; is compares object identity.
/ is true division; // is floor division, including for negative results.
and/or return operands; not returns a bool.
in checks dictionary keys, not dictionary values.
Floating-point equality can be surprising; compare within a tolerance
when appropriate rather than expecting exact decimal arithmetic.
Parentheses improve clarity and prevent precedence mistakes.

Some operators are overloaded by types. For example, + concatenates
strings, and custom classes can define how operators work. The meaning
therefore depends on the operand types.

@ is the matrix multiplication operator. Built-in numeric types do not
implement matrix multiplication; array libraries can define its behavior.

==========================
12. Practice problems
==========================
1. Given a number, print whether it is even using % and a comparison.
2. Use chained comparisons to test whether a value is in a range.
3. Given two booleans, compare the results of and, or, and ^.
4. Check whether a word occurs in a sentence and whether a key occurs
   in a dictionary.
5. Use bitwise & to test whether an integer is even:
   (number & 1) == 0
6. Compute quotient and remainder using //, %, and divmod().
7. Rewrite an expression with parentheses to make its precedence clear.
8. Use a conditional expression to label a number positive, negative,
   or zero.
'''