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