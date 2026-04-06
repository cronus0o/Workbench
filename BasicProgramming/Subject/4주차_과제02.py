a = int(input("영어점수 : "))
b = int(input("수학점수 : "))

if a >= 80 and b >= 80 :
    print("합격")
elif a < 80 and b < 80 :
    print("불합격")
else :
    print("재시험 기회제공")
