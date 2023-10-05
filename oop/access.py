
# private example
class Car:

    # how to devlare access of variables and methods /funtions
    
    # public 
    # whitout any underscore at start of the name

    # private
    # double underscore at atart of the name

    # protected
    # single undersrore at the start of the name 
  
    def __init__(self,c,m,b):
        # public variables
        # self.color = c
        # self.model = m
        # self.brand = b

        # private variables
        self.__color = c
        self.__model = m
        self.__brand = b

    def __display(self):
        print(f"Color :{ self.__color }")
        print(f"Model :{ self.__model }")
        print(f"Brand :{ self.__brand }")
    
    def display_all(self):
        print(f"Color :{ self.__color }")
        print(f"Model :{ self.__model }")
        print(f"Brand :{ self.__brand }")

class Honda(Car):

    def __init__(self,c,m):
        Car.__init__(self,c,m,"Honda")
        super().__init__(self,c,m,"Honda")

    def display_self(self):
        print(f'Color is: {self.__color}')



# c1 = Car('White',"civic","Honda")

# c1.display_all()
# print(c1.__model)
# print(c1.brand)
# print(c1.color)
# print(c1.model)


# h1 = Honda('Black','City')
# h1.display_self()

# protected
class Vehicle:

    def __init__(self,c,m,b):
        # public variables
        # self.color = c
        # self.model = m
        # self.brand = b

        # private variables
        self._color = c
        self._model = m
        self._brand = b
    
    def display_all(self):
        print(f"Color :{ self._color }")
        print(f"Model :{ self._model }")
        print(f"Brand :{ self._brand }")


class Honda(Vehicle):
    def __init__(self,c,m):

        Vehicle.__init__(self,c,m,"Honda")
        # super().__init__(self,c,m,"Honda")

    def display_self(self):
        print(f'Color is: {self._color}')

# v1 = Vehicle('Black','City','Honda')
# v1.display_all()

h1 = Honda('while','city')
h1.display_self()



