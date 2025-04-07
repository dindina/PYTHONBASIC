def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))       # Output: 6
print(sum_all(10, 20, 30, 40)) # Output: 100
print(sum_all())             # Output: 0 (empty tuple)

def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Bob", age=30, city="New York")
# Output:
# name: Bob
# age: 30
# city: New York

describe_person(occupation="Engineer", country="USA")
# Output:
# occupation: Engineer
# country: USA


def combined_args(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

combined_args(1, 2, "hello", name="Charlie", age=25)
# Output:
# Positional arguments (args): (1, 2, 'hello')
# Keyword arguments (kwargs): {'name': 'Charlie', 'age': 25}