# def create_User(username, email, age):
#     if not isinstance(username, str):
#         raise TypeError("username must be a string")
#     if not isinstance(email, str):
#         raise TypeError("email must be a string")
#     if not isinstance(age, int):
#         raise TypeError("age must be an integer")
#     return {"username": username, "email": email, "age": age}

# user1 = create_User("suryaraj", "[EMAIL_ADDRESS]", 21)
# print(user1)

# user2 = create_User("Shyani", None, "old")
# print(user2)

from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    age: int

user1 = User(username = "Suryaraj", email= "[EMAIL_ADDRESS]", age= 21)
print(user1)

user2 = User(username = "Shyani", email= None, age= "old")
print(user2)