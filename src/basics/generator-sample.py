def simplegnerator():
    yield "Hello"
    yield 1
    yield 2
    yield "Bye"

mye = simplegnerator()
print(next(mye))    
print(next(mye))    
print(next(mye))    
print(next(mye))    
print(next(mye))    

try:
    print(next(mye))
except StopIteration:
    print("Generator exhausted")