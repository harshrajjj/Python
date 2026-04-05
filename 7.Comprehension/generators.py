#it is entirely used to save memory and time when we are working with large data sets. It is a type of iterable, like lists or tuples, but instead of storing all the values in memory, it generates them on the fly as you iterate over it.

# Generator expressions are similar to list comprehensions, but they use parentheses instead of square brackets. They are more memory efficient than list comprehensions because they generate items one at a time, rather than storing the entire list in memory.

# Example of a generator expression
squares = (x**2 for x in range(10))

total = sum(x for x in range(11) ) # This will calculate the sum of squares from 0 to 9
print(total)

print(squares)  # This will print a generator object
print(list(squares))  # This will print the list of squares from 0 to 9

