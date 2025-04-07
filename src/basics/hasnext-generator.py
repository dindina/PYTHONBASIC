def has_next(iterator):
    try:
        first = next(iterator)
        return True, first
    except StopIteration:
        return False, None

def my_generator(n):
    for i in range(n):
        yield i

gen = my_generator(5)

has_more, next_val = has_next(gen)
if has_more:
    print(f"The next value is: {next_val}")
    print(f"Consumed the first value: {next_val}")
    for value in gen:
        print(f"Remaining value: {value}")
else:
    print("The generator has no more values.")