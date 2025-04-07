def divide(a, b):
    import pdb; 
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

print(divide(10, 2))
print(divide(5, 0))