'''
Strings in Python (str)

1. What strings are
   - str stores text as a sequence of Unicode code points.
   - Strings can use single quotes, double quotes, or triple quotes.
2. Indexing, negative indexing, and slicing
3. Immutability
4. Useful string methods: split(), join(), strip(), replace()
5. Searching, counting, and membership
6. String formatting and f-strings
7. Character encoding basics: Unicode, code points, bytes, UTF-8
8. Practice problems
   - palindrome
   - anagrams
   - character frequency
   - reversing words
   - removing duplicate characters
'''

# ==========================
# 1. What strings are
# ==========================
single_quoted = 'Hello'
double_quoted = "Python strings"
text_with_apostrophe = "It's a sunny day"
multiline_text = """This string
uses more than one line."""

print("single_quoted =", single_quoted)
print("double_quoted =", double_quoted)
print("text_with_apostrophe =", text_with_apostrophe)
print("multiline_text =", multiline_text)
print("Type:", type(single_quoted))

# A string is a sequence: len() counts its code points and iteration visits
# those code points one at a time.
word = "Python"
print("Length of Python:", len(word))
print("Characters:", list(word))

# ==========================
# 2. Indexing and slicing
# ==========================
sample_text = "Python"

# Indexes start at 0. An index selects one character.
first_character = sample_text[0]
third_character = sample_text[2]
last_character = sample_text[-1]
second_last_character = sample_text[-2]

print("First character:", first_character)
print("Third character:", third_character)
print("Last character:", last_character)
print("Second-last character:", second_last_character)

# Negative indexes count backward from the end: -1 is the last character.
# An index outside the string raises IndexError.

# Slice form: text[start:stop:step]
# start is included, stop is excluded, and step defaults to 1.
print("sample_text[0:2] =", sample_text[0:2])
print("sample_text[2:5] =", sample_text[2:5])
print("sample_text[:3] =", sample_text[:3])
print("sample_text[3:] =", sample_text[3:])
print("sample_text[:] =", sample_text[:])
print("sample_text[::2] =", sample_text[::2])
print("sample_text[::-1] =", sample_text[::-1])

# Slices safely stop at the string boundary, even if stop is too large.
print("sample_text[2:100] =", sample_text[2:100])

# ==========================
# 3. Strings are immutable
# ==========================
original_text = "hello"
uppercase_text = original_text.upper()
replaced_text = original_text.replace("h", "H")

print("Original text:", original_text)
print("upper() result:", uppercase_text)
print("replace() result:", replaced_text)
print("Original is unchanged:", original_text)

# Immutable means a character cannot be assigned in place, for example:
# original_text[0] = "H"  # This raises TypeError.
# String methods return a new string. Save the result to keep it.
original_text = original_text.replace("h", "H")
print("Updated variable:", original_text)

# ==========================
# 4. Common string methods
# ==========================

# split() separates a string into a list. With no separator, runs of
# whitespace are treated as one separator and surrounding whitespace is ignored.
sentence = "  Learn   Python strings  "
words = sentence.split()
comma_separated = "red,green,blue"
colors = comma_separated.split(",")
print("sentence.split() =", words)
print('comma_separated.split(",") =', colors)

# join() combines strings from an iterable, placing the separator between them.
# Every item must be a string.
joined_words = " ".join(words)
joined_colors = " | ".join(colors)
print('" ".join(words) =', joined_words)
print('" | ".join(colors) =', joined_colors)

# strip() removes whitespace from both ends, not from the middle.
messy_text = "  hello Python  \n"
clean_text = messy_text.strip()
left_cleaned = messy_text.lstrip()
right_cleaned = messy_text.rstrip()
print("strip() =", repr(clean_text))
print("lstrip() =", repr(left_cleaned))
print("rstrip() =", repr(right_cleaned))

# strip(chars) removes any listed characters from the ends; it does not remove
# an exact prefix or suffix. Use removeprefix()/removesuffix() for that purpose.
trimmed_marks = "...title!!!".strip(".!?")
prefixed_text = "unhappy".removeprefix("un")
print('"...title!!!".strip(".!?") =', trimmed_marks)
print('"unhappy".removeprefix("un") =', prefixed_text)

# replace(old, new, count) returns a new string. count limits replacements.
phrase = "cat, dog, cat"
all_replaced = phrase.replace("cat", "fox")
one_replaced = phrase.replace("cat", "fox", 1)
print("Replace all:", all_replaced)
print("Replace once:", one_replaced)

# ==========================
# 5. Searching, counting, and membership
# ==========================
search_text = "Python makes learning Python fun"

