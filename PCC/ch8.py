# -- Chapter 8 : Function -- #

# username = input("Enter your username: ")

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}! Welcome back :-)")

# greet_user(username)
# greet_user('jesse')

'''
We defined greet_user() to require a value for the variable username.
The variable username in the definition of greet_user() is an example of a parameter,
a piece of information the function needs to do its job.
The value 'jesse' in greet_user('jesse) is an example of an argument.
Argument is a piece of information that is passed from a function call to a function.

In this case, the argument 'jesse' was passed to the function greet_user(),
and the value was stored in the parameter username.
'''


## -- Passing Arguments -- ##

## Positional Arguments ##

def describe_pet(animal_type, pet_name):
    "Display information about a pet."
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

## Keyword Arguments ## 
'''
A keyword argument is a name-value pair that you pass to a function.
'''

# describe_pet(animal_type='horse', pet_name='butcher')
# describe_pet(pet_name='johnnyboy', animal_type='penguin')

## Default Values ##
'''
When writing a function, you can define a default value for each parameter.
If an argument for the parameter is not provided in function call, Python uses the 
default value.
'''


def describe_pet(pet_name, animal_type='dog'):
    "Display information about a pet."
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('harry')

# describe_pet('johnny', animal_type='Labrador')


## Return Values ##

def get_formatted(first_name, last_name, middle_name=''):
    "Return a full name, neatly formatted."
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' '+ last_name   
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted('jimi', 'hendrix')
# print(musician)

musician = get_formatted('jimi', 'hendrix', 'lee')
# print(musician)

#
# Make a nested function, for first_name last_name using while.
#


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

# print(build_person('jimi', 'hendrix', age=27))


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     print("Hello, ", get_formatted_name(f_name, l_name))

def greet_user(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'maria', 'jesus']
greet_user(usernames)