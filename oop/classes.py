# make new class
class Counter:

    # make constructor
    def __init__(self):
        self.count = 0

    # crate funtions/ methods
    def display(self):
        print(f"Count is: {self.count}")

    def increment(self):
        self.count +=1
        print("Value is incremented")
        

# crate objects of the class
c1 = Counter()
c2 = Counter()

# call object methods
c1.display()
c1.increment()
c1.increment()
c1.increment()
c1.increment()
c1.display()

print("#" * 30)

c2.display()
c2.increment()
c2.increment()
c2.display()
