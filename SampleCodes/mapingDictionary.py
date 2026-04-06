# Maping Dictionary 


info_dict = {
    'exampleFunction': lambda : print('test')
}

while True :  
    a = ''.join(input('Write Here : ').split())
    if a == 'all' : # Generate all function in info_dict
        for i in info_dict.values() : 
            i()
        break
    elif a == 'bye' : 
        break
    elif not a in info_dict : 
        break
    else :
        info_dict[a]() 
        break