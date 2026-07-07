class justnotcoolerror(Exception):
    pass


x = 2
try:
    print(x / 2)
    raise justnotcoolerror("this is just isn't cool men")
except NameError:
    print("Name error means something is probably undefined.")
except ZeroDivisionError:
    print("please do not divide by 0")
except TypeError as error:
    print(error)
except justnotcoolerror as error:
    print(error)
else:
    print("No errors!")
finally:
    print("This finally executes every time")

