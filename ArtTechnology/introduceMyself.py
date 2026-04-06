# Introduction of Myself

import time 

def typer(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()

def hesitating():
    typer("Hmm...")
    time.sleep(1)
    typer('    Aspiring Programmer!')

info_dict = {
    'hi': lambda : typer('Hello User'),
    'whoareyou?': lambda : typer('박지호'),
    'howoldareyou?': lambda : typer('I was born in 2005.'),
    'wheredoyoustudy?': lambda : typer('I am studying at\n    ChungAng University.'),
    'whatisyourhobby?': lambda : typer('My hobby is exploring new things\n    I can do with computers.'),
    'whathobby?': lambda : typer('Programming, Customizing UI'),
    'and,whatcanyoudo?': lambda : typer("Using Linux, Github, Vim!\n    Even the screen\n    you're looking at right now\n    was made with Python!"),
    'so,whoreallyareyou?': hesitating
}

print()
print()
print()
print()
for char in 'Who Am I?':
    print(char, end='', flush=True)
    time.sleep(0.1)
time.sleep(1)
print()
print()
for char in '-Jiho Park-':
    print(char, end='', flush=True)
    time.sleep(0.1)
time.sleep(1)
print()
print()
print()
print()

print()
print()
print()
print()
typer("Welcome User!\nI'm in program now!")
time.sleep(3)
while True :  
    a = ''.join(input('Q : ').split())
    if a == 'all' : 
        for i in info_dict.values() : 
            time.sleep(0.5) 
            print('A : ', end = "")
            i()
        break
    elif a == 'bye' : 
        typer('Stop Process')
        time.sleep(1)
        break
    elif not a in info_dict : 
        typer('Error') 
    else :
        time.sleep(0.5) 
        print('A : ', end = "")
        info_dict[a]() 
        break
time.sleep(3)
