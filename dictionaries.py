band = {
    "vocals": "plant",
    "guitar": "eddie",
    "bass": "Micky",
    "drums": "alex",
    "guitar2": "David"
}

band2 = dict(vocals='plants', guitar='page', bass = 'Micky', drums ='alex', guitar2='David')

print(band)
print(band2)
print(type(band))
print(len(band))

print(band.keys()) # gives all the keys in the dictionaries
print(band.values()) # gievs all the the values in the dictionaries
print(band.items())# gives the tuples of the key and value of the dictonaries that in this case is band

print(band.get("vocals"))

print("guitar" in band)
print("Suryaraj" not in band)

# change value in the code
band["vocals"] = "Michael Jackson"
print(band)

print(band.popitem())
print(band)

# Delete and clear
band["lead singer"] = "Michael Philips"
print(band)

band.update({"bass" : "Arijit Singh"})
print(band)

band2.clear()
print(band2)


print('')
band2 = band # create refernce to the same dictionaries
print("Bad copy")
print(band2)
print(band)

band2["drums"] = "Dave"
print(band)


print('')
band2 = band.copy() # doesn't create a reference but is the same copy
band2["drums"] = "Alex"

print("Good copy")
print(band2)
print(band)

band3 = dict(band)
print('good copy')
print(band3)


print('')

member_1 = {
    "name":"surajjj",
    "Instrument":"guitar"
}

member_2 = {
    "name":"Tinku",
    "Instrument":"Vocalist"
}

member_3 = {
    "name":"Saltu",
    "Instrument":"Guitar"
}

band = {
    "member_1" : member_1,
    "member_2" : member_2,
    "member_3" : member_3
}
print(band["member_1"]["name"])

print(band) 


nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(type(nums2))
print(len(nums))

# No duplicates are allowed
print('')
nums = {1,2,2,3,4,5}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums2 = {1, 2, True, 4, False, 3}
print(nums2)

# Add new element to the set
nums.add(8)
print(nums)

# Merge two sets to create a new set
one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset)