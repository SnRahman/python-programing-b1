class Sum:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def display(self):
        print(f"Value A is: {self.a} \nValue B is: {self.b} ")
    
    def add(self):
        print(f"sum is : {self.a + self.b }")


class Mul(Sum):

    # def __init__(self,a,b):
    #     self.a = a
    #     self.b = b

    # def display(self):
    #     print(f"Value A is: {self.a} \nValue B is: {self.b} ")
    
    def mul(self):
        print(f"multiply is : {self.a * self.b }")


class Sub(Sum):
    def div(self):
        print(f"Division is : { self.a /self.b}")
    



# class Mul(Sum):
#     def mul(self):
#         print(f"Mul is : {self.a + self.b }")


s1 = Sum(12,10)
s2 = Sum(10,30)
s3 = Sum(100,330)
# m1= Mul(2,3)
# m1.mul()

# s1.display()
s1.add()
s2.add()
s3.add()

print("#" * 50)

m1 = Mul(10,2)
m1.mul()
m1.add()

print("#" * 50)

d1 = Sub(50,25)
d1.div()
d1.add()