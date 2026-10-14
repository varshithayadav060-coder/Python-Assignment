# LIST DATATYPE ASSIGNMENT - 50 QUESTIONS
# ======================================

# SOLVED EXAMPLE
# --------------
# Question: Find the maximum and minimum values in a list
print("SOLVED EXAMPLE:")
print("Find the maximum and minimum values in a list")
numbers = [23, 45, 12, 67, 34, 89, 56]
max_val = max(numbers)
min_val = min(numbers)
print(f"List: {numbers}")
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a list of first 10 square numbers
print("Question 1: Create a list of first 10 square numbers")

squares = []

for i in range(1, 11):
    squares.append(i ** 2)

print(squares)


# Question 2: Find the sum of all even numbers
print("\nQuestion 2: Find the sum of all even numbers")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum = even_sum + num

print(even_sum)


# Question 3: Remove duplicates from a list
print("\nQuestion 3: Remove duplicates from a list")

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)


# Question 4: Sort the list in descending order
print("\nQuestion 4: Sort the list in descending order")

numbers = [64, 34, 25, 12, 22, 11, 90]
numbers.sort(reverse=True)

print(numbers)


# Question 5: Find the average of numbers
print("\nQuestion 5: Find the average of numbers")

numbers = [15, 23, 31, 42, 56, 78, 91]
average = sum(numbers) / len(numbers)

print(average)


# Question 6: Create a list of first 15 Fibonacci numbers
print("\nQuestion 6: Create a list of first 15 Fibonacci numbers")

fibonacci = [0, 1]

while len(fibonacci) < 15:
    next_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_number)

print(fibonacci)


# Question 7: Find the second largest number
print("\nQuestion 7: Find the second largest number")

numbers = [45, 67, 23, 89, 12, 34, 78]
numbers.sort()

print(numbers[-2])


