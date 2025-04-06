mystr = "dinesh"

# convert to array

mylist = list(mystr)

print(mylist)

from collections import Counter
counts = Counter(mylist)
print(counts)

data = "apple,banana,orange"
fruits = data.split(',')
joined_fruits = "-".join(fruits)
print(f"Joined string: {joined_fruits}") # Output: apple-banana-orange

print(mystr.join(fruits))


# Joining a List of Words with a Space:
words = ["This", "is", "a", "sentence."]
separator = " "
print(separator.join(words))


#Joining a Tuple:
colors = ("red", "green", "blue")
separator = ", "
color_string = separator.join(colors)
print(color_string)  # Output: red, green, blue
