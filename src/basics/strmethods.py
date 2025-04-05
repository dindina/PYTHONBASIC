str = "dinesh the great"

print(str.upper())

print(str.lower())

print(str.capitalize())

print(str.replace('d','j'))

print(str.swapcase())

print(str.count('d')) # 2

print(str.isdecimal())
print(str.title())

print(str.startswith('d'))
print(str.endswith('d'))    

print(f"len = {len(str)}")

print(' '.join(['dinesh','saran']))

print('dinesh,saran'.split(','))

print('dinesh'.rjust(23))

print('dinesh'.ljust(7) + "win")

print('dinesh'.center(15))


print(str.replace('dinesh','saran'))

print()


name1 = input("enter name")

print(f"hello {name1}")
print("hello {}".format(name1))