'''
Numeric Data Types in Python

1. Numeric types in Python
   - int: whole numbers (positive, negative, zero)
   - float: decimal numbers
   - complex: numbers with real and imaginary parts
   - bool: logical values, but also considered a subclass of int in Python

2. Integer type (int)
   - int is used for exact whole-number values.
   - It supports large values without losing precision.
   - Negative numbers are also valid.

3. Float type (float)
   - float is used for decimal values.
   - It is stored in binary floating-point format, so some decimal values may
     not be represented exactly.

4. Complex type (complex)
   - complex numbers are written as a + bj
   - a is the real part
   - b is the imaginary part

5. Arithmetic operators
   +, -, *, /, //, %, **

6. Division
   - / gives exact floating-point result
   - // gives floor division
   - % gives remainder

7. Operator precedence
   Python follows rules similar to mathematics:
   1. Parentheses
   2. Exponentiation **
   3. Multiplication, Division, Modulus
   4. Addition, Subtraction

8. Type conversion
   int(), float(), complex(), str(), bool()

9. Built-in numeric functions
   abs(), round(), divmod(), pow()

10. Precision and rounding in float
   Floating-point numbers may show tiny representation errors.

11. Practice problems
   - digit sum
   - reverse a number
   - prime numbers
   - GCD and LCM
'''

# ==========================
# 1. Integer type (int)
# ==========================
int_a = 10
int_b = -25
int_c = 0
int_large = 9876543210123456789

print("int_a =", int_a)
print("int_b =", int_b)
print("int_c =", int_c)
print("int_large =", int_large)
print("Type of int_a:", type(int_a))

# Integer arithmetic
int_sum = int_a + int_b
int_diff = int_a - int_b
int_mul = int_a * int_b
int_div_float = int_a / 3
int_div_floor = int_a // 3
int_mod = int_a % 3
int_pow = int_a ** 3

print("int_sum =", int_sum)
print("int_diff =", int_diff)
print("int_mul =", int_mul)
print("int_div_float =", int_div_float)
print("int_div_floor =", int_div_floor)
print("int_mod =", int_mod)
print("int_pow =", int_pow)

# Example: large integer
large_int_a = 12345678901234567890
large_int_b = 98765432109876543210
large_int_sum = large_int_a + large_int_b
print("large_int_sum =", large_int_sum)

# ==========================
# 2. Negative integers
# ==========================
neg_int_a = -15
neg_int_b = -7
neg_int_sum = neg_int_a + neg_int_b
neg_int_mul = neg_int_a * neg_int_b
print("neg_int_sum =", neg_int_sum)
print("neg_int_mul =", neg_int_mul)

# ==========================
# 3. Division operators in int
# ==========================
int_div_1 = 17 / 5      # normal division -> float
int_div_2 = 17 // 5     # floor division -> int
int_div_3 = 17 % 5      # remainder
print("17 / 5 =", int_div_1)
print("17 // 5 =", int_div_2)
print("17 % 5 =", int_div_3)

# Negative division example
neg_div_a = -17 / 5
neg_div_b = -17 // 5
neg_div_c = -17 % 5
print("-17 / 5 =", neg_div_a)
print("-17 // 5 =", neg_div_b)
print("-17 % 5 =", neg_div_c)

# ==========================
# 4. Operator precedence
# ==========================
precedence_a = 10 + 5 * 3
precedence_b = (10 + 5) * 3
precedence_c = 10 ** 2 + 3 * 4
precedence_d = (10 + 5) ** 2

print("10 + 5 * 3 =", precedence_a)
print("(10 + 5) * 3 =", precedence_b)
print("10 ** 2 + 3 * 4 =", precedence_c)
print("(10 + 5) ** 2 =", precedence_d)

# Rule: multiplication and division are done before addition and subtraction.
# Exponentiation has higher priority than multiplication/division.

# ==========================
# 5. Type conversion
# ==========================
int_to_float = float(25)
float_to_int = int(25.9)
int_to_complex = complex(4)
str_to_int = int("123")
str_to_float = float("12.5")
float_to_str = str(45.67)

print("float(25) =", int_to_float)
print("int(25.9) =", float_to_int)
print("complex(4) =", int_to_complex)
print("int(\"123\") =", str_to_int)
print("float(\"12.5\") =", str_to_float)
print("str(45.67) =", float_to_str)

# Important note:
# int(25.9) does not round; it truncates toward zero.
# float("abc") raises ValueError.
# int("abc") raises ValueError.

# ==========================
# 6. Float type (float)
# ==========================
float_a = 3.14
float_b = 2.5
float_c = -7.8
float_d = 0.0

print("float_a =", float_a)
print("float_b =", float_b)
print("float_c =", float_c)
print("Type of float_a:", type(float_a))

float_add = float_a + float_b
float_sub = float_a - float_b
float_mul = float_a * float_b
float_div = float_a / float_b
float_pow = float_a ** 2

