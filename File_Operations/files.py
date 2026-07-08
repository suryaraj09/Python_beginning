import os

# # r = Read
# # a = Append
# # w = Write
# # x = Create
# # t = Text
# # b = Binary
# # r+ = Read and Write

# f = open("names.txt")
# # print(f.read())

# # print(f.read(4))
# # print(f.readline())
# # print(f.readline())

# for line in f:
#     print(line)

# f.close()

# try:
#     f = open("names.txt")
#     print(f.read())
# except:
#     print(" the file you are trying to read does not exist")
# finally:
#     f.close()
#     print("file is closed")


# Append - creates the files if it does nit exists

# f = open("names.txt", "a")
# f.write("\nNiel")
# f.close()

# f = open("names.txt")
# print(f.read())
# f.close()


# Write (Overwrite)

f = open("context.txt", "w")
f.write("I deleted all the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

#Two ways to create a new file

# Opens a file for writing, creates the file if it does not exists

f = open("name_list.txt", "w")
f.close()

# creates the specified file, but returns an error if the file exists
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()


f = open("name_list.txt")
print(f.read())
f.close()