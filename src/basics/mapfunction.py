# Squaring a List of Numbers:
numbers = [1, 2, 3, 4, 5]
sq = map(lambda x: x**2 , numbers )
print(type(sq))
print(list(sq))


dicty = {'a':1,'b':2}
print(type(dicty))

club = map(lambda item : item[0]+str(item[1]) , dicty.items())
print(list(club))




