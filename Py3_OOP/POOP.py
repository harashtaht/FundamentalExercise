# Object Orientated Programming in Python

def hello():
    print("hello")

# hello()

# x=1
# print(type(hello))
# print(type(x))

string = "hello"
# print(string.upper())

# class Dog:

#     def __init__(self, name):
#         self.name = name
#         # print("Bark! my name is " + name)

#     # def __init__(self):
#     #     pass

#     def add_one(self, x):
#         return x + 1

#     def bark(self):
#         print("bark!")

# # variable d, assigned it to an instance of the class Dog

# d = Dog("Tim")

# d2 = Dog("Bill")
# print(type(d))
# d.bark()
# print(d.add_one(5))
# print(d.name)
# print(d2.name)


## ---- 13 Mins ##

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

d = Dog("Tim", 3)
d2 = Dog("Bill", 6)

print(d.get_name())
d.set_age(14)
print(d.get_age())