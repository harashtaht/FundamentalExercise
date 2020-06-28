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

user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi'
}

# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)

'''
Notice that the key-value pairs are not returned in order in which they were stored,
even when looping through a dictionary.
Python doesn't care about the order in which the key-value pairs are stored;
it tracks only the connections between them.
'''

favorite_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

# for name, language in favorite_language.items():
#     print(name.title() + "'s favorite language is " + 
#     language.title() + ".")

# friends = ['phil', 'sarah']
# for name in favorite_language.keys():
#     print(name.title())

#     if name in friends:
#         print("Hi " + name.title() +
#         ", I see your favorite language is " +
#         favorite_language[name].title() + "!")


# # Not in order.
# for name in favorite_language.keys():
#     print(name.title() + ", thank you for taking the poll.")

# print("\n")
# # Printed in order.
# for name in sorted(favorite_language.keys()):
#     print(name.title() + ", thank you for taking the poll.")


# print("The following languages have been mentioned in database:")
# for language in set(favorite_language.values()):
#     print(language.title())

'''
Sometimes you’ll want to store a set of dictionaries in a list or a list of items as a value in a dictionary. 
This is called nesting. You can nest a set
of dictionaries inside a list, a list of items inside a dictionary, 
or even a dictionary inside another dictionary. Nesting is a powerful feature, as the following examples will demonstrate.
'''

alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)


# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5}
    aliens.append(new_alien)

# Show the first 5 aliens
# for alien in aliens[:5]:
#     print(alien)
# print(".....")

# Show how many aliens have been created.
# print("Total number of aliens: " + str(len(aliens)))

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie' : {
        'first': 'marie',
        'last' : 'curie',
        'location' : 'paris',
    },
}

# for keys in users.keys():
#     print(keys)
#     print(f"\nValues: {users[keys]}")