#String data type

#literal assignment
first = "surajjj"
last = "jadeja"

# # print(type(first))
# # print(type(last))

# Pizza = str("Pepproni")
# print(type (Pizza))
# print(type (Pizza) == str )
# print(isinstance (Pizza, str))

# #concatenation
# decade = str(2002)
# print(type(decade))
# print(decade)

# statement = "I like rock music from the " + decade +"s."
# print(statement)

# #Multiple lines
multiline = '''
Hey how are you ?

I was just checking in. 
                          All good?

'''
print(multiline)

# Escaping Special Characters 
sentence = 'I\'m back at work!\t Hey! \n\n Where\'s this at \\ located?'
print(sentence)

print(multiline.upper)
print(multiline.lower)
print(multiline.title)
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))

print(len(multiline.strips))
print(len(multiline.lstrips))
