class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, user_string):
        name, age = user_string.split('-')
        return cls(name, int(age))

user_string = "Suryaraj-23"
user_1 = user.from_string(user_string)
print(user_1.name)
print(user_1.age)