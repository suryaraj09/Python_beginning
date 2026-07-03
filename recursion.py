

def add_one(num):
    if (num>=9):
        return num + 1 # Base code where recurssion will stop
    
    total = num + 1 # Recursive call for the function
    print(total)

    return add_one(total)


# Call function for the initial value which is 0
mynewtotal = add_one(0)
print(mynewtotal)



