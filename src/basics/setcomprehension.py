#new_set = {expression for item in iterable if condition}

# Creating a Set of Squares of Numbers:

number_list = [1,2,3,3,5,6,6]
print(number_list)
square_setty = { number**2 for number in number_list }
print(square_setty)



list11 = [1,2,3,4]
print(type(list11))

list11 = {1,2,3,4}
print(type(list11))

list11 = (1,2,3,4)
print(type(list11))


#Extracting Unique First Letters from a List of Words:
words = ["apple", "banana", "apricot", "grape", "blueberry"]

unique = { str[0]  for str in words }
print(sorted(unique))


# Filtering Even Numbers and Adding Them to a Set:
numbers = [1, 2, 3, 4, 5, 6, 2, 4, 8]

even_numbers = { number for number in numbers  if number %2 == 0}
print(even_numbers)

#  Creating a Set of Lengths of Words:

phrases = ["the quick brown fox", "jumps over", "the lazy dog"]

for phrase in phrases:
    for word in phrase.split():
        print(word)

lenght = { len(word) for phrase in phrases for word in phrase.split() }

print(lenght)


str = "hello,how,are,you"
splitted = str.split(",")
print(type(splitted))


# Generating a Set of Unicode Code Points for Characters in a String:
text = "hello world"

unicodes = {ord(ch) for ch in text}
print(unicodes)

# Creating a Set of Transformed Values from a Dictionary:
data = {"a": 10, "b": 20, "c": 10, "d": 30}

trans_values = { value*2 for value in data.values() }
print(trans_values)

trans_keys = { value*2 for value in data.keys() }
print(trans_keys)
