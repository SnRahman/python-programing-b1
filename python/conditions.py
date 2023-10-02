# Task
#     Check two given numbers and return true if one of the numbers is 50 or if their sum is 50.
#     Check from the given integer, whether it is positive or negative.
#     Check whether a given number is even or odd.
#     Check whether a given positive number is a multiple of 3.
#     All the prior tasks are to be solved with functions.
#     check from the given two numbers, weather the first number is "grater", "lesser" or "equal" to the second number.
#     check from the three sides of triangle. use conditions to determine and display 
#     weather the triangle is "Equilateral" (all sides are equal), "Isosceles" (two sides are equal), or "Scalane" (no sides are equal)
#     check from the given month (1-12) if its "Winter" (December-Feburary), "Spring" (March-May), "Summer" (June-August), or "Autumn" OR "Fall" (September-November).
#     Create a function that takes two numbers as input and returns the largest of the two.
#     create a function that takes two strings as input and returns a new string that concatenates both if them.
#     Write a function that takes a temperature in celsius and converts it to Fahrenheit.
#     Write a program that takes the age and checks if they are eligible for voting (e.g 18 or older)
#     Implement a function that checks if a given number is positive, negative, or zero and return the result.
#     create a function that takes two numbers as input and returns their product  using arithmetic operations. (e.g the product of 2 and 3 is 6)
#     implement a function that takes two strings as input and checks if they are equal.
#     Write a function that takes a number as input and returns the absolute value of the number
#     Determine whether a given year is a leap year.


month = 'jan'

if(month=='dec' or month=='jan' or month=='feb'):
    print('Winter')


a = 10
b = 23
c = 2
d = 5


# Arthmetic operators
print(f'a + b is: {a+b}')
print(f'b - a is: {b-a}')
print(f'b * a is: {b*a}')
print(f'b / a is: {b/a}')
print(f'a ** c is: {a**c}')
print(f'b % c is: {b%c}')

# conditional operators
# == , != , > , < , >= , <= 

if(a < b):
    print('True')
    print('Yes')
    print('if')
else:
    print('False')
    print('no')
    print('else')

print('###########################')

if(a == b):
    print('both values are equalls')
elif(a == c):
    print('2nd condition is true')
else:
    print('Not Equall')

# Logical operators
# And OR Not

if( a>b and a>c ):
    print('a is greater')
elif(b >a and b>c):
    print('b is greater')
elif(c>a and c>b):
    print('c is greater')


if( a>b or a>c ):
    print('a is greater')
if(b >a or b>c):
    print('b is greater')
if(c>a or c>b):
    print('c is greater')

if (not a==b):
    print('matched')

print('###########################')
print('Functions')

# function without parameters
def display():
    print('hello World!')

display()

# function with parameters
def add(x,z):
    c = x+z
    print(f"sum is:{c}")

add(c,b)
add(12,10)

# function with default values
def pow(b,p=2):
    d = b**p
    print(f"Answer is: {d}")

pow(5)
pow(5,3)

# assing positional values

def sum(a,b,c,d):
    print(f" A:{a}")
    print(f" B:{b}")
    print(f" C:{c}")
    print(f" D:{d}")
    print(f"sum is :{a+b+c+d}")

print('###########################')

sum(10,12,125,25)
sum(a,b,c,d)
sum(d=12,a=25,c=10,b=6)



def mul(X,Y=1,Z=1):
    print('Answer is: {}'.format(X*Y*Z))

mul(2)
mul(2,3)
mul(X=2,Z=5)
mul(2,Z=5)

print('###########################')

# Returning functions
def sub(l,m):
    c= l-m
    print(c)
    return c

result = sub(10,5)
print(f"result is :{result}")
print(sub(10,5))













# print('hello')






