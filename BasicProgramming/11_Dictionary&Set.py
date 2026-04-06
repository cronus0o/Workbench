# [Section 11]
# Dictionary

dict1 = {
    'age': 20,
    'height': 175,
    'weight': 80
}

print(dict1)
print(dict1['age'])

dict1['phone'] = 'xxxx-yyyy'
dict1['weight'] = 70
print(dict1)

# .get(key) # when No keys, return nothing
# .keys()
# .values()
# .items() # return tuple

# 'key' in dictionary # True or False

# import operator
# operator.itemgetter()

# Set ... Only Keys Dictionary
# & | - ^
# .intersection()
# .union()
# .difference()
# .symmetric_difference()

# List Comprehension
# list = [calculate(i) for i in range() if]
numList = [num for num in range(1, 6)]
print(numList)

# zip()

# Shallow Copy
# Deep Copy