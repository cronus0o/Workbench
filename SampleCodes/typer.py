# Typer : function
# print each character in a string

# import time module
# Time interval between each print

import time 

def typer(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.3)
    print()

typer('Typer Example')