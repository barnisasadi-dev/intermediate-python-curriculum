# Problem 1
# Ask the user for two numbers.
# Print their sum, difference, and product.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old")

# Problem 2
# Ask the user for a number.
# Print whether the number is even or odd.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


# Problem 3
# Create a list of numbers.
# Print the biggest number in the list.

numbers = [4, 10, 3, 5, 8]
total = 0
for i in range(len(numbers)):
    total = total + numbers[i]
print("Sum:", total)

# Problem 4
# Use a while loop to print the numbers from 1 to 10.
animals = ["cat", "dog", "cat", "bird", "cat"]
count = 0
for i in range(len(animals)):
    if animals[i] == "cat":
        count = count + 1
print("Cats:", count)

# Problem 5
# Create a function called count_above_10(numbers).
# It should return how many numbers in the list are above 10.
# Call it and print the result.

first = "Sova"
last = "Coding"

# String concatenation
full = first + " " + last
print(full)

# Repeat a string
print("ha" * 3)  # 'hahaha'

# 'in' checks if something appears inside a string
sentence = "I like python"
print("python" in sentence)
print("java" in sentence)

# Escape characters
print("He said, \"hello\"")
print("He said, \'hello\'")
print("\\")

print("Line 1\nLine 2")
