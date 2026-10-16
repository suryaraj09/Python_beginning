import attrs
# class user:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email

#     def __repr__(self):
#         return f"User(name = {self.name}, age = {self.age}, email = {self.email})"

# user = user("surajj", 22, "suryarajjadeja09@gmail.com")

# # print(user.name)
# # print(user.age)
# # print(user.email)
# print(user)

@attrs.define
class user:
    name:str
    age:int
    email:str
    classes:str

user = user("surayraj", 22, "surayrajjadeja09@gmail.com", "high")
print(user)

@attrs.define
class company:
    name: str
    emp : int
    Uid: int

company = company("google", 100, 12345)
print(company.name)
print(company.emp)
print(company.Uid)  

class department:
    def __init__(self, name, emp):
        self.name = name
        self.emp = emp

    def __repr__(self):
        return f"Department(name = {self.name}, emp = {self.emp})"

