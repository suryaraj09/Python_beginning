import time

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Function Executed")

    return wrapper

@timer
def count():
    total = 0
    for i in range(1000000):
        total += i
    print(total)

count()
