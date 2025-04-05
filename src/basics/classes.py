class Dog:
    # Class attributes and methods will go here
    pass  # 'pass' is used when you need an empty block of code

    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        
    def sound(self):
        print("Woof!")
    
    def gename(self):
        print(self.name)
    
    def print(self):
        return "dog is here " + self.name
        
class Cat:
    # Class attributes and methods will go here
    pass  # 'pass' is used when you need an empty block of code

    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        
    def sound(self):
        print("Meow!")
    
    def gename(self):
        print(self.name)
    
    def print(self):
        return "cat is here " + self.name



my_dog = Dog("raho","pupp")  # Creating an object of the Dog class
my_dog.sound()
my_dog.gename()
print(my_dog.print())

my_cate = Cat("tommy","catty")  # Creating an object of the Dog class
my_cate.sound()
my_cate.gename()
print(my_cate.print())