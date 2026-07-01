# def hello_world():
#     print("Hello World")

# hello_world()

# let's talk about naming function the same way we do for the variable hahahahahaha

# def sum(num1, num2):
#     print(num1 + num2)

# sum(42, 42)

# def square_root(num):
#     print (num*num)

# square_root(4)

def sum(num1 = 0 , num2 = 0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum()
print(total)

def multiple_items(*args):
    total = 0
    for num in args:
        total += num
    return total

multiple_items(4,5,6)
print(total)

def mult_named_items(**kwargs): #keyword_arguments
    print(kwargs)
    print(type(kwargs))
    # Print the "Hello World" message. "Hello World" is stored in variable named data. 

mult_named_items(first="Dave", last="Gray")


