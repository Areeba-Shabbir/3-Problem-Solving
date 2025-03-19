      # Problem-Solving Challenges
# 🔹 Problem 1: Reverse a String
 # Write a function that takes a string as input and returns the reversed string.

def reverse_string(s: str) -> str:
    return s[::-1]
print(reverse_string("hello"))  # Output: "olleh"

#s[::-1] uses slicing to reverse the string.
# -1 as the step parameter tells Python to traverse the string backward.


# 🔹 Problem 2: Count Vowels in a String
# Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).

def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels("Apple"))  # Output: 2


# 🔹 Problem 3: Sum of Digits
# Write a function that takes a non-negative integer and returns the sum of its digits.

# Using String Conversion

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_of_digits(1234))  # Output: 10


# Using Modulus and Division (Mathematical Approach)

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # Extract the last digit
        n //= 10  # Remove the last digit
    return total

print(sum_of_digits(1234))  # Output: 10


