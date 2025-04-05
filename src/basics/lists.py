list = [1, 2, 3, 4, 5]
print(list)

list1 = ['dinesh', 2, 3, 4.5, True]
print(list1)    

print(1 in list1) # True , becaase the list1 contains 'True' which is 1 
#print(1 in list)


list2 = ['dinesh', 2, 3, 4.5, False]
print(1 in list2)  # Output: False (because False is 0)

print(type(list1))


del list1[0]
print(list1)

list1.remove(True)
print(list1)

list1.append("jaja")
print(list1)
list1.insert(2, "jaja")
print(list1)

strlist = ['xdi','l','ppp'];
strlist.sort()
print(strlist)
strlist.sort(reverse=True)
print(strlist)


asciibetial = ['a','b','c','A','D'] 
asciibetial.sort(key=str.lower)
print(asciibetial)    