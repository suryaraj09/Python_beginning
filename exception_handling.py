try:
    f = open('test.txt')
except FileNotFoundError:
    print("Sorry, this file doesn't exist.")
except PermissionError as e:
    print(e)
except Exception as e :
    print(f"An error occurred: {e}")
else:
    print(f.read())
    f.close()
finally:
    print("execution completed")

