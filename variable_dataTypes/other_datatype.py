'''
Other Built-in Data Types in Python

1. Overview
2. bool: truth values and logical operations
3. bytes: immutable sequences of byte values
4. bytearray: mutable sequences of byte values
5. memoryview: views of buffer data
6. Converting between text and bytes
7. range: immutable arithmetic sequences of integers
8. None and NoneType
9. Choosing the right type
10. Practice problems
'''

# ==========================
# 1. Overview
# ==========================
# In addition to numbers, strings, lists, tuples, dictionaries, and sets,
# Python has useful built-in types for binary data, integer sequences, and
# the absence of a value:
# - bool: truth values used in conditions
# - bytes: immutable binary data
# - bytearray: mutable binary data
# - memoryview: access to buffer data without copying it
# - range: an immutable sequence of integers, often used in loops
# - None: the single value whose type is NoneType

# ==========================
# 2. bool: truth values and logical operations
# ==========================
# bool has exactly two values: True and False. It is a subclass of int,
# where True behaves like 1 and False like 0, but use bool values to express
# logical results rather than as a replacement for numeric data.
is_ready = True
has_error = False
print("is_ready =", is_ready, type(is_ready))
print("has_error =", has_error, type(has_error))
print("True + True =", True + True)
print("False == 0:", False == 0)

# bool(value) converts a value to its truth value. Common false values
# ("falsy" values) include None, False, numeric zero, and empty collections
# or strings. Most other objects are true ("truthy").
truthiness_examples = (None, False, 0, 0.0, "", [], {}, set())
for value in truthiness_examples:
	print(f"bool({value!r}) =", bool(value))

truthy_examples = ("hello", [0], {"active": False}, 1)
for value in truthy_examples:
	print(f"bool({value!r}) =", bool(value))

# Truthiness checks whether a value is empty/zero-like, not whether it has
# a particular meaning. For example, an empty list is false, while a
# non-empty list containing False is true.
print("bool([False]) =", bool([False]))

# and and or short-circuit: they return one of their operands, not
# necessarily a bool. not always returns a bool.
print("'left' and 'right':", "left" and "right")
print("'' or 'fallback':", "" or "fallback")
print("not []:", not [])

# Use and/or for conditions and short-circuit defaults carefully. Use
# "is None" when distinguishing a missing value from other falsy values.
optional_count = 0
print("optional_count or 10:", optional_count or 10)
print("None-aware default:", 10 if optional_count is None else optional_count)

# Comparison and membership operations usually produce bool values.
print("3 < 5:", 3 < 5)
print("'py' in 'python':", "py" in "python")

# ==========================
# 3. bytes: immutable sequences of byte values
# ==========================
# Each item in bytes is an integer from 0 through 255, not a one-character
# string. bytes literals use a b prefix and can contain ASCII characters
# and escaped byte values.
message_bytes = b"Hello"
escaped_bytes = b"A\x00B"
print("message_bytes =", message_bytes)
print("escaped_bytes =", escaped_bytes)
print("Type:", type(message_bytes))
print("First byte as an integer:", message_bytes[0])
print("Byte value at index 1:", message_bytes[1])

# bytes(iterable) builds bytes from integers in the range 0..255.
bytes_from_numbers = bytes([65, 66, 67])
print("From integer values:", bytes_from_numbers)

# bytes(n) creates n zero-valued bytes; it does not convert the number n
# into its textual digits or binary representation.
zero_bytes = bytes(4)
print("bytes(4) =", zero_bytes)
print("Length of bytes(4):", len(zero_bytes))

# bytes.fromhex() parses pairs of hexadecimal digits. Whitespace between
# pairs is allowed; invalid input raises ValueError.
hex_bytes = bytes.fromhex("48 69 21")
print("From hexadecimal:", hex_bytes)

# bytes is immutable: item assignment is not allowed. It supports sequence
# operations such as indexing, slicing, iteration, membership, and joining.
# Slicing returns another bytes object.
sample_bytes = b"Python"
print("Slice:", sample_bytes[1:4], type(sample_bytes[1:4]))
print("Contains b'th':", b"th" in sample_bytes)
print("Iterated byte values:", list(sample_bytes))
print("Concatenation:", b"Py" + b"thon")
print("Repetition:", b"ha" * 3)
# sample_bytes[0] = ord("p") would raise TypeError.

# bytes also has useful binary-data methods.
binary_text = b"red,green,blue"
print("Split bytes:", binary_text.split(b","))
print("Replace bytes:", binary_text.replace(b"green", b"gold"))
print("Hex representation:", binary_text.hex())

# bytes is immutable and hashable, so it can be used as a dictionary key.
status_by_response = {b"OK": 200, b"NOT FOUND": 404}
print("Status for b'OK':", status_by_response[b"OK"])

