try:
    val1 = int(input("enter the first number "))
    if val1 < 0:
            raise ValueError("Input must be a non-negative integer.")
    val2 = int(input("enter the second number "))
    result = val1//val2
    print(f" The result is {result}")
except TypeError as e:    
    print(f" The error is {e}")
except ZeroDivisionError:
    print("Cannot divide by zero")     
except ValueError as e:    
    print(f" The Value error is {e}")
    