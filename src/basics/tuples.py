tuple1 = ('a','b','c','d','e')
print(tuple1)
print(tuple1[0])
print(tuple1[0:3])


list1 = ['a','b','c','d','e']

print("printing tuple")
for i in tuple1:
    print(i)
print("printing list")
for i in range(0,len(tuple1)-2):
    print(tuple1[i]) 


nested = ((1,2,3), (4,5,6))       

print(nested[1])
print(nested[1][0])
print(nested[1][2])


repeat1 = ( 1, 3, 4, 4, 4 ,5 ,6 ,7)

print(repeat1.count(4))