# ==========================
# 4. bytearray: mutable sequences of byte values
# ==========================
# bytearray contains integer byte values like bytes, but it can be changed
# in place. Its values must remain in the inclusive range 0..255.
mutable_bytes = bytearray(b"cat")
print("mutable_bytes =", mutable_bytes)
print("Type:", type(mutable_bytes))
print("First byte as an integer:", mutable_bytes[0])

# Assigning a byte replaces that position; append() adds one byte value.
mutable_bytes[0] = ord("b")
mutable_bytes.append(ord("s"))
print("After assignment and append:", mutable_bytes)

# extend() adds values from an iterable. The new values must each be integers
# in the byte range, or a ValueError/TypeError is raised.
mutable_bytes.extend([ord("!"), ord("?")])
print("After extend():", mutable_bytes)

# Other common mutable-sequence operations are insert(), pop(), remove(),
# and clear(). remove(value) removes the first matching byte value.
mutable_bytes.insert(1, ord("!"))
last_byte = mutable_bytes.pop()
mutable_bytes.remove(ord("!"))
print("After insert(), pop(), and remove():", mutable_bytes)
print("Popped byte value:", last_byte)

# Slicing bytearray creates a new bytearray. A slice is not a live view of
# the original object's memory.
mutable_slice = mutable_bytes[0:2]
mutable_slice[0] = ord("C")
print("Changed slice:", mutable_slice)
print("Original remains:", mutable_bytes)

# bytearray is mutable and unhashable, so it cannot be a dictionary key
# or a set element. Convert to bytes when an immutable snapshot is needed.
immutable_snapshot = bytes(mutable_bytes)
print("Immutable snapshot:", immutable_snapshot)

# ==========================
# 5. memoryview: views of buffer data
# ==========================
# memoryview exposes the binary data of an object that supports Python's
# buffer protocol (for example bytes, bytearray, and some arrays) without
# first copying the data. A view is useful when working with large buffers.
buffer = bytearray(b"ABCDE")
view = memoryview(buffer)
print("view =", view)
print("Type:", type(view))
print("Length in elements:", len(view))
print("Number of bytes:", view.nbytes)
print("First element as an integer:", view[0])

# A writable view of a bytearray can change the original buffer.
view[1] = ord("x")
print("Buffer after changing view:", buffer)

# Slicing a memoryview creates another view into the same underlying data,
# rather than a copied bytes/bytearray slice.
part = view[2:4]
part[0] = ord("y")
print("Buffer after changing sliced view:", buffer)
print("Viewed slice as bytes:", part.tobytes())

# A view of immutable bytes is read-only. Attempting to assign through it
# raises TypeError.
read_only_view = memoryview(b"fixed")
print("View of bytes is read-only:", read_only_view.readonly)
print("Read-only view as bytes:", read_only_view.tobytes())
# read_only_view[0] = ord("F") would raise TypeError.

# A view keeps the underlying buffer exported. Resizing a bytearray while
# an active view refers to it raises BufferError. Release views when done.
part.release()
view.release()
buffer.append(ord("!"))
print("Resizable buffer after releasing views:", buffer)

# memoryview can also be used as a context manager to release it reliably.
with memoryview(b"data") as data_view:
	print("Context-managed view as bytes:", data_view.tobytes())
# data_view has been released after the with block.

# ==========================
# 6. Converting between text and bytes
# ==========================
# Text (str) and binary data (bytes/bytearray) are different types.
# Encode text to bytes with a named character encoding, and decode bytes
# back into text using the same encoding.
text = "café"
encoded_text = text.encode("utf-8")
decoded_text = encoded_text.decode("utf-8")
print("Text:", text)
print("UTF-8 bytes:", encoded_text)
print("Decoded text:", decoded_text)

# Encoding affects the byte representation. UTF-8 uses multiple bytes for
# many non-ASCII characters, so byte length can differ from character count.
print("Text character count:", len(text))
print("UTF-8 byte count:", len(encoded_text))

# bytes("text") without an encoding raises TypeError. Specify the encoding
# with str.encode() or str.encode("utf-8"), not bytes(text).
#
# Decoding invalid byte sequences with the default strict error handling
# raises UnicodeDecodeError. Other policies include errors="replace" and
# errors="ignore"; choose deliberately because they may alter data.
invalid_utf8 = b"\xff"
replacement_text = invalid_utf8.decode("utf-8", errors="replace")
print("Replacement text escaped for display:",
	  replacement_text.encode("unicode_escape"))

# Use bytes for fixed binary data; use bytearray when constructing or
# modifying binary data in place.
packet = bytearray(b"ID:")
packet.extend([1, 2, 3])
print("Constructed packet:", packet)
print("Packet as immutable bytes:", bytes(packet))

