a = input("아이디 : ")
if a == "admin" :
    print("모든 콘텐츠 이용 가능")
else :
    b = int(input("회원 레벨 : "))
    if 2 <= b <= 7 :
        print("일부 콘텐츠 이용 가능")
    else :
        print("콘텐츠 이용 불가")
    
