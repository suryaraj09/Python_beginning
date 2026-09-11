user_input = list(map(int, input("Enter the values of an Array --> ").split(',')))


for i in user_input:
    if i < user_input[0]:
        user_input[0] = i

print("The Smallest value is: ",user_input[0])