from pydantic import validate_call

@validate_call
def create_user(first_name:str, last_name:str, age:int)-> dict:

    # if not instance_of(first_name, str):
    #     raise TypeError("first_name must be a string")
    
    # if not instance_of(last_name, str):
    #     raise TypeError("last_name must be a string")
    
    # if not instance_of(age, int):
    #     raise TypeError("age must be an integer")

    email = f"{first_name.lower()}_{last_name.lower()}@example.com"
    return {"first_name": first_name, 
    "last_name": last_name, 
    "age": age,
    "email": email}

user1 = create_user("surajjj", "jadeja", '22')
print(user1)
