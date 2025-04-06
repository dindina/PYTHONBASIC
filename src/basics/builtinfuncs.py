# len

array = [1,2,3,4,5]
print(len(array))

set111 = {1,2,3,4,5}
print(len(set111))

dict11 = {1:'dinesh',2:'saran'}
print(len(dict11))

tuple22 = (1,2,3,4,5)
print(len(tuple22))


str111 = "dinesh"
print(len(str111))


#type

x = 10
print(type(x))       # Output: <class 'int'>

array = [1,2,3]
print(type(array))   # Output: <class 'list'>

set333 = {1,2,3}
print(type(set333))     # Output: <class 'set'>

dict1111 = {1:'dinesh',2:'saran'}
print(type(dict1111))    # Output: <class 'dict'>

str333 = "dinesh"
print(type(str333))     # Output: <class 'str'>

float1 =  10.1
print(type(float1))  # Output: <class 'float'>


#list

tuple1 = (8,9,10)
list1 = list(tuple1)
print(type(list1))   # Output: <class 'list'>

my_string = "abc"
list2 = list(my_string)
print(list2)  # Output: ['a', 'b', 'c']


# tuple function
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)     # Output: (1, 2, 3)

# dict function 
pairs = [('a',1),('b',2),('c',3)]
my_dict = dict(pairs)
print(my_dict)

mynewdict = dict(dinesh=1,saran=2)
print(mynewdict)


# set

klist = [1,2,2,3,33,33]

myset1 = set(klist)
print(myset1)

# int float str

mystr = "1"
print(int(mystr)+111)

mystr = "11.22"
print(float(mystr)+111)

num = 123
print(str(num) + "dinesh")

my_list1 = [1, 2, 3]
print(str(my_list1) + "dinesh")  # Output: "[1, 2, 3]"

# abs
negative = -100
positive = abs(negative)
print(positive)  # Output: 100)

# pow 
base = 10
power = 5

value = pow(base, power)
print(value)  # Output: 10000

# round
print(round(3.14159, 2))  # Output: 3.14
print(round(3.7))        # Output: 4


# range
for i in range(5):
    print(i)        # Output: 0 1 2 3 4
for i in range(2, 7, 2):
    print(i)        # Output: 2 4 6

# sum
numbers = [11, 21, 31, 41]
print(sum(numbers))      # Output: 104
print(sum(numbers, 10))  # Output: 114

# max
numbers = [11, 21, 31, 41]
print(max(numbers))      # Output: 41

# min 
numbers = [11, 21, 31, 41]
print(min(numbers))

# sorted 
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)

numbers.sort()
print(sorted_numbers)  
print(numbers)

# reversed
numbers1 = [1, 2, 3, 4, 5]
reversed_numbers = reversed(numbers1) # Returns a reverse iterator over the elements of a sequence
print(reversed_numbers) # will not print the array
print(list(reversed_numbers))  # Output: [5, 4, 3, 2, 1]

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


dicty = dict(zip(names,ages))
print(dicty)


