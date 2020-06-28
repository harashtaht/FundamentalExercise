# -- Chapter 7 : User Input and While Loops -- #

'''
The input() function pauses your program and waits for the user to enter some text.
Once Python receives the user's input,
it stores it in a variable to make it convenient for you to work with.
The input() function takes one argument: the prompt, or instructions,
that we want to display to the user so they know what to do.
'''

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

# name = input(prompt)
# print("\nHello, " + name + "!")

'''
When you use the input() function, Python interprets everything the user enters as a string.
'''

# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")


# -- Introducing while Loops

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.\n"

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)


# -- Flag

'''
For a program that should run only as long as many conditions are true,
you can define one variable that determines whether or not the entire program is active.
This variable, called flag, acts as a signal to the program.

'''

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print("> ", message)


# -- Using a break to Exit a Loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()} !")


"""A loop that starts with while True will run forever unless it reaches a break statement.
Rather than breaking out of a loop entirely without executing the rest of its code,
you can use the continue statement to return to the beginning of the loop based on
the result of a conditional test.
"""

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number %2 == 0:
        continue

    print(current_number)

