users = ['Surajj', 'Dave' , 'John', 'Sara']
data = ['Dave', 42, True]
emptylist = []

print ("Dave" in users)
print(users[0])
print(users[-1])
print(users[0:2])

print(users.index('Dave'))

print('')

print(len(data))

users.append('Lucy')
print(users)

users.extend(['tinku' , 'saltu'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Robert', 'jpj']
print(users)

users.remove('Bob')
print(users)

print('')
print(users.pop())
print(users)

#del data
data.clear()
print(data)

print('')
users[1:2] = ['dave']
users.sort(key=str.lower)
print(users)


print('')
nums = [2, 42, 32, 23, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print('')

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(nums)
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)

print(type(nums))

mylist = list([1, 'Neil', True])
print(mylist)

#Tuples

mytuple = tuple(('Dave', 42, True))
anothertuple = (1,2,3,4,5)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)