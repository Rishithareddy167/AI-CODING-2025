"""
Comparison of Zero-shot and Few-shot Prompts for Counting Vowels in a String

Zero-shot Prompt:
-----------------
"Write a function that counts the number of vowels in a string."

Few-shot Prompt:
----------------
"Write a function that counts the number of vowels in a string.

Example:
>>> count_vowels('hello')
2
>>> count_vowels('AIAC')
3
>>> count_vowels('sky')
0
"
"""

# Zero-shot implementation (based only on the task description)
def count_vowels_zero_shot(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Few-shot implementation (informed by examples)
def count_vowels_few_shot(s):
    # Based on the examples, the function should be case-insensitive and count all vowels
    return sum(1 for char in s if char.lower() in 'aeiou')

# Test cases for comparison
test_strings = [
    "hello",        # 2 vowels
    "AIAC",         # 3 vowels
    "sky",          # 0 vowels
    "Python",       # 1 vowel
    "Beautiful",    # 5 vowels
    "bcd",          # 0 vowels
    "AEIOUaeiou",   # 10 vowels
]

print("Comparing Zero-shot and Few-shot Prompt Implementations:\n")
print(f"{'Input String':<15} {'Zero-shot':<10} {'Few-shot':<10}")
print("-" * 40)
for s in test_strings:
    zero_shot_result = count_vowels_zero_shot(s)
    few_shot_result = count_vowels_few_shot(s)
    print(f"{s:<15} {zero_shot_result:<10} {few_shot_result:<10}")

print("\nReflection:")
print("""
- Both zero-shot and few-shot implementations produce correct results for the provided test cases.
- The zero-shot approach relies solely on the task description, so it may be more verbose or less optimized.
- The few-shot approach, informed by examples, can lead to more concise and idiomatic code (e.g., using generator expressions).
- Few-shot prompts help clarify edge cases (like case sensitivity) and expected behavior, reducing ambiguity.
""")
