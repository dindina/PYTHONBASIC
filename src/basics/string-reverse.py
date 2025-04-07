def reverse( mystr: str) -> str:
    return mystr[::-1]

str1 = "dinesh"
print(reverse(str1))



print(str1[0:1])
print(str1[0:len(str1)])
print(str1[::-1])


my_string = "world"
reversed_iterator = reversed(my_string)
print(reversed_iterator)

reversed_string = "".join(reversed_iterator)
print(reversed_string)

print(my_string[::-1])


# reverse an  array

intarray = [1,2,3,33]
print(intarray[::-1])

mytuple = (1,2,3,345,2)
print(mytuple[::-1])

