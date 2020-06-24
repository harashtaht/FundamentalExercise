# -- Part 5 : If Statements -- #

cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# a - Conditional Tests

'''
At the heart of every if statement is an expression that can be evaluated as True or False
and is called a conditional test.
Testing for equality is case sensitive in Python.

'''

# car = 'Audi'
# print(car.lower() == 'audi') #True
# print(car == 'audi') #False

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")
