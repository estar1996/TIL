# 22.07.28

## 클래스 복습

```python
from datetime import datetime

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @classmethod
    def detail(cls,name,year):
        now_year = datetime.today().year
        age = now_year - year
        return cls(name,age)
    
    def check_age(name,year):
        if year <= (2022-19):
            return True
        else:
            return False

    

gyu = Person.detail('gyu',1996)
gyu = Person('gyu',datetime.today().year-1996)

print(gyu.age,Person.check_age(gyu,1996))
```

이름과 연도를 입력하면 나이와 미성년 여부를 리턴하는 클래스이다.

```python
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
```

왜 잘 나오는데 뒤에 None 이 붙을까 ??