# zip
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
zipped = zip(names, ages)
print(list(zipped))  
print(type(zipped))
for name, age in zipped:
    print(f"{name} is {age} years old.")

names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
city = ["city1", "city2", "city3"]
zipped = zip(names, ages,city)
print(list(zipped)) 

# to convert two lists into a dict

dicty = dict(zip(names,ages))
print(dicty)


prices = [10, 20, 15]
quantities = [3, 2, 5]

somevalue = zip(prices,quantities)
print("printing zip " + somevalue.__str__())
print(list(somevalue))


# Processing Corresponding Elements in Calculations:

prices = [10, 20, 15]
quantities = [3, 2, 5]

# get the total price

total_price = [ price*qty  for price,qty in zip(prices,quantities)]
print(total_price)
print(sum(total_price))

# Comparing Elements of Two Lists:
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 4, 4, 6]

compare = [ (x,y) for x,y in zip(list1,list2) if x!=y]
print(compare)


# Creating Pairs of Adjacent Elements:
# Scenario: You want to process elements in a list in pairs.
data = [10, 20, 30, 40, 50]

adjacent_pairs = zip(data, data[1:])
for first, second in adjacent_pairs:
    print(f"Pair: ({first}, {second})")


# Transposing a List of Lists (Matrix):
# Scenario: You have a list of lists representing a matrix, and you want to transpose it (swap rows and columns).
# 

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in zip(*matrix):
    print(row)
transposed_matrix = [list(row) for row in zip(*matrix)]
print(transposed_matrix)

listee = [1,3,31,32]
mylisee = [*listee]
print(mylisee)