print("float_add =", float_add)
print("float_sub =", float_sub)
print("float_mul =", float_mul)
print("float_div =", float_div)
print("float_pow =", float_pow)

# Examples with division
float_div_1 = 7 / 3
float_div_2 = 10 / 4
print("7 / 3 =", float_div_1)
print("10 / 4 =", float_div_2)

# ==========================
# 7. Floating-point precision problem
# ==========================
float_precision_a = 0.1 + 0.2
float_precision_b = 0.3 - 0.1
print("0.1 + 0.2 =", float_precision_a)
print("0.3 - 0.1 =", float_precision_b)

# Explanation:
# Due to binary floating-point representation, some decimal values cannot be
# represented exactly.
# This is normal in Python and many other programming languages.

# Using round() to reduce display issues
float_round_a = round(0.1 + 0.2, 2)
float_round_b = round(2.675, 2)
print("round(0.1 + 0.2, 2) =", float_round_a)
print("round(2.675, 2) =", float_round_b)

# ==========================
# 8. abs(), round(), divmod(), pow()
# ==========================

# abs() = absolute value
abs_int_a = abs(-20)
abs_float_a = abs(-12.5)
print("abs(-20) =", abs_int_a)
print("abs(-12.5) =", abs_float_a)

# round() = round to a given number of decimal places
round_float_a = round(15.678, 2)
round_float_b = round(15.678, 1)
print("round(15.678, 2) =", round_float_a)
print("round(15.678, 1) =", round_float_b)

# divmod() = returns (quotient, remainder)
divmod_a = divmod(17, 5)
divmod_b = divmod(-17, 5)
print("divmod(17, 5) =", divmod_a)
print("divmod(-17, 5) =", divmod_b)

# pow() = power function
pow_int_a = pow(2, 5)
pow_int_b = pow(3, 3)
pow_float_a = pow(2, 0.5)
print("pow(2, 5) =", pow_int_a)
print("pow(3, 3) =", pow_int_b)
print("pow(2, 0.5) =", pow_float_a)

# ==========================
# 9. Complex numbers
# ==========================
complex_a = 3 + 4j
complex_b = 2 - 1j

print("complex_a =", complex_a)
print("Type of complex_a:", type(complex_a))

complex_add = complex_a + complex_b
complex_sub = complex_a - complex_b
complex_mul = complex_a * complex_b
complex_div = complex_a / complex_b

print("complex_a + complex_b =", complex_add)
print("complex_a - complex_b =", complex_sub)
print("complex_a * complex_b =", complex_mul)
print("complex_a / complex_b =", complex_div)

# Access real and imaginary parts
complex_real = complex_a.real
complex_imag = complex_a.imag
print("complex_a.real =", complex_real)
print("complex_a.imag =", complex_imag)

# abs() for complex gives magnitude
complex_abs = abs(complex_a)
print("abs(3 + 4j) =", complex_abs)

# Note:
# In Python, complex numbers can be added, multiplied, etc., with other numbers.
# But direct comparison with ints/floats is not commonly used.

# ==========================
# 10. bool as numeric value
# ==========================
bool_a = True
bool_b = False
bool_int_a = int(True)
bool_int_b = int(False)
print("bool_a =", bool_a)
print("int(True) =", bool_int_a)
print("int(False) =", bool_int_b)

# In Python, True = 1 and False = 0.

# ==========================
# 11. Practical examples and exercises
# ==========================

# Example 1: Sum of digits
number_digit_sum = 456
sum_of_digits = sum(int(digit) for digit in str(number_digit_sum))
print("sum_of_digits for 456 =", sum_of_digits)

# Example 2: Reverse a number
number_reverse = 12345
reverse_number = int(str(number_reverse)[::-1])
print("reverse_number of 12345 =", reverse_number)

# Example 3: Check if a number is prime
prime_test_number = 29
prime_is_prime = True
if prime_test_number < 2:
    prime_is_prime = False
else:
    for prime_factor in range(2, int(prime_test_number ** 0.5) + 1):
        if prime_test_number % prime_factor == 0:
            prime_is_prime = False
            break
print("Is 29 prime?", prime_is_prime)

# Example 4: GCD (Greatest Common Divisor)
import math

gcd_num_a = 48
gcd_num_b = 18
gcd_value = math.gcd(gcd_num_a, gcd_num_b)
print("GCD of 48 and 18 =", gcd_value)

# Example 5: LCM (Least Common Multiple)
lcm_num_a = 48
lcm_num_b = 18
lcm_value = abs(lcm_num_a * lcm_num_b) // math.gcd(lcm_num_a, lcm_num_b)
print("LCM of 48 and 18 =", lcm_value)

# ==========================
# 12. Key points summary
# ==========================
print("""
Summary:
- int is for integers.
- float is for decimal numbers.
- complex is for real + imaginary numbers.
- / gives float, // gives floor division, % gives remainder.
- Python follows operator precedence.
- Some float values are not exact due to binary representation.
- abs(), round(), divmod(), pow() are important numeric built-ins.
- Type conversion is done by int(), float(), complex(), and str().
- Python supports large integers exactly.
""")

