print("*************\n")
print("*Calculator*")
print("\n*************")



def calci():
    while True:
        num_1 = int(input("Please enter the first number => "))
        num_2 = int(input("Please enter the second number => "))

        op = input(
            "Please select from the following operations to execute \n"
            "1.Add\n2.Substract\n3.Multiply\n4.Divide \n"
        ).strip()

        if op == "1":
            print(num_1 + num_2)
        elif op == "2":
            print(num_1 - num_2)
        elif op == "3":
            print(num_1 * num_2)
        elif op == "4":
            if num_2 == 0:
                print("cannot divide by zero")
            else:
                print(num_1 / num_2)
        else:
            print("Invalid operation")

        if not repeat():
            break

def repeat():
    while True:
        oper = input("please select y for continuing operation and q to quit the program: ").strip().lower()
        if oper == "y":
            return True
        if oper == "q":
            return False
        print("please select y or q")

        
if __name__ == "__main__":
    calci()
