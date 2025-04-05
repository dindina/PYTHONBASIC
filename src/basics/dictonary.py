hashmap = {1:'dinesh', 2:'saran', "dinesh" : 1 , "saran" : 2}
print(hashmap)
print(hashmap[1])
print(hashmap['saran'])

print(hashmap.keys())
print(hashmap.get('dinesh'))
print(hashmap.values())

print(hashmap.items())

print('sara1n' in hashmap)



for key in hashmap.keys():
    print(key)

for value in hashmap.values():
    print(value)

for key in hashmap.keys():
    print(f"{key} = {hashmap.get(key)} ")

for key in hashmap.items():
    print(f"{key[0]} = {key[1]} ")

for key,value in hashmap.items():
    print(f"{key} = {value} ")

hashmap1 = {"dinesh" : 100000 , "saran" : 20000}
hashmap.update(hashmap1)
print(hashmap)

hashmap.setdefault("dinesh1",1555)
print(hashmap)



ex_1 = {}.fromkeys("addr",["dinesh","saran"])
print(ex_1)


ex_1 = {"model":"civic", "brand":"honda" }
ex_1.pop("model")   
print(ex_1)

ex_1 = {"model":"civic", "brand":"honda" }
ex_1.popitem()   
print(ex_1)

print(hashmap.get("dinesh11",1))

empty = dict(dinesh=1,saran=2)
print(empty)