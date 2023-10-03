class Circle:
    # define static variables
    pi = 3.14

    def __init__(self,r):
        self.radius = r

    def cal_area(self):
        area = Circle.pi * (self.radius ** 2)
        print(f"area is: {area}")

    # define Static method
    @staticmethod
    def area(rad):
        area = Circle.pi * (rad ** 2)
        print(f"area is: {area}")

    

# normal objects of class
c1= Circle(3)
c2= Circle(4)
c1.cal_area()
c2.cal_area()

# call static methods/functions
Circle.area(5)

# call/ use static property/ variables
print(Circle.pi)
print(Circle.pi)
