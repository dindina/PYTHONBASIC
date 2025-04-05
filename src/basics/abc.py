from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectable(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 22/7 * self.radius ** 2
    
class CircleRect(Rectable,Circle):
    def __init__(self,width,height,radius):
        #Rectable.__init__(self,width,height)
        #Circle.__init__(self,radius)
        self.width = width
        self.height = height
        self.radius = radius
            
    
    def area(self):
        return Rectable.area(self) + Circle.area(self)

if __name__ == "__main__":
    rect = Rectable(5,10)
    print(rect.area())
    circ = Circle(7)
    print(circ.area())
    circrect = CircleRect(5,10,7)
    print(circrect.area())


        
