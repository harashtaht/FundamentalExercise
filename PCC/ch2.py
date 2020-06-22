# -- Variables --

message = "Hello Python world!"
# print(message)

message = "Hello Python Crash Course World!"
# print(message)

'''
we added a variable named message, and the string is the value.
few variables rules:
- v. names can only contain letters, numbers and underscores. 
    can not start with a number.
- spaces are not allowed
- avoid using Python keywords and function names as v.names.
- should be short but descriptive
- be careful when using the lowercase letter l and uppercase letter O, 
    they could be confused w/ numbers 1 and 0
'''

# -- Strings --

"The language 'Python' is named after Monty Python, not the snake."

name = "ada lovelace"
# print(name.title())

'''The method title() appears after the variable in the print() statement.
A method is an action that Python can perform on a piece of data.
The lower() method is particularly useful for storing data.
Many times you won't trust the capitalization that your users provide, 
so you'll convert strings to lowercase before storing them.
Then when you want to display the information, you'll use the case that makes
the most sense for each string.
'''

# print(name.upper())
# print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

# print("Hello, " + full_name.title() + "!")

'''In programming, whitespace refers to any nonprinting character, 
such as spaces, tabs, and end-of-line symbols.
To ensure that no whitespaces exists at the right end of a string, 
use the rstrip() method.'''

# print("Python")
# print("\tPython")
# print("\nPython")

favorite_language = 'python '
favorite_language2 = '     python'
# print(favorite_language)
# print(favorite_language.rstrip())
# print(favorite_language2)
# print(favorite_language2.lstrip())


# -- Numbers --
# 1 - Integers

# print(3/2)
# print(3//2)

x = 16.0/7
# print(round(x,3))

'Documentary to check - https://docs.python.org/3/tutorial/index.html'

