## -- Chapter 9 : Classes -- ##

'''
In OOP, you write classes that represent real-world things and situations,
and you create objects based on these classes.
Making an object from a class is called instantiation, and you work
with instances of class.
'''

# Creating and Using a Class

class Dog():
    "A simple attempt to model a dog."

    def __init__(self, name, age):
        "Initialize name and age attributes."
        self.name = name
        self.age = age

    def sit(self):
        "Simulate a dog sitting in response to a command."
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        "Simulate rolling over in response to a command."
        print(self.name.title() + " rolled over!")


'''
A function that's part of a class is a method.
The __init__() method is a special method Python runs automatically
whenever we create a new instance based on the Dog class.
Variables that are accessible through instances like this are called attributes. 
-> i.e. self.age, self.name
'''