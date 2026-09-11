class Employee:
    # Dunder init (Double underscore) where the python intialise an objects attributes and set up its starting state right when the object is created
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.email = first + '-' + last + '@company.com'
        self.pay = pay 

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def string_emp(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

class developer(Employee):
    raise_amt = 1.10

 
dev1 = developer('surajjj', 'jadeja', 600000)
dev2 = developer('tony', 'stark', 900000)

print(dev1.email)
print(dev2.email)
print(help(developer))