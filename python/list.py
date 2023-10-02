square = lambda x: x * x
print(square(5))  # Output: 25


my_list = [1, 2, 3, 4, 5]
first_element = my_list[0]  # Access the first element (1)
my_list[2] = 10  # Change the third element to 10

list_length = len(my_list)  # Returns the number of elements in the list
my_list.append(6)  # Adds 6 to the end of the list
my_list.extend([4, 5])  # Appends the elements of an iterable (e.g., another list) to the end of the list.
my_list.insert(1, 10) # Inserts an element at a specified index.
my_list.remove(4)  # Removes the first occurrence of 4
popped_element = my_list.pop()  # Removes and returns the third element (10)
popped_element = my_list.pop(2)  # Removes and returns the third element (10)
index = my_list.index(5) # Returns the index of the first occurrence of a value in the list.
count = my_list.count(2) #  Returns the number of occurrences of a value in the list.
my_list.sort()  # Sorts the list in place ASC
my_list.reverse()  # Reverses the list in place
copied_list = my_list.copy() # Creates a shallow copy of the list.
my_list.clear()  # Results in an empty list: []

# check if an element exists in a list
if(2 in my_list):
    print(True)
else:
    print(False)


print(f"popped_elemet: {popped_element}")
print(f"copied: {copied_list}")
print(my_list)

# Iterating Through a List:
for item in my_list:
    print(item)


# How to identify a list?
my_variable = [1, 2, 3]
if isinstance(my_variable, list):
    print("It's a list")


my_variable = [1, 2, 3]
if type(my_variable) is list:
    print("It's a list")

if type(my_variable) ==  list:
    print("It's a list")




# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values by key
print(person["name"])  # Output: John
print(person["age"])   # Output: 30

# Modifying values
person["age"] = 31

# Adding a new key-value pair
person["country"] = "USA"

# Removing a key-value pair
del person["city"]

#tuples
my_tuple = (1, 2, 3)
another_tuple = "apple", "banana", "cherry"
mixed_tuple = (1, "apple", 3.14, (4, 5))

a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3


#FOR LOOP
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: Using a range to specify the number of iterations
for i in range(5):  # Iterates from 0 to 4
    print(i)



#while loop
count = 0
while count < 5:
    print(count)
    count += 1


#break and continue
for i in range(10):
    if i == 5:
        break  # Exit the loop when i reaches 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

#else
fruits = ["apple", "banana", "cherry"]
searched_fruit = "orange"

for fruit in fruits:
    if fruit == searched_fruit:
        print(f"The fruit '{searched_fruit}' is found!")
        break
else:
    print(f"The fruit '{searched_fruit}' is not in the list.")

# get key and values

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

