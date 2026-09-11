class Students:
    university = "Ahmedabad University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"hello my name is : {self.name}"

    @classmethod
    def show_university(cls):
        return f"University name is : {cls.university}"

    @staticmethod
    def is_valid_age(age):
        if age>=18:
            return "T"
        else:
            return "F"

    @classmethod
    def from_string(cls, student_string):
        name, age = student_string.split("-")
        return cls(name, int(age))


student = Students.from_string("Suryaraj-22")

print(student.introduce())
print(Students.show_university())
print(Students.is_valid_age(22))