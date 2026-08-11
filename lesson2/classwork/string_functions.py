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

Max Ch
1:38 PM
text = "   Hello world   "
print("Raw text is:", text)

print(text.lower())  # make everything lowercase
print(text.upper())  # make everything uppercase
print(text.title())  # title case

print(text.strip())  # remove spaces on the left and right
print(text.strip().lower())

message = "banana bread"
print("Count of a:", message.count("a"))
print("Find 'bread':", message.find("bread")) # index of first match (or -1)

print(message.replace("banana", "pumpkin"))