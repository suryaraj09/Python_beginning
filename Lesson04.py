import math
# #String data type

# #literal assignment
# first = "surajjj"
# last = "jadeja"

# # # print(type(first))
# # # print(type(last))

# # Pizza = str("Pepproni")
# # print(type (Pizza))
# # print(type (Pizza) == str )
# # print(isinstance (Pizza, str))

# # #concatenation
# # decade = str(2002)
# # print(type(decade))
# # print(decade)

# # statement = "I like rock music from the " + decade +"s."
# # print(statement)

# # #Multiple lines
# multiline = '''
# Hey how are you ?

# I was just checking in. 
#                           All good?

# '''
# print(multiline)

# # Escaping Special Characters 
# sentence = 'I\'m back at work!\t Hey! \n\n Where\'s this at \\ located?'
# print(sentence)

# print(multiline.upper)
# print(multiline.lower)
# print(multiline.title)
# print(multiline.replace("good", "ok"))
# print(multiline)

# print(len(multiline))

# print(len(multiline.strips))
# print(len(multiline.lstrips))

title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$4".rjust(4))
print("Muffin".ljust(16, ".") + "$10".rjust(4))
print("Cheescake".ljust(16, ".") + "$15".rjust(4))

# print('')

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

print('')

Price = 100
best_Price = int(80)
print(type(Price))
print(isinstance(Price, int))


print('')
#float type
gpa = 3.28
y = float(1.14)
print(isinstance(gpa, float))

print('')

#complex value
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print('')
#Built-in function of the python
print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))
print(gpa * -1)

print('')

print(math.pi)
print(math.sqrt(gpa))
print(math.ceil(gpa))
print(math.floor(gpa))