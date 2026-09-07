# method is a function that is associated with class. Classes allow us to logically group our data and functions in a way that is easy to reuse and also easy to build upon if need be. 

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def full_record(self):
        return '{} - {} - {}'.format(self.fullname(), self.email, self.pay)
        

emp_1  = Employee('Suryaraj', 'Jadeja', 50000)
emp_2  = Employee('Tony', 'Stark', 50000)

print(emp_1.fullname())
print(emp_2.fullname())

print(emp_1.full_record())
print(emp_2.full_record())


