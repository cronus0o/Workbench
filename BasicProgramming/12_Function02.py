# [Section 12]
# Local Variable vs Global Variable

# global variable

# Recursive Function
# maximum 1000 deeps
def factorial(p) :
    if p == 1 :
        return 1
    else :
        return p * factorial(p-1)
    
print(factorial(5))

# Function in Variable, List, Parameter
def function(p1, p2, p3) :
    print(p1 + p2 + p3)

a = function
a(1, 2, 3)

# Nested Function

# lambda Function
sum = lambda p1, p2 : p1 + p2
print(sum(10, 20))

# Map Function
mylist = [1, 2, 3, 4, 5]
add10 = lambda num : num + 10
mylist = list(map(add10, mylist))
print(mylist)

# Generator, Yield
def generator() :
    yield 1
    yield 2
    yield 3
print(list(generator()))
