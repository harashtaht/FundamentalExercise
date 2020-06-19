# Object Orientated Programming in Python
# -- Part 1 --

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

# print(d.get_name())
# d.set_age(14)
# print(d.get_age())

# -- Part 2 -- 

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        # self.is_active = False
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
# print(course.students[0].name)
# print(course.add_student(s3))

# print(course.get_average_grade())


## -- Part 3 : Inheritance -- ##

# INIT 1
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("Meow")

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print("Bark")

# Modified for inheritance

# Upper level class
class Pet:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")

# Child classes
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

# p = Pet("Tim", 19)
# p.show()
# p.speak()

# c = Cat("Bill", 34, "brown")
# c.show()
# c.speak()

# d = Dog("Jill", 25)
# d.show()
# d.speak()

# f = Fish("Bubbles", 10)
# f.show()
# f.speak()

## -- Part 4 : -- ##
