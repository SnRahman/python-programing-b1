class Car:
    def __init__(self,color,model,brand):
        self.color = color
        self.model = model
        self.brand = brand

    def display_color(self):
        print(f"Color is :{self.color}")

    def display_model(self):
        print(f"Model is :{self.model}")

    def display_brand(self):
        print(f"Brand is :{self.brand}")

class Honda(Car):

    def __init__(self,color,model):
        Car.__init__(self,color,model,"Honda")

class Toyota(Car):
    def __init__(self,color,model):
        Car.__init__(self,color,model,"Toyota")

c1= Car('Black',"civic","honda")
c1.display_color()
c1.display_model()
c1.display_brand()
print("#" * 50)

h1= Honda('Black',"civic")
h1.display_color()
h1.display_model()
h1.display_brand()

print("#" * 50)

h1= Honda('White',"city")
h1.display_color()
h1.display_model()
h1.display_brand()

print("#" * 50)
t1 = Toyota('Grey','Corolla')
t1.display_color()
t1.display_model()
t1.display_brand()