# Question 8: Reverse a list
print("\nQuestion 8: Reverse a list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()

print(numbers)


# Question 9: Count how many times 5 appears
print("\nQuestion 9: Count how many times 5 appears")

numbers = [1, 5, 2, 5, 3, 5, 4, 5, 6]

print(numbers.count(5))


# Question 10: Create a list of prime numbers between 1 and 50
print("\nQuestion 10: Create a list of prime numbers between 1 and 50")

primes = []

for num in range(2, 51):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

print(primes)


# Question 11: Flatten a nested list
print("\nQuestion 11: Flatten a nested list")

numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = []

for sublist in numbers:
    for num in sublist:
        flat_list.append(num)

print(flat_list)


# Question 12: Find common elements between two lists
print("\nQuestion 12: Find common elements between two lists")

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []

for num in list1:
    if num in list2:
        common.append(num)

print(common)


# Question 13: Create a list of lists
print("\nQuestion 13: Create a list of lists")

numbers = [[1, 2], [3, 4], [5, 6]]

print(numbers)


# Question 14: Find the sum of each sublist
print("\nQuestion 14: Find the sum of each sublist")

numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sums = []

for sublist in numbers:
    sums.append(sum(sublist))

print(sums)


# Question 15: Transpose a matrix
print("\nQuestion 15: Transpose a matrix")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = []

for i in range(len(matrix[0])):
    row = []

    for j in range(len(matrix)):
        row.append(matrix[j][i])

    transposed.append(row)

print(transposed)


# Question 16: Find the maximum value in each sublist
print("\nQuestion 16: Find the maximum value in each sublist")

numbers = [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
maximums = []

for sublist in numbers:
    maximums.append(max(sublist))

print(maximums)


# Question 17: Create a 3D list
print("\nQuestion 17: Create a 3D list")

numbers = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

print(numbers)


# Question 18: Find the sum of all elements in a 3D list
print("\nQuestion 18: Find the sum of all elements in a 3D list")

numbers = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
total = 0

for group in numbers:
    for sublist in group:
        total = total + sum(sublist)

print(total)


# Question 19: Extract all even numbers from a nested list
print("\nQuestion 19: Extract all even numbers from a nested list")

numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_numbers = []

for sublist in numbers:
    for num in sublist:
        if num % 2 == 0:
            even_numbers.append(num)

print(even_numbers)


# Question 20: Create a list of mixed data types
print("\nQuestion 20: Create a list of mixed data types")

mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]

print(mixed_list)


# Question 21: Find the length of each string
print("\nQuestion 21: Find the length of each string")

words = ["apple", "banana", "cherry", "date"]
lengths = []

for word in words:
    lengths.append(len(word))

print(lengths)


# Question 22: Create a list of tuples
print("\nQuestion 22: Create a list of tuples")

items = [(1, "a"), (2, "b"), (3, "c")]

print(items)


# Question 23: Extract the first element from each tuple
print("\nQuestion 23: Extract the first element from each tuple")

items = [(1, "a"), (2, "b"), (3, "c")]
first_elements = []

for item in items:
    first_elements.append(item[0])

print(first_elements)


# Question 24: Create a list of dictionaries
print("\nQuestion 24: Create a list of dictionaries")

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

print(people)


# Question 25: Extract all name values
print("\nQuestion 25: Extract all name values")

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

names = []

for person in people:
    names.append(person["name"])

print(names)


# Question 26: Find the person with maximum age
print("\nQuestion 26: Find the person with maximum age")

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

oldest_person = max(people, key=lambda person: person["age"])

print(oldest_person)


# Question 27: Create a 4D list
print("\nQuestion 27: Create a 4D list")

numbers = [
    [[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
    [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]
]

print(numbers)


# Question 28: Find the maximum value in a 4D list
print("\nQuestion 28: Find the maximum value in a 4D list")

numbers = [
    [[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
    [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]
]

all_numbers = []

for group in numbers:
    for sublist in group:
        for row in sublist:
            all_numbers.extend(row)

print(max(all_numbers))


# Question 29: Create a list of sets
print("\nQuestion 29: Create a list of sets")

sets_list = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]

print(sets_list)


# Question 30: Find the union of all sets
print("\nQuestion 30: Find the union of all sets")

sets_list = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
union_set = set()

for item in sets_list:
    union_set = union_set.union(item)

print(union_set)


# Question 31: Create a list of complex numbers
print("\nQuestion 31: Create a list of complex numbers")

numbers = [1 + 2j, 3 + 4j, 5 + 6j]

print(numbers)


# Question 32: Find the magnitude of each complex number
print("\nQuestion 32: Find the magnitude of each complex number")

numbers = [1 + 2j, 3 + 4j, 5 + 6j]
magnitudes = []

for num in numbers:
    magnitudes.append(abs(num))

print(magnitudes)


# Question 33: Create a nested list with different levels
print("\nQuestion 33: Create a nested list with different levels")

numbers = [1, [2, 3], [4, [5, 6]], 7]

print(numbers)


# Question 34: Count the depth of nesting
print("\nQuestion 34: Count the depth of nesting")

numbers = [1, [2, 3], [4, [5, 6]], 7]

def find_depth(items):
    depth = 1

    for item in items:
        if isinstance(item, list):
            depth = max(depth, 1 + find_depth(item))

    return depth

print(find_depth(numbers))


# Question 35: Create a list of functions
print("\nQuestion 35: Create a list of functions")

functions = [len, str, int, float]

print(functions)


# Question 36: Apply each function to the string "123"
print("\nQuestion 36: Apply each function to the string '123'")

functions = [len, str, int, float]
value = "123"
results = []

for function in functions:
    results.append(function(value))

print(results)


# Question 37: Create a list of lambda functions
print("\nQuestion 37: Create a list of lambda functions")

functions = [
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x + 1
]

print(functions)


# Question 38: Apply each lambda function to 5
print("\nQuestion 38: Apply each lambda function to 5")

functions = [
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x + 1
]

results = []

for function in functions:
    results.append(function(5))

print(results)


# Question 39: Create a list of classes
print("\nQuestion 39: Create a list of classes")

classes = [list, dict, set, tuple]

print(classes)


# Question 40: Create instances of each class
print("\nQuestion 40: Create instances of each class")

classes = [list, dict, set, tuple]
instances = []

for class_type in classes:
    instances.append(class_type())

print(instances)


# Question 41: Create a list of None values
print("\nQuestion 41: Create a list of None values")

values = [None, None, None, None]

print(values)


# Question 42: Replace all None values with 0
print("\nQuestion 42: Replace all None values with 0")

values = [None, None, None, None]
updated_values = []

for value in values:
    if value is None:
        updated_values.append(0)
    else:
        updated_values.append(value)

print(updated_values)


# Question 43: Create a list of boolean values
print("\nQuestion 43: Create a list of boolean values")

values = [True, False, True, False]

print(values)


# Question 44: Count True values
print("\nQuestion 44: Count True values")

values = [True, False, True, False]
true_count = values.count(True)

print(true_count)


# Question 45: Create a list of ranges
print("\nQuestion 45: Create a list of ranges")

ranges = [range(3), range(5), range(2)]

print(ranges)


# Question 46: Convert each range to a list
print("\nQuestion 46: Convert each range to a list")

ranges = [range(3), range(5), range(2)]
range_lists = []

for item in ranges:
    range_lists.append(list(item))

print(range_lists)


# Question 47: Create a list of generators
print("\nQuestion 47: Create a list of generators")

generators = [
    (x for x in range(3)),
    (x for x in range(5))
]

print(generators)


# Question 48: Convert each generator to a list
print("\nQuestion 48: Convert each generator to a list")

generators = [
    (x for x in range(3)),
    (x for x in range(5))
]

generator_lists = []

for generator in generators:
    generator_lists.append(list(generator))

print(generator_lists)


# Question 49: Create a list of iterators
print("\nQuestion 49: Create a list of iterators")

iterators = [
    iter([1, 2, 3]),
    iter([4, 5, 6])
]

print(iterators)


# Question 50: Extract all elements from each iterator
print("\nQuestion 50: Extract all elements from each iterator")

iterators = [
    iter([1, 2, 3]),
    iter([4, 5, 6])
]

iterator_lists = []

for iterator in iterators:
    iterator_lists.append(list(iterator))

print(iterator_lists)
