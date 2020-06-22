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
print(even_numbers)