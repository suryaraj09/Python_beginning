import requests
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self, amount=None):
        rate = amount if amount is not None else self.raise_amount
        self.pay = int(self.pay * rate)

    def monthly_schedule(self, month):
        response = requests.get(f'https://company.com/Office-hours{month}')
        if response.status_code == 200:
            return response.text
        else:
            return "Bad Response"

# why is my camera lagging so much and why I cannot do anything about it 

emp_1 = Employee('Suryaraj', 'Jadeja', 50000)
print(emp_1.email)  
# what 