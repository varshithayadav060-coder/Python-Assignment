# SET DATATYPE ASSIGNMENT
# ======================

# SOLVED EXAMPLE
# --------------
# Question: Find the union of two sets
print("SOLVED EXAMPLE:")
print("Find the union of two sets")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {union_set}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a set of first 10 natural numbers
print("Question 1: Create a set of first 10 natural numbers")
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(numbers)
Question 1: Create a set of first 10 natural numbers
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# Question 2: Add element 11 to set
print("\nQuestion 2: Add element 11 to set {1, 2, 3, 4, 5}")
numbers = {1, 2, 3, 4, 5}
numbers.add(11)
print(numbers)
Question 2: Add element 11 to set {1, 2, 3, 4, 5}
{1, 2, 3, 4, 5, 11}

# Question 3: Remove element 3 from set
print("\nQuestion 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}")
numbers = {1, 2, 3, 4, 5, 6}
numbers.remove(3)
print(numbers)
Question 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}
{1, 2, 4, 5, 6}


# Question 4: Find the intersection of two sets
print("\nQuestion 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))
Question 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
{4, 5}

# Question 5: Find the difference between two sets
print("\nQuestion 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.difference(set2))
Question 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
{1, 2, 3}

# Question 6: Check if 5 is in the set
print("\nQuestion 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}")
numbers = {1, 2, 3, 4, 6, 7, 8}
print(5 in numbers)
Question 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}
False

# Question 7: Find the length of a set
print("\nQuestion 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}")
letters = {'a', 'b', 'c', 'd', 'e'}
print(len(letters))
Question 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}
5

# Question 8: Create a set of vowels from string
print("\nQuestion 8: Create a set of vowels from string 'hello world'")
text = "hello world"
vowels = {char for char in text if char in "aeiou"}
print(vowels)
Question 8: Create a set of vowels from string 'hello world'
{'e', 'o'}

# Question 9: Remove duplicates from a list using set
print("\nQuestion 9: Remove duplicates from list using set")
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_numbers = set(numbers)
print(unique_numbers)
Question 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set
{1, 2, 3, 4, 5, 6, 7}

# Question 10: Check if one set is a subset of another
print("\nQuestion 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}")
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5, 6}
print(set1.issubset(set2))
Question 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}
True
