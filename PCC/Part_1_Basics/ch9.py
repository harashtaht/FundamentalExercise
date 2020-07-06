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
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# Modifying Attribute Values
'could be done directly through an instance, set the value through a method, or increment the value through a method'

# MAV - directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# MAV - through a method
# class Car():

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 1

#     def get_descriptive_name(self):
#         long_name = f"{str(self.year)} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         print(f"This car has {str(self.odometer_reading)} miles on it.")
    
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

# my_new_car = Car('audi', 'a4', 2016)

# my_new_car.read_odometer()
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()
# my_new_car.update_odometer(20)

my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()


# -- Inheritance -- #

'''
If the class written is a specialized version of another class that had been written,
we can use inheritance. When one class inherits from another, 
it automatically takes on all the attributes and methods of the first class.
The original class is called parent class,
and the new class is called child class.
'''

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.increment_odometer(20020)
# my_tesla.read_odometer()

'''
The super() function is a special function that helps Python make connections between the parent and child class.
This line tells Python to call the __init__() method from child car's parent class,
giving ElectricCar instance all the attributes of its parent class.
The name super comes from a convention of calling the parent class a superclass,
and child class a subclass.
'''


# class ElectricCar(Car):
#     '''Represent aspects of a car, specific to electric vehicles.'''

#     def __init__(self, make, model, year):
#         '''
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         '''
#         super().__init__(make, model, year)
#         self.battery_size = 70

#     def describe_battery(self):
#         # Print statement describing the battery size.
#         print(f"This car has a {str(self.battery_size)}-kWh battery.")

#     def initialize_battery(self, battery_size_in):
#         self.battery_size = battery_size_in

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# my_tesla.initialize_battery(120)
# my_tesla.describe_battery()


from car import Car, ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print("\n****\n")

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()