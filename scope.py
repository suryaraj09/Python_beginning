# name = "Dave"
# print(name)

# def hello_world():
#     print(name)
#     print(name + "!"*5)

# hello_world()

# def sum(num1 = 0, num2 = 0):
#     return num1 + num2

# while True:
#     num1_str1 = input("\nEnter the first number => ")
#     num_str2 = input("Enter the second number => ")
    
#     try:
#         # Convert inputs to integers for mathematical addition
#         num1 = int(num1_str1)
#         num2 = int(num_str2)
        
#         result = sum(num1, num2)
#         print("the sum of your input =>", result)
#     except ValueError:
#         print("Please enter valid integers!")
#         continue

#     # Ask the user if they want to do it again (y) or quit (q)
#     choice = input("Do you want to do it again? (y/q): ").strip().lower()
#     if choice == 'y':
#         continue
#     elif choice == 'q':
#         print("Goodbye!")
#         break
#     else:
#         print("Please enter a valid choice!")
#         continue    

# name = input("Please enter your name = > ")

# def greetings():
#     print("hello" +" " +name +" " + '!'*5)

# greetings()

# def max(*numbers):
#     if len(numbers) == 0:
#         return None
#     max_num = numbers[0]
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num

# print(max())

# def main(*args):
#     print(args)

# main("uzi", "maleay", "Lucy")

# def maina(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(f'{key}:{value}')
    
# maina(name = "surajj", role = "AI Engineer", age = "23")

count = 1
def another():
    global count
    count += 10
    color = "blue"
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")

another()



