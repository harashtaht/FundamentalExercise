# ** Chapter 4 : Working With Lists ** #

magicians = ['alice', 'david', 'carolina', 'deddy', 'yugi']

# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")

# ls = []
# for value in range(1,5):
#     ls.append(value)
# print(ls)

dc = {}
for val in range(len(magicians)):
    dc[val] = magicians[val]

# print(dc)

even_numbers = list(range(2,11,2))
# print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)

# print(squares)

# print(min(squares))
# print(max(squares))
# print(sum(squares))

# squares = [value**2 for value in range(1,11,2)]

# squares = [value*2 for value in magicians]
# print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print("Here are the first three players on my team:")
# for player in players[:3]:
    # print(player.title())

# Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

# print(my_foods)
# print(friend_foods)

'''Tuples
is an immutable list
'''

dimensions = (200,50)
# print(dimensions[0])
# print(dimensions[-1])


