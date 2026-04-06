import time

def typer(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    
typer("안녕하세요. 반갑습니다!")