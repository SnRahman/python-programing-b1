from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def move(self):
        print('movement')
        pass

class Human(Animal):
    def move(self):
        print('Humans can walk!')

class Snake(Animal):
    def move(self):
        print("Snake can Crwal")


h1 = Human()
h1.move()

s1 = Snake()
s1.move()