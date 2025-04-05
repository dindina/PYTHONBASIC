print('hello')
set2 = set({ 1 , 3 ,4 ,5 })
set3  = set()
set4 = set(range(1,12,2))
print(set2)
print(set3)
print(set4)

set2.add(100)
print(set2)

set2.remove(100)
print(set2)

set2.discard(10)
print(set2)


set11 = { char.lower() for char in 'dinesh'}
print(set11)