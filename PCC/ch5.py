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

# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print("Hold the anchovies")

age_0 = 22
age_1 = 18

# print((age_0>=21) and (age_1<=21))

requested_topping = ['mushrooms', 'onions', 'pineapple']

# print('mushrooms' in requested_topping)

# banned_users = ['andrew', 'carolina', 'david']
# user = ['marie', 'andrew']

# for i in user:
#     if i not in banned_users:
#         print(i.title()+", you can post a response if you wish")
#     else:
#         print("shut the fuck up, " + i.title() + ". You're motherfucking banned, you bitch.")

# age = int(input("What's your age? "))

# if age < 4:
#     print(f"The fee is free for a {age} years old. Enjoy!")
# elif 4 <= age < 18:
#     print(f"For a {age} years old, the fee for an entry will be 5$.")
# else:
#     print(f"The fee will be 10$ for a {age} years old.")

# if age <4:
#     price = 0
# elif age <18:
#     price = 5
# else:
#     price = 10

# print(f"Your admission cost is $ {price}")

# requested_topping = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_topping:
#     print('Adding mushrooms.')
# if 'pepperoni' in requested_topping:
#     print('Adding pepperoni.')
# if 'extra cheese' in requested_topping:
#     print('Adding extra cheese.')

# print('\n Finished making your pizza! Enjoy.')


# requested_topping = []

# cond = input("Would you like to request toppings? [Y/N]").lower()


# if cond == 'y':
#     tops = input("What would it be? ")
#     requested_topping.append(tops)
#     cond2 = input("Anything else? [Y/N] ").lower()
#     if cond2 == 'y':
#         tops2 = input("What else, sir? ")
#         requested_topping.append(tops2)
#         cond2 = input("Anything else? [Y/N] ").lower()

# elif cond =='n':
#     print("Please wait...")

# for i in requested_topping:
#     print(f"Adding {i}.")

# print("Finished making your pizza!")