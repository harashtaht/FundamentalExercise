# -- Chapter 3 : Introducing Lists -- #

'''
A list is a collection of items in a particular order.
You can make a list that includes the letters of the alphabet, 
the digits from 0-9, or the names of all the people in your family.
'''

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# print(bicycles[2].title())
# print(bicycles[-1].title())

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'
# motorcycles.append('ducati')
app = 'ducati'
app2 = 'vario'
motorcycles.append(app.title())
motorcycles.append(app2.upper())
# print(motorcycles)

# -- Inserting Elements into List

# print(motorcycles)
motorcycles.insert(0, 'harley davidson'.title())
motorcycles.insert(3, 'satria')
# print(motorcycles)

# del motorcycles[-1]
# print(motorcycles)

'''
The pop() method removes the last item in a list,
but it lets you work with that item after removing it.
The term pop comes from thinking of a list as a stack of items and popping
one item off the top of the stack.
In this analogy, the top of a stack corresponds to the end of a list.
'''
# print(motorcycles)
# print(motorcycles.pop())
# print(motorcycles)
popped_motorcycles = motorcycles.pop()
# print(popped_motorcycles)

'''If you only know the value of the item you want to remove,
you can use remove() method'''

# motorcycles.remove('suzuki')
# print(motorcycles)

too_expensive = 'ducati'
# print(motorcycles)
# print('\nA ' + too_expensive.title() + " is too expensive for my lame ass.")

# Do the exercise on page 79 of 562

# 
# *** Organizing a List ***

cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

for i in range(len(cars)):
    cars[i] = cars[i].title()
    # print(cars[i])
# print(cars)

'''
To maintain the original order of a list but present it in a sorted order,
you can use the sorted() function.
The sorted() function lets you display your list in a particular
order but doesn't affect the actual order of the list.
'''

# print('This is the original list:\n', cars)

# print('Here is the sorted list:\n', sorted(cars))
# # cars.sort()
# # print('Here is the sorted list:\n', cars)

# print('Here is the original list again:\n', cars)

# print(cars)
# cars.reverse()
# print(cars)

# // Exercise 3-8
locs = ['shinjuku', 'new zealand', 'brooklyn', 'amsterdam', 'manchester']
# print(locs)

# print(sorted(locs))

# print(locs)

# print(sorted(locs, reverse=True))

# locs.reverse()
# print(locs)
# locs.reverse()
# print(locs)
