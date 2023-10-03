class Circle:
    pi = 3.14159  # Static property

    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def add(x, y):
        return x + y
    
# Accessing the static property using the class name
print(Circle.pi)  # Output: 3.14159

# Accessing the static property using an instance
circle = Circle(5)
print(circle.pi)  # Also outputs: 3.14159
