# Problem 1
# Create a function called biggest(numbers).
# It should return the biggest number in the list.
# Call it and print the result.
def biggest(numbers):
    biggest_num = numbers(0)
 for num in numbers[1:]:
        if num > biggest_num:
            biggest_num = num
            return biggest_num
            my_list = [10, 24, 76, 23, 12]
result = biggest(my_list)
print(result)

# Problem 2
# Create a function called frequency(word).
# It should return a dictionary that counts how many times each letter appears.
# Call it and print the result.
def frequency(word):
    """Return a dictionary with each letter and its count."""
    counts = {}
for letter in word:
     if letter in counts:
            counts[letter] += 1
        else:

# Problem 3
# Create a function called min_and_max(numbers).
# It should return the smallest and biggest number.
# Call it, unpack the results, and print both.



# Problem 4
# Create a helper function called is_long(word).
# It should return True if the word has at least 5 letters.
# Create another function called count_long_words(words).
# It should count how many words are long.



# Problem 5
# Create a function called average(numbers).
# It should return the average of the numbers in the list.
# Call it and print the result.