# ==========================
# 7. range: immutable arithmetic sequences of integers
# ==========================
# range(stop), range(start, stop), and range(start, stop, step) describe
# integer sequences. The stop value is excluded.
zero_to_four = range(5)
three_to_seven = range(3, 8)
even_numbers = range(2, 11, 2)
print("range(5) as a list:", list(zero_to_four))
print("range(3, 8) as a list:", list(three_to_seven))
print("Even numbers:", list(even_numbers))
print("Type:", type(zero_to_four))

# A range stores its start, stop, and step rather than building a list of
# every item. This makes ranges useful for large loops and sequences.
large_range = range(1_000_000)
print("Length of large_range:", len(large_range))

# range arguments must be integers (or integer-like values implementing
# the index protocol); a float such as range(0.0, 3.0) raises TypeError.
# The step cannot be zero.
#
# A negative step counts downward. The stop is still excluded.
countdown = range(5, 0, -1)
print("Countdown:", list(countdown))

# range supports iteration, len(), indexing, slicing, and membership.
counting = range(10, 20, 2)
print("First item:", counting[0])
print("Last item:", counting[-1])
print("Slice:", counting[1:4], type(counting[1:4]))
print("16 is in counting:", 16 in counting)
print("15 is in counting:", 15 in counting)

# A range cannot be changed and does not provide list methods such as
# append(). Convert it to a list if you need a mutable collection.
# counting[0] = 12 would raise TypeError.
mutable_numbers = list(counting)
mutable_numbers.append(20)
print("Converted to a mutable list:", mutable_numbers)

# range() is commonly used to repeat an action or to access sequence indexes.
for number in range(1, 4):
	print("Loop number:", number)

names = ["Asha", "Noah", "Mina"]
for index in range(len(names)):
	print(f"names[{index}] = {names[index]}")

# When both index and value are needed, enumerate() is usually clearer.
for index, name in enumerate(names):
	print(f"Name {index}: {name}")

# ==========================
# 8. None and NoneType
# ==========================
# None is Python's sole NoneType value. It commonly means "no value",
# "not available", or "no result".
result = None
print("result =", result)
print("type(result) is NoneType:", type(result) is type(None))
print("None is false in a condition:", bool(None))

# Test for None with identity operators (is / is not), not equality.
if result is None:
	print("No result is available")

if result is not None:
	print("A result is available")

# None is distinct from 0, False, an empty string, and an empty collection,
# even though all of those values are false in a Boolean context.
print("None == 0:", None == 0)
print("None == False:", None == False)
print("None == '':", None == "")
print("None == []:", None == [])

# A function that reaches its end without a return statement returns None.
def print_greeting(name):
	"""Print a greeting; this function has no explicit return value."""
	print(f"Hello, {name}!")


greeting_result = print_greeting("Asha")
print("Return value:", greeting_result)

# Use None as a default when it is important to distinguish an omitted
# argument from a valid value such as 0 or an empty string.
def describe_value(value=None):
	"""Describe whether an optional value was supplied."""
	if value is None:
		return "No value supplied"
	return f"Value supplied: {value!r}"


print(describe_value())
print(describe_value(0))

# Do not call methods on None; it has no collection or text operations.
# For example, None.append(1) raises AttributeError.

# ==========================
# 9. Choosing the right type
# ==========================
# Use:
# - bool for true/false conditions and logical results;
# - bytes for immutable binary data and binary keys;
# - bytearray for binary data that must be modified;
# - memoryview to inspect or modify buffer data without making a slice copy;
# - range for a memory-efficient arithmetic sequence of integers;
# - None to represent the deliberate absence of a value.
#
# Use str for human-readable text. Encode/decode explicitly when crossing
# between text and binary data.
#
# Convert range to list only when you need a mutable list or list-specific
# operations. Check optional values with "is None" before using them.
# Prefer explicit conditions over relying on truthiness when zero, False,
# or an empty collection could be a valid supplied value.

# ==========================
# 10. Practice problems
# ==========================
# 1. Test how bool() treats zero, non-empty collections, and empty strings.
# 2. Write a condition that uses a boolean operator without losing a valid
#    value such as 0.
# 3. Create a bytes object from integer values and print its hexadecimal form.
# 4. Build a bytearray, change one byte, and convert it to bytes.
# 5. Create a memoryview over a bytearray and modify a byte through the view.
# 6. Encode non-ASCII text as UTF-8 and compare character and byte counts.
# 7. Use range() to print all multiples of 3 below 30.
# 8. Use a negative-step range to count down from 10 to 1.
# 9. Write a function that returns None when a search has no result, and
#    check its result using "is None".
