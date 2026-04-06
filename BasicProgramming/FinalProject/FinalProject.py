# 기초프로그래밍 02분반 기말 프로젝트 : Turtle Graphic을 이용한 만국기 그리기

# module
import time
from nations import *

# 구현된 국가별 그리기 함수 맵핑 Dictionary
nations = { 
    'japan': draw_Japan,
    'northkorea': draw_NorthKorea,
    'southkorea': draw_SouthKorea,
    'china': draw_China,
    'india': draw_India,
    'israel': draw_Israel,
    'taiwan': draw_Taiwan,
    'uk': draw_UK,
    'usa': draw_USA,
    'vietnam': draw_Vietnam,
    'mycountry': draw_MyCountry
}

# 주 작동 코드
while True :  
    a = ''.join(input("국가의 이름을 입력하십시오 : ").split()).lower() # join()-split(), lower() : 띄어쓰기, 대소문자 오기입 무시
    if a == 'all' : # 모두 출력하는 기능
        b = float(input('각 국기 그리기 사이의 시간 간격(초) : '))
        for i in nations.values() : # 맵핑 딕셔너리 value값
            i() # 반환된 함수명을 이용해 실행
            time.sleep(b) # 각 동작마다 대기 시간 
    elif a == 'stop' : # 프로세스 종료 기능
        print("국가 그리기 종료")
        break
    elif not a in nations : # 예외처리
        print("해당 국가 출력 불가")
    else :
        nations[a]() # 각 국가별 함수 실행

