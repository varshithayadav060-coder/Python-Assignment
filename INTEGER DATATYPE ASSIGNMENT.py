INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================


# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")

product = 1
for i in range(1, 11):
    product = product * i
print("Product =", product)
Question 1: Calculate the product of first 10 natural numbers Product = 3628800



# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")

remainder = 156 % 7
print("Remainder =", remainder)
Question 2: Find the remainder when 156 is divided by 7 Remainder = 2


# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")

number = 25
square = number * number
print("Square =", square)
Question 3: Calculate the square of 25 Square = 625


# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")

number = 125
cube_root = 5
print("Cube root =", cube_root)
Question 4: Find the cube root of 125 Cube root = 5


# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")

number = 12345
total = 0

while number > 0:
    digit = number % 10
    total = total + digit
    number = number // 10

print("Sum of digits =", total)
Question 5: Calculate the sum of digits in number 12345 Sum of digits = 15


# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")

number = 97
count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count = count + 1

if count == 2:
    print("97 is a prime number")
else:
    print("97 is not a prime number")
Question 6: Check if 97 is a prime number 97 is a prime number


# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")

number = 8
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial =", factorial)
Question 7: Find the factorial of 8 Factorial = 40320


# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")

a = 15
b = 23
c = 31
d = 42
e = 56

total = a + b + c + d + e
average = total / 5

print("Average =", average)
Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56 Average = 33.4


# Question 9: Find the GCD of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")

a = 48
b = 36

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print("GCD =", a)
Question 9: Find the greatest common divisor (GCD) of 48 and 36 GCD = 12


# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")

total = 0

for i in range(1, 21):
    odd_number = 2 * i - 1
    total = total + odd_number

print("Sum of first 20 odd numbers =", total)
Question 10: Calculate the sum of first 20 odd numbers Sum of first 20 odd numbers = 400
