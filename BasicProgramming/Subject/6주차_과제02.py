inS, outS = "", ""
count, i = 0, 0
inS = input("문자열을 입력하세요 : ")
count = len(inS)

for i in range(count) :
    outS += inS[count - 1 - i]

print("내용을 거꾸로 출력 --> %s" % outS)
