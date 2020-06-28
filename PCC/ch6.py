# -- Chapter 6: Dictionaries -- #

alien_0 = {'color': 'green', 'points' : 5}

alien_0['x_position'] = 0
alien_0['y_position'] = 25
# print(alien_0)

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}

# speed_inp = int(input("Choose speed: (1 = slow, 2 = medium, 3 = fast) "))

# if speed_inp == 1:
#     alien_0['speed'] = 'slow'
# elif speed_inp == 3:
#     alien_0['speed'] = 'fast'
# else:
#     pass

if alien_0['speed'] == 'slow':
    x_increment = 10
elif alien_0['speed'] == 'medium':
    x_increment = 25
else:
    x_increment = 50

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

# print("New x-position of alien: " + str(alien_0['x_position']))


'''
When you no longer need a piece of information that's stored in a dictionary,
you can use the del statement to completely remove a key-value pair.
All del needs is the name of the dictionary and the key you want to remove.
'''

alien_0 = {'color' : 'green', 'points' : 5}
# print(alien_0)

del alien_0['points']
# print(alien_0)


# -- Looping Through Dictionary

