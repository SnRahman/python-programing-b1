# Task
"""
1- Sum all the list elements by using both a loop and a Python built-in function.
2- Reverse the list by using both a loop and a Python built-in function.
3- Make a table of the given number with all possible loops.
4- Find the largest number in a list by using both a loop and a Python built-in function.
5- Find the smallest number in a list by using both a loop and a Python built-in function.
6- Add the list element at the specified index.
7- Delete the list element from the specified index.
8- Make a normal list to store the name of 5 students and iterate with for loop.
9- Make an associative list to store the name of 5 students and iterate with a for loop.
10- Make a normal list of associative Lists(a list that will have associative Lists) to store the information of at least 2 students and access them as hard-coded.
    Information to store:
        A- Name, age, registration number, course, favorite programming languages (should be a normal list), Marks of 5 different subjects (should be an associative list).
    The operations to perform:
        B- Display every single value for any student.
        C- Display the first and last favorite programming languages of any student.
        D- Display the marks of any two subjects for any student.
"""


# lambda functions
def abc():
    print('hello')

a = 10
b = lambda a : a**2
print(b(a))

add = lambda x,y : x+y
result = add(14,25)
result1 = add(12,50)

print(result)
print(result1)


# list
li = [1,5,2,78,6,9,7,45,7,87,7,70]
lis = [144,2.20,'string',True]
a = 100

# print all list
print(li)
print(lis)

# get value by index
print(li[3])
print(lis[2])

# updaate value by index
li[2] = 20

# get list length
a = []
length = len(li)
print(f"length is:{length}")

# append new item at the end
li.append(100)

# add new items at the end
li.extend( lis )
li.extend( [90,87,65] )

# insert new value at desired place
li.insert(4,50)

# remove value from list
li.remove(7)

# remove and return single value from the last by index
value = li.pop()
value = li.pop(5)
print(value)

# get index of the value form the list
index = li.index(87)
print(index)

# count the total accurance of the element in the list
count = li.count(7)
print(count)

# sort list in Ascending order
li.sort()
d = [10.01, 10.05,10.10,10.50,10.89,-10.05,10.56]
d.sort()

# reverse order the existing list
li.reverse()

# get a copy of existing list
copy =li.copy()
print(copy)

# remove all the 
li.clear()

# check if an element exists in a list
check = 100 in li
print(check)
print(45 in li)

# How to identify a list?
print(type(li))
print(type(a))
var_type = type(li)
var_type = type(lis[3])

# print(var_type)
result =  isinstance(a,list)
result1 =  isinstance(li,list)
print(result)
print(result1)

# dictionary 
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

# get dictionay values
print(person)
print(person['age'])
print(person['name'])
print(person['city'])

# update and add key  dictionay
person['age'] = 25
person['gender'] = "Male"

# print(person['gender'])
print(person)

# delete existing key
del person['age']
print(person)


# Tuples 
t = (1,5,2,4)
print(t)
print(t[2])

# loops
# for loop

for i in li:
    print(i)

length = len(li)
print(length)
for j in range(length):
    print(F"index :{j} value is: {li[j]}") 

for j in range(1,11):
    print(j) 

# while loop

count = 0
while (count<10 ):
    count +=1
    print('hello')

while count<10:
    count +=1
    print('hello')

# break the loop on given condition
for i in range(10):
    print(i)
    if(i == 5):
        break


# skip the current iteration and jumps to next iteration.
for i in range(10):
    if(i%2 != 0):
        continue    
    print(i)

# else in loops
# else case runs when loop successfully completed without break or any other intruption
for i in range(5):
    print(i)
else:
    print('Loop is completed')

for i in range(5):
    if(i%2 != 0):
        continue 
    print(i)
else:
    print('Loop is completed')

# get key and values from list and tuples
# list example
for index,value in enumerate(li):
    print(f' index: {index} value: {value}')

# get key values from dictionary
for key,value in person.items():
    print(f' key: {key} value: {value}')


















