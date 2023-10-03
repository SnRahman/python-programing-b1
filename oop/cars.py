class Car:
    def __init__(self,color,model,brand):
        self._color = color
        self._model = model
        self._brand = brand

    def display_color(self):
        print(f"Color is :{self._color}")

    def display_model(self):
        print(f"Model is :{self._model}")

    def display_brand(self):
        print(f"Brand is :{self._brand}")

    def _display_all(self):
        print(f'color: {self._color}')
        print(f'Model: {self._model}')
        print(f'Brand: {self._brand}')



class Honda(Car):

    def __init__(self,color,model):
        Car.__init__(self,color,model,"Honda")
    
    def display(self):
        print(f'color: {self._color}')
        print(f'Model: {self._model}')
        print(f'Brand: {self._brand}')


class Toyota(Car):
    def __init__(self,color,model):
        Car.__init__(self,color,model,"Toyota")

c1= Car('Black',"civic","honda")
c1._display_all()
# c1.display_color()
# c1.display_model()
# c1.display_brand()
# print("#" * 50)

# h1= Honda('Black',"civic")
# h1.display()
# h1.display_color()
# h1.display_model()
# h1.display_brand()

# print("#" * 50)

# h1= Honda('White',"city")
# h1.display_color()
# h1.display_model()
# h1.display_brand()

# print("#" * 50)
# t1 = Toyota('Grey','Corolla')
# t1.display_color()
# t1.display_model()
# t1.display_brand()