# find() returns the first matching index, or -1 if it is not found.
# index() also returns the first matching index, but raises ValueError if absent.
first_python = search_text.find("Python")
missing_word = search_text.find("Java")
python_index = search_text.index("Python")
print('find("Python") =', first_python)
print('find("Java") =', missing_word)
print('index("Python") =', python_index)

# count() counts non-overlapping occurrences.
python_count = search_text.count("Python")
print('count("Python") =', python_count)

# in and not in test whether a substring occurs. Matching is case-sensitive.
has_learning = "learning" in search_text
has_lowercase_python = "python" in search_text
missing_java = "Java" not in search_text
print('"learning" in search_text =', has_learning)
print('"python" in search_text =', has_lowercase_python)
print('"Java" not in search_text =', missing_java)

# Other useful checks: startswith(), endswith(), isalpha(), isdigit(), isspace().
file_name = "notes.txt"
print('file_name.endswith(".txt") =', file_name.endswith(".txt"))
print('"123".isdigit() =', "123".isdigit())

# ==========================
# 6. String formatting and f-strings
# ==========================
student_name = "Asha"
completed_lessons = 5
lesson_total = 8
progress = completed_lessons / lesson_total * 100

# An f-string evaluates expressions inside braces when the string is created.
progress_message = (
	f"{student_name} completed {completed_lessons} of {lesson_total} lessons."
)
print(progress_message)

# A format specifier controls how a value is displayed.
price = 12.5
formatted_price = f"Price: ${price:.2f}"
formatted_progress = f"Progress: {progress:.1f}%"
print(formatted_price)
print(formatted_progress)

# Expressions and method calls can go inside braces.
print(f"Name in uppercase: {student_name.upper()}")
print(f"Next lesson: {completed_lessons + 1}")

# Double braces produce literal braces in the result.
json_like_text = f"{{'name': '{student_name}'}}"
print("Literal braces:", json_like_text)

# Older alternatives include str.format() and %-formatting.
format_method_text = "Hello, {}!".format(student_name)
percent_format_text = "Hello, %s!" % student_name
print("format() example:", format_method_text)
print("%-format example:", percent_format_text)

# ==========================
# 7. Character encoding basics
# ==========================
# str is text (Unicode); bytes is raw byte data. Encoding converts text to bytes,
# and decoding converts bytes back to text. UTF-8 is a common encoding.
unicode_text = "cafe \u00e9"
utf8_bytes = unicode_text.encode("utf-8")
decoded_text = utf8_bytes.decode("utf-8")

print("Unicode text:", unicode_text)
print("UTF-8 bytes:", utf8_bytes)
print("Decoded text:", decoded_text)
print("Text type:", type(unicode_text))
print("Encoded type:", type(utf8_bytes))

# ord() gives a code point number; chr() creates a character from a code point.
letter_e = "A"
code_point = ord(letter_e)
character_again = chr(code_point)
print("ord('A') =", code_point)
print("chr(65) =", character_again)

# ASCII covers a small set of characters; UTF-8 represents Unicode text using
# one or more bytes per character. Therefore len(text) and len(encoded_bytes)
# can differ. A visible symbol can also consist of multiple code points.
accented_text = "é"
accented_bytes = accented_text.encode("utf-8")
print("len('é') =", len(accented_text))
print("len('é'.encode('utf-8')) =", len(accented_bytes))

# Decode with the same encoding used to encode. Invalid byte sequences can raise
# UnicodeDecodeError; invalid text for an encoding can raise UnicodeEncodeError.

# ==========================
# 8. Practice problems
# ==========================

def normalize_letters(text):
	"""Lowercase text and keep only letters and digits."""
	return "".join(
		character.casefold()
		for character in text
		if character.isalnum()
	)


def is_palindrome(text):
	"""Return whether text reads the same forward and backward."""
	normalized_text = normalize_letters(text)
	return normalized_text == normalized_text[::-1]


def are_anagrams(first_text, second_text):
	"""Return whether two texts contain the same letters and digits."""
	first_normalized = normalize_letters(first_text)
	second_normalized = normalize_letters(second_text)
	return sorted(first_normalized) == sorted(second_normalized)


def character_frequency(text):
	"""Return a dictionary containing each character's number of occurrences."""
	frequencies = {}
	for character in text:
		frequencies[character] = frequencies.get(character, 0) + 1
	return frequencies


def reverse_word_order(sentence):
	"""Return the words in reverse order, with one space between each word."""
	words = sentence.split()
	return " ".join(words[::-1])


def remove_duplicate_characters(text):
	"""Keep each character's first occurrence and preserve the original order."""
	return "".join(dict.fromkeys(text))


