# [Section 09]

def function(parameter) :
    print(parameter)
    return

function(1)

# Parameter = Local Variable

# Dafault Argument Value
def func1(p1 = 10, p2 = 20, p3 = 30) :
    print(p1 + p2 + p3)

func1()
func1(1,2,3)

# Keyword Argument 
func1(p2 = 30) 

# Arbitrary Argument List
def func2(*p) :
    for i in p :
        print(i)

func2('start','end')

# Dictionary Argument
def func3(**p) :
    for i in p.values() :
        print(i, ': ', end = '')
    print('\n')

func3(age = 20, height = 175, weight = 80)

# Default & Arbitrary
def func4(p1, *p2) :
    print(p1)
    for i in p2 :
        print(i)

func4(1, 2, 3, 4)
# func4(p1 = 5, 1, 2, 3) Wrong Syntax