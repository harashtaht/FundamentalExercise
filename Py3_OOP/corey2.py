# Tutorial 2: Class Variables #

# -- initial -- #

'''Class variables are variables that we set inside a class, and are shared among all instances. 
Which in here is "raise_amount". Instance variables are variables that are different from each instance.
For example, the names and the pay for each employee.'''

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        # print(self.first + " " + self.last)
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_1.__dict__)
# print(Employee.__dict__)

# print(emp_1.raise_amount)
# Employee.raise_amount = 1.07

# emp_1.raise_amount = 1.05
# print(emp_1.__dict__)
# print(emp_2.__dict__)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)