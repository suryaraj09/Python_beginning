# def outer_function():
#     message = 'Hello'
#     def inner_function():
#         print(message)
#     return inner_function()

# hi_func = outer_function('hi')
# bye_func = outer_function('bye')

# hi_func()
# bye_func()

# # this dynamically ALter the Functionality of your functions

# # A python decorator is a tool that lets you add new features to an existing function without altering the existing function's code.

# def decorator_function(message):
#     def wrapper_function():
#         return message.upper()
#     return wrapper_function

# def display():
#     print("Display function")

# display = decorator_function('Hello')
# display()

# def greet():
#     print("Hello")
#     print("How are you?")

# x = greet

# x()

def log_fun(func):
    def wrapper():
        print("Function started")
        func()
        print("Function Ended")
    return wrapper

@log_fun
def say_hello():
    print("Hello World")

say_hello()