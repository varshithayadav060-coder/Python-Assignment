# DICTIONARY DATATYPE ASSIGNMENT - 50 QUESTIONS
# ============================================

# SOLVED EXAMPLE
# --------------
# Question: Find the key with maximum value in a dictionary
from tokenize import Double
from typing import List


print("SOLVED EXAMPLE:")
print("Find the key with maximum value in a dictionary")
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95, 'Eve': 88}
max_key = max(scores, key=scores.get)
max_value = scores[max_key]
print(f"Dictionary: {scores}")
print(f"Key with maximum value: {max_key}")
print(f"Maximum value: {max_value}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a dictionary of student names and their ages
print("Question 1: Create a dictionary of student names and their ages")
students = {"Alice": 20, "Bob": 21, "John": 22}
print(students)
output: {'Alice': 20, 'Bob': 21, 'John': 22}

# Question 2: Add a new key-value pair
print("\nQuestion 2: Add a new key-value pair")
data = {'a': 1, 'b': 2, 'c': 3}
data['d'] = 4
print(data)
output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Question 3: Get all keys
print("\nQuestion 3: Get all keys")
data = {'name': 'John', 'age': 25, 'city': 'New York'}
print(list(data.keys())) 
output: ['name', 'age', 'city']

# Question 4: Get all values
print("\nQuestion 4: Get all values")
data = {'python': 3, 'java': 2, 'c++': 1}
print(list(data.values()))
output: [3, 2, 1]

# Question 5: Check if key 'age' exists
print("\nQuestion 5: Check if key 'age' exists")
data = {'name': 'Alice', 'age': 30, 'city': 'London'}
print('age' in data)
output: True

# Question 6: Remove key 'temp'
print("\nQuestion 6: Remove key 'temp'")
data = {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
data.pop('temp')
print(data)
output: {'a': 1, 'b': 2, 'c': 4}

# Question 7: Sum of all values
print("\nQuestion 7: Find the sum of all values")
marks = {'math': 85, 'science': 92, 'english': 78}
print(sum(marks.values()))
output: 255

# Question 8: Dictionary with squares of numbers 1 to 5
print("\nQuestion 8: Dictionary with squares")
squares = {x: x**2 for x in range(1, 6)}
print(squares)
output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Question 9: Count frequency of each character in "hello"
print("\nQuestion 9: Count character frequency")
s = "hello"
frequency = {}
for char in s:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)
output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Question 10: Merge two dictionaries
print("\nQuestion 10: Merge two dictionaries")
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
merged = {**d1, **d2}
print(merged)
output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Question 11: Create a nested dictionary
print("\nQuestion 11: Create a nested dictionary")
person = {'person': {'name': 'Alice', 'age': 25}}
print(person) 
output: {'person': {'name': 'Alice', 'age': 25}}


# Question 12: Access nested value 'name'
print("\nQuestion 12: Access nested value")
person = {'person': {'name': 'Alice', 'age': 25}}
print(person['person']['name']) 
output: Alice

# Question 13: Dictionary with list values
print("\nQuestion 13: Dictionary with list values")
data = {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
print(data)
output: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}

# Question 14: Add 'orange' to fruits
print("\nQuestion 14: Add orange to fruits")
data = {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
data['fruits'].append('orange')
print(data)
output: {'fruits': ['apple', 'banana', 'orange'], 'colors': ['red', 'blue']}

# Question 15: Dictionary with tuple values
print("\nQuestion 15: Dictionary with tuple values")
data = {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print(data)
output: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}

# Question 16: Extract first coordinate
print("\nQuestion 16: Extract first coordinate")
data = {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print(data['coordinates'][0])
output: 10

# Question 17: Dictionary with set values
print("\nQuestion 17: Dictionary with set values")
data = {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
print(data)
output: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}

# Question 18: Add 'o' to vowels
print("\nQuestion 18: Add o to vowels")
data = {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
data['vowels'].add('o')
print(data)
output: {'vowels': {'a', 'e', 'i', 'o'}, 'consonants': {'b', 'c', 'd'}}

# Question 19: Create a 3-level nested dictionary
print("\nQuestion 19: Create a nested dictionary")
data = {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print(data)
output: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}

# Question 20: Access employee name
print("\nQuestion 20: Access employee name")
data = {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print(data['company']['department']['employee']['name'])
output: John

# Question 21: Dictionary with mixed data types
print("\nQuestion 21: Dictionary with mixed data types")
data = {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print(data)
output: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}

# Question 22: Check data type of each value
print("\nQuestion 22: Check data types")
data = {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
for key, value in data.items():
    print(key, type(value))
output:int <class 'int'>
float <class 'float'>
str <class 'str'>
bool <class 'bool'>

# Question 23: Dictionary with function values
print("\nQuestion 23: Dictionary with function values")
functions = {'len': len, 'str': str, 'int': int}
print(functions)
output: {'len': <built-in function len>, 'str': <class 'str'>, 'int': <class 'int'>}

# Question 24: Apply each function to "123" using dictionary
print("\nQuestion 24: Apply each function to 123")
functions = {'len': len, 'str': str, 'int': int}
print("len =", functions['len']("123"))
print("str =", functions['str']("123"))
print("int =", functions['int']("123"))
output: len = 3
str = 123
int = 123

# Question 25: Dictionary with lambda functions
print("\nQuestion 25: Dictionary with lambda functions")
functions = {'double': lambda x: x*2, 'square': lambda x: x**2}
print(functions)
output: {'double': <function <lambda> at 0x7f8c1c2e1d30>, 'square': <function <lambda> at 0x7f8c1c2e1dc0>}

# Question 26: Apply each lambda function to 5
print("\nQuestion 26: Apply lambda functions to 5")
functions = {'double': lambda x: x*2, 'square': lambda x: x**2}
print("Double =", functions['double'](5))
print("Square =", functions['square'](5))
output: Double = 10
Square = 25


# Question 27: Dictionary with class values
print("\nQuestion 27: Dictionary with class values")
classes = {'list': list, 'dict': dict, 'set': set}
print(classes)
output: {'list': <class 'list'>, 'dict': <class 'dict'>, 'set': <class 'set'>}

# Question 28: Create instances using class dictionary
print("\nQuestion 28: Create instances")
classes = {'list': list, 'dict': dict, 'set': set}
print("List =", classes['list']())
print("Dictionary =", classes['dict']())
print("Set =", classes['set']())
output: List = []
Dictionary = {}
Set = {}

# Question 29: Dictionary with None values
print("\nQuestion 29: Dictionary with None values")
data = {'a': None, 'b': None, 'c': None}
print(data)
output: {'a': None, 'b': None, 'c': None}

# Question 30: Replace None values with 0
print("\nQuestion 30: Replace None with 0")
data = {'a': None, 'b': None, 'c': None}
for key in data:
    if data[key] is None:
        data[key] = 0
print(data)
output: {'a': 0, 'b': 0, 'c': 0}

# Question 31: Dictionary with boolean values
print("\nQuestion 31: Dictionary with boolean values")
data = {'is_active': True, 'is_admin': False}
print(data) 
output: {'is_active': True, 'is_admin': False}

# Question 32: Count True values
print("\nQuestion 32: Count True values")
data = {'is_active': True, 'is_admin': False}
print(sum(data.values()))
output: 1

# Question 33: Dictionary with complex numbers
print("\nQuestion 33: Dictionary with complex numbers")
data = {'z1': 3+4j, 'z2': 1+2j}
print(data)
output: {'z1': (3+4j), 'z2': (1+2j)}

# Question 34: Find magnitude of complex numbers
print("\nQuestion 34: Find magnitude")
data = {'z1': 3+4j, 'z2': 1+2j}
for key, value in data.items():
    print(key, abs(value))
    output: z1 5.0
    output: z2 2.23606797749979
    

# Question 35: Create a 4-level nested dictionary
print("\nQuestion 35: Create a 4-level nested dictionary")
data = {'level1': {'level2': {'level3': {'level4': 'Hello'}}}}
print(data) 
output: {'level1': {'level2': {'level3': {'level4': 'Hello'}}}}

# Question 36: Access deepest value
print("\nQuestion 36: Access deepest value")
data = {'level1': {'level2': {'level3': {'level4': 'Hello'}}}}
print(data['level1']['level2']['level3']['level4'])
output: Hello

# Question 37: Dictionary with range values
print("\nQuestion 37: Dictionary with range values")
data = {'r1': range(3), 'r2': range(5)}
print(data)
output: {'r1': range(0, 3), 'r2': range(0, 5)}

# Question 38: Convert each range to list
print("\nQuestion 38: Convert ranges to lists")
data = {'r1': range(3), 'r2': range(5)}
result = {key: list(value) for key, value in data.items()}
print(result)
output: {'r1': [0, 1, 2], 'r2': [0, 1, 2, 3, 4]}

# Question 39: Dictionary with generator values
print("\nQuestion 39: Dictionary with generator values")
data = {'g1': (x for x in range(3)), 'g2': (x for x in range(2, 5))}
print("Generators created")
output: Generators created

# Question 40: Convert each generator to list
print("\nQuestion 40: Convert generators to lists")
data = {'g1': (x for x in range(3)), 'g2': (x for x in range(2, 5))}
result = {key: list(value) for key, value in data.items()}
print(result)
output: {'g1': [0, 1, 2], 'g2': [2, 3, 4]}

# Question 41: Dictionary with iterator values
print("\nQuestion 41: Dictionary with iterator values")
data = {'i1': iter([1, 2, 3]), 'i2': iter([4, 5, 6])}
print("Iterators created")
output: Iterators created

# Question 42: Extract all elements from each iterator
print("\nQuestion 42: Extract iterator elements")
data = {'i1': iter([1, 2, 3]), 'i2': iter([4, 5, 6])}
result = {key: list(value) for key, value in data.items()}
print(result)
output: {'i1': [1, 2, 3], 'i2': [4, 5, 6]}

# Question 43: Dictionary with nested lists
print("\nQuestion 43: Dictionary with nested lists")
data = {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print(data)
output: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}

# Question 44: Find sum of each nested list
print("\nQuestion 44: Sum of each nested list")
data = {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print("Matrix row sums =", [sum(row) for row in data['matrix']])
print("Vector sum =", sum(data['vector']))
output: Matrix row sums = [3, 7]
        Vector sum = 18

# Question 45: Dictionary with nested dictionaries
print("\nQuestion 45: Nested configuration dictionary")
data = {'config': {'db': {'host': 'localhost', 'port': 5432}}}
print(data)
output: {'config': {'db': {'host': 'localhost', 'port': 5432}}}

# Question 46: Access database port
print("\nQuestion 46: Access database port")
data = {'config': {'db': {'host': 'localhost', 'port': 5432}}}
print(data['config']['db']['port'])
output: 5432

# Question 47: Dictionary with nested tuples
print("\nQuestion 47: Dictionary with nested tuples")
data = {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print(data)
output: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}

# Question 48: Extract first point coordinates
print("\nQuestion 48: Extract first point coordinates")
data = {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print(data['points'][0])
output: (1, 2)

# Question 49: Dictionary with nested sets
print("\nQuestion 49: Dictionary with nested sets")
data = {
    'groups': {frozenset({1, 2, 3}), frozenset({4, 5, 6})},
    'categories': {frozenset({'a', 'b'}), frozenset({'c', 'd'})}
}
print(data)
output: {'groups': {frozenset({1, 2, 3}), frozenset({4, 5, 6})}, 'categories': {frozenset({'a', 'b'}), frozenset({'c', 'd'})}}

# Question 50: Find union of all nested sets
print("\nQuestion 50: Find union of all nested sets")
data = {
    'groups': {frozenset({1, 2, 3}), frozenset({4, 5, 6})},
    'categories': {frozenset({'a', 'b'}), frozenset({'c', 'd'})}
}
groups_union = set.union(*(set(group) for group in data['groups']))
categories_union = set.union(*(set(category) for category in data['categories']))
print("Groups union =", groups_union)
print("Categories union =", categories_union)
output: Groups union = {1, 2, 3, 4, 5, 6}
        Categories union = {'a', 'b', 'c', 'd'}
