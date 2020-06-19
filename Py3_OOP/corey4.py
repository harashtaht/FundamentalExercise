# Tutorial 4 : Creating Subclasses

class Employee:
    raise_amt = 1.04 #class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    pass


dev_1 = Developer('Corey', 'Schafer', 50000)
dev_2 = Developer('Test', 'Employee', 60000)

# print(dev_1.email)
# print(dev_2.email)

print(help(Developer))