# End of numeric notes

# ======================================================
# Additional important numeric concepts (append section)
# ======================================================

# 13. Numeric literals in Python
# Python supports different numeral formats.

int_decimal_a = 123
int_binary_a = 0b1010      # binary -> 10
int_octal_a = 0o12         # octal -> 10
int_hexadecimal_a = 0xA    # hexadecimal -> 10

print("int_decimal_a =", int_decimal_a)
print("int_binary_a =", int_binary_a)
print("int_octal_a =", int_octal_a)
print("int_hexadecimal_a =", int_hexadecimal_a)

# 14. Scientific notation / exponent form
scientific_num_a = 1.5e3
scientific_num_b = 2.5e-2
print("scientific_num_a =", scientific_num_a)
print("scientific_num_b =", scientific_num_b)

# 15. Comparing numeric values
int_cmp_a = 10
int_cmp_b = 20
int_cmp_c = 10

print("int_cmp_a == int_cmp_c:", int_cmp_a == int_cmp_c)
print("int_cmp_a < int_cmp_b:", int_cmp_a < int_cmp_b)
print("int_cmp_a > int_cmp_b:", int_cmp_a > int_cmp_b)
print("int_cmp_a <= int_cmp_c:", int_cmp_a <= int_cmp_c)
print("int_cmp_a != int_cmp_b:", int_cmp_a != int_cmp_b)

# Chained comparisons
print("5 < 10 < 15:", 5 < 10 < 15)
print("10 <= 10 <= 12:", 10 <= 10 <= 12)

# 16. Modulo and divisibility
mod_num_a = 25
mod_num_b = 4
mod_result = mod_num_a % mod_num_b
print("25 % 4 =", mod_result)

# A number is divisible by 2 if remainder is 0.
print("Is 18 divisible by 2?", 18 % 2 == 0)
print("Is 19 divisible by 2?", 19 % 2 == 0)

# 17. Floor division vs truncation
floor_div_a = 9 // 2
trunc_div_a = int(9 / 2)
print("9 // 2 =", floor_div_a)
print("int(9 / 2) =", trunc_div_a)

# 18. Negative values and absolute value
neg_abs_a = -45
neg_abs_b = abs(neg_abs_a)
print("abs(-45) =", neg_abs_b)

# 19. Special float values
import math

nan_num_a = float('nan')
inf_num_a = float('inf')
neg_inf_num_a = float('-inf')
print("nan_num_a =", nan_num_a)
print("inf_num_a =", inf_num_a)
print("neg_inf_num_a =", neg_inf_num_a)
print("math.isfinite(nan_num_a) =", math.isfinite(nan_num_a))
print("math.isfinite(inf_num_a) =", math.isfinite(inf_num_a))

# 20. Checking numeric type
is_int_a = isinstance(10, int)
is_float_a = isinstance(10.5, float)
is_complex_a = isinstance(3 + 4j, complex)
print("isinstance(10, int) =", is_int_a)
print("isinstance(10.5, float) =", is_float_a)
print("isinstance(3 + 4j, complex) =", is_complex_a)

# 21. Common math functions from math module
math_sqrt_a = math.sqrt(25)
math_floor_a = math.floor(4.9)
math_ceil_a = math.ceil(4.1)
math_factorial_a = math.factorial(5)
print("math.sqrt(25) =", math_sqrt_a)
print("math.floor(4.9) =", math_floor_a)
print("math.ceil(4.1) =", math_ceil_a)
print("math.factorial(5) =", math_factorial_a)

# 22. Decimal precision and rounding practice
round_num_a = round(2.675, 2)
round_num_b = round(3.14159, 3)
print("round(2.675, 2) =", round_num_a)
print("round(3.14159, 3) =", round_num_b)

# 23. Complex number formulas
complex_real_a = 3 + 4j
complex_mag_a = abs(complex_real_a)
complex_conjugate_a = complex_real_a.conjugate()
print("abs(3 + 4j) =", complex_mag_a)
print("(3 + 4j).conjugate() =", complex_conjugate_a)

# 24. Type conversion notes
# int() removes decimal part: int(7.9) -> 7
# float() converts integer values to decimals: float(7) -> 7.0
# complex() can accept real values: complex(7) -> (7+0j)
# str() converts to string; int("7") converts to integer

# 25. Short exam revision checklist
# - int, float, complex are numeric types.
# - / gives float, // gives floor division, % gives remainder.
# - Python follows precedence rules.
# - float values may have representation precision issues.
# - abs(), round(), divmod(), pow() are very important built-ins.
# - math.gcd(), math.factorial(), math.sqrt() are useful numeric tools.
# - bool is technically a subclass of int in Python.
# - Complex numbers have real and imag parts.
# - Different numeric literal forms: binary, octal, hexadecimal, scientific notation.

print("\nNumeric Data Types - complete revision notes ended successfully.")

