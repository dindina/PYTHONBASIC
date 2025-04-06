# new_list = [expression for item in iterable if condition]

# Creating a List of Squares:

numbers = [1, 2, 3, 4, 5]
squares = [ number**2 for number in numbers]
print(squares)

# Filtering Even Numbers and Squaring Them:

numbers = list( range(0,12))
even_squares = [ number**2 for number in numbers if number % 2 ==0] 
print(even_squares)

strings = ["dinesh","saran",'ami','avini']

upper_strings = [ str.upper() for str in strings]
print(upper_strings)


first_chars = [ str[0] for str in strings ] 
print(first_chars)


# Creating a List of Tuples:

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

tuplie = [ (x,y) for x,y in zip(list1,list2)]
print(tuplie)

dicty = [ {x:y} for x,y in zip(list2,list1)]
print(dicty)


# Flattening a List of Lists:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [ col for row in matrix for col in row] 
print(flat_list)
