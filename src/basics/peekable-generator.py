from itertools import peekable

def my_generator(n):
    for i in range(n):
        yield i

# Create a peekable object from the generator
gen = peekable(my_generator(5))

# Check if there's a next value without consuming it
if gen:  # peekable object is truthy if it has more items
    next_value = gen.peek()
    print(f"The next value is: {next_value}")
    # Now you can safely consume the value if needed
    first_value = next(gen)
    print(f"Consumed the first value: {first_value}")
else:
    print("The generator has no more values.")

# Continue consuming the rest of the values
print("Remaining values:")
for value in gen:
    print(value)

# After all values are consumed, the peekable object becomes falsy
if not gen:
    print("The generator is now exhausted.")