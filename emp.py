# class employee:

#     raise_amt = 1.04

#     def __init__(self, first, last, pay):
#         self.first  = first
#         self.last = last
#         self.email = first + "." + last + "@comnpany.com"
#         self.pay = pay

#     def fullname(self):
#         return f'{self.first} {self.last}'

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)

#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount

#     @classmethod
#     def from_string(cls, emp_string):
#         first, last, pay = emp_string.split("-")
#         return cls(first, last, pay)

#     @staticmethod
#     def is_worday(day):
#         if day == 'Saturday' or day == 'Sunday':
#             return False
#         return True

#     def __repr__(self):
#         return f"employee ('{self.first}', '{self.last}', {self.pay})"

#     def __str__(self):
#         return f"Full name = {self.fullname()}\nemail = {self.email}"

# emp_1 = employee('Suryaraj', 'Jadeja', 50_000)
# print(repr(emp_1))
# print(str(emp_1))

# class developer(employee):
#     raise_amt = 1.10

#     def __init__(self, first, last, pay,prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang

# class manager(employee):
#     def __init__(self, first, last, pay,employees=None, supervisor=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees 

#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)

#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)

#     def print_emp(self):
#         for emp in self.employees:
#             print(emp.fullname())

# # print(emp_1)
# # print

# # mgr_1 = manager('sue', 'jone', 90_000)
# # print(mgr_1.email)
# # print(isinstance(mgr_1, developer))

# # dev_1 = employee('Correy', 'Schaffer', 50_000)
# # dev_2 = employee('Surajjj', 'Jadeja', 55_000)

# # print(dev_1.pay)
# # dev_1.apply_raise()
# # print(dev_1.pay) # this prints the dev_1and talk about 

# print(int.__add__(10,20))

# print(int.__sub__(10,20))

print(len('test'))
print('test'.__len__())