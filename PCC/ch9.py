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

my_dog = Dog('willie', 6)

# print(my_dog.name.title())
# print(my_dog.age)
# my_dog.sit()


class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()