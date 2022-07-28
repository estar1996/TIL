1. 
class Circle:
    pi = 3.14

    def __init__(self,r,x,y):
      self.r = r
      self.x = x
      self.y = y

    
    def area(self):
      return Circle.pi * self.r * self.r
    
    def circumference(self):
      return 2 * Circle.pi * self.r
    
    def center(self):
      return(self.x,self.y)

a = Circle(3,2,4)

print(Circle.area(a))
print(Circle.circumference(a))


2. 
class Animal :
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')
    def eat(self):
        print(f'{self.name}! 먹는다!')



class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
    def run(self):
        print(f'{self.name}! 달린다!')
    def bark(self):
        print(f'{self.name}! 먹는다!')

class Bird(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
    def walk(self):
        print(f'{self.name}! 걷는다!')
    def eat(self):
        print(f'{self.name}! 먹는다!')
    def fly(self):
        print(f'{self.name}! 푸드덕!')
dog = Dog('꼽이')
bird = Bird('구구')

print(Bird.eat(Bird('구구')))

# None 이 출력됩니다 ...?

3. 
(a) : fibo.py
(b) : fibo_recursion
(c) : recrusion 