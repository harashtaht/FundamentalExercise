class MyFirstClass:
    pass

a = MyFirstClass()
b = MyFirstClass()

# print(a)
# print(b)

####

# class Point:
#     pass

# p1 = Point()
# p2 = Point()

# p1.x = 5
# p1.y = 4

# p2.x = 3
# p2.y = 6

# print(p1.x, p1.y)
# print(p2.x, p2.y)

#### 

# class Point:
#     def reset(self):
#         self.x = 0
#         self.y = 0
    
# p = Point()
# p.reset()
# print(p.x, p.y)
# print(p)
# print(p.reset())

##----##

import math

class Point:
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt (
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2
        )

# how to use it:
point1 = Point()
point2 = Point()

point1.reset()
# point2.move(5,0)

# print(point2.calculate_distance(point1))
# assert (point2.calculate_distance(point1) == point1.calculate_distance(point2))

# point1.move(3,4)
# print(point1.calculate_distance(point2))
# print(point1.calculate_distance(point1))

##--- secret string---##

class SecretString:
    '''A not at all secure way to store a secret string.'''

    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        '''Only show the string if the pass_phrase is correct.'''
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ''

secret_string = SecretString("ACME: Top Secret", "antwerp")
# print(secret_string.decrypt("antwerp"))

# print(secret_string.plain_string)

# hacked
# print(secret_string._SecretString__plain_string)

# -- virtual environment "venv" page 48
