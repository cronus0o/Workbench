a = int(input("첫 번째 숫자 : "))
b = int(input("두 번째 숫자 : "))
result = 0
for i in range(a, b+1, 1) :
    if i%2 == 1 :
        result += i
print("%d와 %d 사이에 있는 홀수의 합계 : %d" % (a, b, result))
