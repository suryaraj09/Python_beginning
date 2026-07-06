addition = lambda num : num + num

print(addition(2))

addTwo = lambda num : num +2

print(addTwo(40))

sum = lambda a, b : a + b

print(sum(2,2))

######################################################
# a quick function that we don't need later we use lambda

def funcbuilder(x):
    return lambda num : num + x

addten = funcbuilder(10)

print(addten(20))

#####################################################

lambda num : num * num

numbers = [1,2,3,4,5,6,7,8,9,10]

squared = map(lambda num: num * num, numbers)

print(list(squared))

####################################################

lambda num : num % 2 != 0

odd = filter(lambda num : num % 2 != 0, numbers)

print(list(odd))

# so the map() or filter has a syntax such as this where map(function, Iteration) and filter (Function, Iteration)
# Map() applies the operation to each variable in the list whereas filter() filter out the vairable from the list according to iterational operation.


from functools import reduce

lambda acc, curr : acc + curr

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr : acc + curr, numbers)

print(total)
