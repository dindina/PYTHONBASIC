import sys

a = [1, 2, 3]
print(f"Initial refcount of a: {sys.getrefcount(a)}")

b = a
print(f"Refcount of a after b = a: {sys.getrefcount(a)}")

def my_func(arg):
    print(f"Refcount of arg inside function: {sys.getrefcount(arg)}")

my_func(a)
print(f"Refcount of a after function call: {sys.getrefcount(a)}")

del b
print(f"Refcount of a after del b: {sys.getrefcount(a)}")