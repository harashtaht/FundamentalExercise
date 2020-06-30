# Chapter 10: Files and Exceptions #

# with open('./Files/pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

'''
If a bug in your program preents the close() statement from being executed,
the file may never lose.
Improperly closed files can cause data to be lost or corrupted.
If you close() too early in your program, you'll find yourself
trying to work with a closed file (a file you can't access),
leading to more errors.
---------------------------------------------------------------
You can also tell Python exactly where the file is on your compater regardless
of where the program that's being executed is stored.
Which is called an absolute file path.
'''

file_path = './Files/pi_digits.txt'

# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents)

# with open(file_path) as file_object:
#     for line in file_object:
#         print(line) #will have blank lines in between line

filename = './Files/programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write("Programming101")

# with open(filename, 'w') as file_object:
#     file_object.write("Programming101.\n")
#     file_object.write("Testing.\n")

# a stands for Append. Adding new lines after.
# with open(filename, 'a') as file_object:
#     file_object.write("The blablabla.\n")
#     file_object.write("Helvetica.\n")

# print(5/0) #ZeroDivisionError: division by zero

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

## Try-Except-Else

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

'''
It's bad that the program crashed, but it's also not a good idea
to let users see tracebacks.
Nontechnical users will be confused by them,
and in a malicious setting, attackers will learn more
than you want them to know from a traceback.

The only code that should go in a try statement is code that might cause an exception to be raised.
The except block tells Python what to do in case a certain exception arises when it
tries to run the code in the try statement.
'''

# title = "Alice in Wonderland"
# print(title.split())
filepath = './Files/'
filename = 'alice_in_wonderland.txt'
file_ = filepath + filename

def count_words(filename):
    # Count the approximate number of words in a file.
    filepath = './Files/'
    file_ = filepath+filename
    try:
        with open(file_) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = f"Sorry, the file {filename} does not exist."
        print(msg)
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {str(num_words)} words.")

# list_ = ['Bagong', 'Buwo', 'Leos']
# for i in list_:
#     print('haha'+i)

# filename = ['alice_in_wonderland.txt', 'gautama.txt']
# for i in filename:
#     # count_words(filepath+i)
#     count_words(i)

'''
The json module allows you to dump simple Python data structures into a file
and load the data from that file the next time the program runs.
You can also use json to share data between different Python programs, 
or other language.
'''


import json

numbers = [2, 3, 5, 7, 11, 13]

filename = './Files/numbers.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)

# with open(filename) as f_obj:
#     numbers = json.load(f_obj)

# print(numbers)

# username = input("What is your name? ").title()

# filename = './Files/username.json'
# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print(f"We'll remember when you come back, {username}!")

'''
Often, you'll come to a point where your code will work, but you recognize that
you could improve the code by breaking it up into a series of functions that 
have specific jobs.
This process is called Refactoring.
Which makes the code cleaner, easier to understand, and easier to extend.
'''

def greet_user():
    filename = './Files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print(f"We'll remember the next time you come back, {username}!")
    else:
        print(f"Welcome back, {username}")

# greet_user()

def get_stored_username():
    filename = './Files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

        