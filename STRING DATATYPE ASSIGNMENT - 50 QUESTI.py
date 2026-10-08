# STRING DATATYPE ASSIGNMENT - 50 QUESTIONS
# ========================================

# SOLVED EXAMPLE
# --------------
# Question: Count vowels in the string "Hello World"
print("SOLVED EXAMPLE:")
print("Count vowels in the string 'Hello World'")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"String: {text}")
print(f"Number of vowels: {count}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================
### Question 1: Reverse the string "Python Programming"

text = "Python Programming"
print("Reversed string =", text[::-1])

### Question 2: Check if "racecar" is a palindrome

text = "racecar"
print("Is palindrome =", text == text[::-1])


### Question 3: Count the number of words in "Python is a great programming language"

text = "Python is a great programming language"
print("Number of words =", len(text.split()))

### Question 4: Convert "hello world" to title case

text = "hello world"
print("Title case =", text.title())


### Question 5: Find the length of string "Data Science"

text = "Data Science"
print("Length =", len(text))


### Question 6: Replace all spaces with underscores in "Machine Learning"

text = "Machine Learning"
print("Result =", text.replace(" ", "_"))


### Question 7: Check if "python" is in "Python Programming Language"

text = "Python Programming Language"
print("Is python present =", "python" in text)

### Question 8: Extract the first 5 characters from "Artificial Intelligence"

text = "Artificial Intelligence"
print("First 5 characters =", text[:5])

### Question 9: Convert "UPPERCASE" to lowercase

text = "UPPERCASE"
print("Lowercase =", text.lower())

### Question 10: Remove all vowels from "Computer Science"

text = "Computer Science"
vowels = "aeiouAEIOU"
result = ""

for char in text:
    if char not in vowels:
        result += char

print("Without vowels =", result)


### Question 11: Find the most frequent character in "mississippi"

text = "mississippi"
most_common = max(set(text), key=text.count)
print("Most frequent character =", most_common)


### Question 12: Check if two strings are anagrams: "listen" and "silent"

text1 = "listen"
text2 = "silent"
print("Are anagrams =", sorted(text1) == sorted(text2))

### Question 13: Capitalize the first letter of each word in "python programming language"

text = "python programming language"
print("Result =", text.title())

### Question 14: Count consonants in "Hello World"

text = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char.isalpha() and char not in vowels:
        count += 1

print("Number of consonants =", count)

### Question 15: Find the longest word in "Python is a programming language"

text = "Python is a programming language"
longest = max(text.split(), key=len)
print("Longest word =", longest)

### Question 16: Remove all punctuation from "Hello, World! How are you?"

import string

text = "Hello, World! How are you?"
result = ""

for char in text:
    if char not in string.punctuation:
        result += char

print("Without punctuation =", result)

### Question 17: Check if a string starts with "Python"

text = "Python Programming"
print("Starts with Python =", text.startswith("Python"))

### Question 18: Find the index of the first occurrence of 'o' in "Hello World"

text = "Hello World"
print("Index of o =", text.find("o"))

### Question 19: Split the string "apple,banana,orange" by comma

text = "apple,banana,orange"
print("Split string =", text.split(","))

### Question 20: Join the list ['Python', 'is', 'awesome'] with spaces

words = ["Python", "is", "awesome"]
print("Joined string =", " ".join(words))

### Question 21: Check if the string contains only digits: "12345"

text = "12345"
print("Contains only digits =", text.isdigit())

### Question 22: Check if the string contains only letters: "HelloWorld"

text = "HelloWorld"
print("Contains only letters =", text.isalpha())

### Question 23: Convert "hello world" to "hElLo WoRlD" (alternating case)

text = "hello world"
result = ""

for i, char in enumerate(text):
    if char.isalpha():
        if i % 2 == 0:
            result += char.lower()
        else:
            result += char.upper()
    else:
        result += char

print("Alternating case =", result)

### Question 24: Find all positions of 'a' in "banana"

text = "banana"
positions = []

for i, char in enumerate(text):
    if char == "a":
        positions.append(i)

print("Positions of a =", positions)

### Question 25: Remove leading and trailing whitespace from "  Hello World  "

text = "  Hello World  "
print("Trimmed string =", text.strip())


### Question 26: Check if the string ends with "ing": "programming"

text = "programming"
print("Ends with ing =", text.endswith("ing"))


### Question 27: Replace the first occurrence of 'o' with '0' in "Hello World"

text = "Hello World"
print("Result =", text.replace("o", "0", 1))

### Question 28: Find the shortest word in "Python is a programming language"

text = "Python is a programming language"
shortest = min(text.split(), key=len)
print("Shortest word =", shortest)

### Question 29: Count words that start with 'p' in "Python programming is powerful"

text = "Python programming is powerful"
count = sum(1 for word in text.split() if word.lower().startswith("p"))
print("Number of words =", count)

### Question 30: Reverse the words in "Hello World Python"

text = "Hello World Python"
result = " ".join(text.split()[::-1])
print("Reversed words =", result)


### Question 31: Check if the string is a valid email format: "[user@example.com](mailto:user@example.com)"

email = "user@example.com"
valid = (
    email.count("@") == 1
    and " " not in email
    and "." in email.split("@")[1]
    and email.split("@")[0] != ""
    and email.split("@")[1].split(".")[0] != ""
    and email.split("@")[1].split(".")[-1] != ""
)

print("Valid email format =", valid)

### Question 32: Extract the domain from "https://www.example.com/path"

url = "https://www.example.com/path"
domain = url.split("//")[1].split("/")[0]
print("Domain =", domain)

### Question 33: Count lines in a multi-line string

text = """Hello World
Python Programming
Data Science"""

print("Number of lines =", len(text.splitlines()))

### Question 34: Find common characters between "hello" and "world"

text1 = "hello"
text2 = "world"

common = sorted(set(text1) & set(text2))
print("Common characters =", common)

### Question 35: Check if the string is a valid phone number: "+1-555-123-4567"

phone = "+1-555-123-4567"
valid = phone.startswith("+") and all(
    part.isdigit() for part in phone[1:].split("-")
) and len(phone[1:].replace("-", "")) == 11

print("Valid phone number format =", valid)


### Question 36: Extract numbers from "abc123def456ghi789"

text = "abc123def456ghi789"
numbers = ""

for char in text:
    if char.isdigit():
        numbers += char

print("Extracted numbers =", numbers)


### Question 37: Convert "snake_case" to "camelCase"

text = "snake_case"
words = text.split("_")
result = words[0] + "".join(word.title() for word in words[1:])
print("Camel case =", result)

### Question 38: Check if the string is a valid palindrome ignoring case: "A man a plan a canal Panama"

text = "A man a plan a canal Panama"
cleaned = "".join(char.lower() for char in text if char.isalnum())

print("Is palindrome =", cleaned == cleaned[::-1])

### Question 39: Find the most common word in "the quick brown fox jumps over the lazy dog"

text = "the quick brown fox jumps over the lazy dog"
words = text.split()
most_common = max(set(words), key=words.count)

print("Most common word =", most_common)

### Question 40: Generate an acronym from "National Aeronautics and Space Administration"

text = "National Aeronautics and Space Administration"
acronym = "".join(word[0].upper() for word in text.split())

print("Acronym =", acronym)

### Question 41: Check if the string contains balanced parentheses: "((()))"

text = "((()))"
count = 0
balanced = True

for char in text:
    if char == "(":
        count += 1
    elif char == ")":
        count -= 1

    if count < 0:
        balanced = False
        break

balanced = balanced and count == 0
print("Balanced parentheses =", balanced)

### Question 42: Convert "hello world" to Morse code

text = "hello world"

morse = {
    "h": "....", "e": ".", "l": ".-..", "o": "---",
    "w": ".--", "r": ".-.", "d": "-.."
}

result = " ".join(
    "/"
    if char == " "
    else morse[char]
    for char in text.lower()
)

print("Morse code =", result) 


### Question 43: Find the longest common substring between "programming" and "grammar"

text1 = "programming"
text2 = "grammar"
longest = ""

for i in range(len(text1)):
    for j in range(i + 1, len(text1) + 1):
        substring = text1[i:j]
        if substring in text2 and len(substring) > len(longest):
            longest = substring

print("Longest common substring =", longest)


### Question 44: Check if the string is a valid URL: "https://www.google.com"

url = "https://www.google.com"
valid = url.startswith(("http://", "https://")) and "." in url.split("//")[1]

print("Valid URL format =", valid)


### Question 45: Extract all words with length greater than 5 from "Python programming is amazing and powerful"

text = "Python programming is amazing and powerful"
words = [word for word in text.split() if len(word) > 5]

print("Words longer than 5 characters =", words)

### Question 46: Convert "hello world" to Pig Latin

text = "hello world"
result = []

for word in text.split():
    result.append(word[1:] + word[0] + "ay")

print("Pig Latin =", " ".join(result))

### Question 47: Check if the string is a valid IPv4 address: "192.168.1.1"

ip = "192.168.1.1"
parts = ip.split(".")

valid = (
    len(parts) == 4
    and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)
)

print("Valid IPv4 address =", valid)

### Question 48: Find all substrings of "abc"

text = "abc"
substrings = []

for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        substrings.append(text[i:j])

print("All substrings =", substrings)


### Question 49: Convert "hello world" to ROT13 encoding

text = "hello world"
result = ""

for char in text:
    if "a" <= char <= "z":
        result += chr((ord(char) - ord("a") + 13) % 26 + ord("a"))
    elif "A" <= char <= "Z":
        result += chr((ord(char) - ord("A") + 13) % 26 + ord("A"))
    else:
        result += char

print("ROT13 =", result)


### Question 50: Check if the string is a valid credit card number: "4532015112830366"

card = "4532015112830366"
digits = [int(char) for char in card]

for i in range(len(digits) - 2, -1, -2):
    digits[i] *= 2
    if digits[i] > 9:
        digits[i] -= 9

valid = card.isdigit() and sum(digits) % 10 == 0
print("Valid credit card number =", valid)