print("Palindrome:", is_palindrome("A man, a plan, a canal: Panama"))
print("Anagrams:", are_anagrams("Dormitory", "Dirty room"))
print("Character frequency:", character_frequency("banana"))
print("Reverse word order:", reverse_word_order("Python is fun to learn"))
print("Remove duplicate characters:", remove_duplicate_characters("banana"))

# Practice notes:
# - The palindrome and anagram functions ignore spaces and punctuation and
#   compare text without case differences.
# - character_frequency() counts spaces and punctuation too. Filter them first
#   if a problem asks for letters only.
# - reverse_word_order() reverses word order, not the letters inside each word.
# - dict preserves insertion order, so dict.fromkeys() keeps first occurrences.

# ==========================
# 9. More everyday operations
# ==========================

# + joins strings and * repeats a string. Both create new strings.
greeting = "Hello" + ", " + "Python"
repeated_separator = "-" * 10
print("Concatenation:", greeting)
print("Repetition:", repeated_separator)

# A string can be compared with == and !=. Comparisons are case-sensitive.
# Ordering comparisons use lexicographic (character-by-character) order.
print('"Python" == "python":', "Python" == "python")
print('"apple" < "banana":', "apple" < "banana")

# Convert numbers explicitly before concatenating them with strings.
age = 20
age_message = "Age: " + str(age)
print(age_message)

# ==========================
# 10. Case conversion and character tests
# ==========================
mixed_case = "PyThOn Is FUN"
print("lower():", mixed_case.lower())
print("upper():", mixed_case.upper())
print("title():", mixed_case.title())
print("capitalize():", mixed_case.capitalize())
print("swapcase():", mixed_case.swapcase())

# casefold() is intended for caseless text comparisons; it can be more thorough
# than lower() for some Unicode characters.
first_word = "Straße"
second_word = "STRASSE"
same_ignoring_case = first_word.casefold() == second_word.casefold()
print("Same ignoring case:", same_ignoring_case)

# isalpha(), isdigit(), isdecimal(), and isalnum() test every character.
# They return False for an empty string. Spaces and punctuation are not letters.
print('"Python".isalpha():', "Python".isalpha())
print('"123".isdecimal():', "123".isdecimal())
print('"room 7".isalnum():', "room 7".isalnum())
print('"".isalpha():', "".isalpha())

# ==========================
# 11. Escape sequences and raw strings
# ==========================
# Backslash introduces special characters such as newline and tab.
escaped_text = "First line\nSecond line\tIndented"
quoted_text = "She said, \"Hello!\""
backslash_text = "A backslash: \\"  #backslash_text = "A backslash: \\\"
print("Escaped text:", escaped_text)
print("Quoted text:", quoted_text)
print("Backslash text:", backslash_text)

# A raw string keeps most backslashes literal. It is handy for regular
# expressions and Windows paths. A raw string cannot end with one odd backslash.
windows_path = r"C:\Users\Asha\notes"
print("Raw path:", windows_path)

# ==========================
# 12. Splitting once and line handling
# ==========================
# partition(separator) splits at the first match and always returns a 3-tuple:
# (text_before, separator, text_after). rpartition() uses the last match.
email_address = "asha@example.com"
email_name, at_sign, email_domain = email_address.partition("@")
print("Email name:", email_name)
print("Email separator:", at_sign)
print("Email domain:", email_domain)

# splitlines() separates text at line boundaries.
multiline_message = "First line\nSecond line\nThird line"
message_lines = multiline_message.splitlines()
print("Lines:", message_lines)

# ==========================
# 13. Unicode normalization
# ==========================
# Some text that looks identical can use different code-point sequences. For
# example, an accented letter may be one code point or a letter plus accent.
# Normalize text before comparison when canonical Unicode equivalence matters.
import unicodedata

composed_accent = "\u00e9"
decomposed_accent = "e\u0301"
normalized_composed = unicodedata.normalize("NFC", composed_accent)
normalized_decomposed = unicodedata.normalize("NFC", decomposed_accent)
print("Equal before normalization:", composed_accent == decomposed_accent)
print(
	"Equal after NFC normalization:",
	normalized_composed == normalized_decomposed,
)

# ==========================
# 14. Efficiently building strings
# ==========================
# For a few pieces, + is clear and fine. For many pieces, collect them and use
# join() once; repeated concatenation in a loop can create many intermediate
# strings because strings cannot be modified in place.
number_words = ["one", "two", "three"]
efficient_result = ", ".join(number_words)
print("Joined result:", efficient_result)

# Common reminders:
# - input() returns str; convert it with int() or float() before arithmetic.
# - Use == to compare string values, not is (which tests object identity).
# - Strings are case-sensitive unless you normalize/casefold them explicitly.
# - Use encode() to make bytes for storage or transmission, and decode() to
#   turn bytes back into text using the correct encoding.


