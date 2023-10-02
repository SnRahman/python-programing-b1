# 1
# define a class 
class test:
    class_attribute = "I am a class attribute"


# make object of class
obj = test()

print(obj.class_attribute)

# 2
class MyClass:
    # class property
    class_property = 42

obj1 = MyClass()
print(obj1.class_property)

# 3
class MyClass:
    class_property = 42

    def class_method(self):
        return f"This is a class method. class_property = {self.class_property}"
    
obj1 = MyClass()
print(obj1.class_method())  # Output: This is a class method. class_property = 42



class MyClass:
    class_variable = 0
    increment = 0

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

    def increment_increment(self):
        self.increment += 1

obj1 = MyClass()
obj2 = MyClass()

obj1.increment_class_variable()
print(obj1. )  # Output: 1
print(obj2.class_variable)  # Output: 1
