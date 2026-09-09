import datetime
class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, user_string):
        name, age = user_string.split('-')
        return cls(name, int(age))

    @staticmethod
    def workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            print("It's a weekend")
        print("it's a workday")
        

user_string = "Suryaraj-23"
user_1 = user.from_string(user_string)
user_1.workday(datetime.date(2024, 12, 25))
print(user_1.name)
print(user_1.age)