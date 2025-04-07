
#Similar to list comprehensions, Python offers generator expressions, which provide a concise way to create anonymous generator functions. They use parentheses () instead of square brackets 

# List comprehension (creates a list in memory)

squares_list = [x**2 for x in range(5)]
print(squares_list)  # Output: [0, 1, 4, 9, 16]

# Generator expression (creates a generator object)
squares_gen = (x**2 for x in range(5))
print(squares_gen)   # Output: <generator object <genexpr> at 0x...>

# Iterate through the generator expression
for sq in squares_gen:
    print(sq)