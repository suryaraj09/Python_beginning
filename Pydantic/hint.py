def create_user(first_name, last_name, age):
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"
    return {"first_name": first_name, "last_name": last_name, "age": age, "email": email}

user1 = create_user("surajjj", "jadeja", 22)
print(user1)
