## Tutorial 5 : Magic/Dunder Methods

## https://www.youtube.com/redirect?q=https%3A%2F%2Fdocs.python.org%2F3%2Freference%2Fdatamodel.html%23special-method-names&redir_token=58Eg1eK3r7wJG5-zfQpV1uRioFh8MTU5MjY1NDYzOUAxNTkyNTY4MjM5&event=video_description&v=3ohzBxoFHAY

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

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# __add__ for salary
# print(emp_1 + emp_2)

# __len__
# print(len('test'))
# print('test'.__len__())
# print(len(emp_1))


# print(repr(emp_1))
# print(emp_1.__repr__())

# print(str(emp_1))
# print(emp_1.__str__())

# print(1+2)
# print(int.__add__(1,2))

