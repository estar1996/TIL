1. 
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 


class Rec:
    def __init__(self, p1, p2):
        self.p1 = p1  
        self.p2 = p2 
        self.height = abs(p1.x - p2.x)
        self.width = abs(p1.y - p2.x)
    def area(self):
        return self.height*self.width
    
    def perimeter(self):
        return  (self.height + self.width)* 2 
    
    def square(self):
        return  self.height == self.width

