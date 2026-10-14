# TUPLE DATATYPE ASSIGNMENT
# ========================

# SOLVED EXAMPLE
# --------------
# Question: Find the sum and product of all elements in a tuple
from ast import Is


print("SOLVED EXAMPLE:")
print("Find the sum and product of all elements in a tuple")
numbers = (2, 4, 6, 8, 10)
sum_tuple = sum(numbers)
product = 1
for num in numbers:
    product *= num
print(f"Tuple: {numbers}")
print(f"Sum: {sum_tuple}")
print(f"Product: {product}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================
# Question 1: Create a tuple of first 10 natural numbers
print("Question 1: Create a tuple of first 10 natural numbers")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Tuple =", numbers)

output
Tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Question 2: Find the length of tuple
print("\nQuestion 2: Find the length of tuple")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Length =", len(numbers))  

output
Length = 10 

# Question 3: Access the 3rd element
print("\nQuestion 3: Access the 3rd element")

letters = ('a', 'b', 'c', 'd', 'e')
print("3rd element =", letters[2]) 

output
3rd element = c


# Question 4: Find the maximum value
print("\nQuestion 4: Find the maximum value")

numbers = (23, 45, 12, 67, 34, 89, 56)
print("Maximum value =", max(numbers)) 

output
Maximum value = 89


# Question 5: Count how many times 5 appears
print("\nQuestion 5: Count how many times 5 appears")

numbers = (1, 5, 2, 5, 3, 5, 4, 5, 6)
print("Count of 5 =", numbers.count(5))

output
Count of 5 = 4


# Question 6: Create a tuple of mixed data types
print("\nQuestion 6: Create a tuple of mixed data types")

mixed_tuple = (10, 3.14, "Python", True)
print("Mixed tuple =", mixed_tuple) 

output
Mixed tuple = (10, 3.14, 'Python', True)


# Question 7: Find the index of 'python'
print("\nQuestion 7: Find the index of element 'python'")

languages = ('java', 'python', 'c++', 'javascript')
print("Index of python =", languages.index('python')) 

output
Index of python = 1


# Question 8: Check if 25 exists in the tuple
print("\nQuestion 8: Check if 25 exists in the tuple")

numbers = (10, 20, 30, 40, 50)
print("Is 25 present =", 25 in numbers)

output
Is 25 present = False


# Question 9: Create a tuple of first 5 even numbers
print("\nQuestion 9: Create a tuple of first 5 even numbers")

even_numbers = (2, 4, 6, 8, 10)
print("Even numbers =", even_numbers)

output
Even numbers = (2, 4, 6, 8, 10)


# Question 10: Find the average of numbers in the tuple
print("\nQuestion 10: Find the average of numbers in the tuple")

numbers = (15, 23, 31, 42, 56, 78)
average = sum(numbers) / len(numbers)
print("Average =", average)

output
Average = 40.833333333333336