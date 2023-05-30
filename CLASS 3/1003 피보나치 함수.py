# 피보나치 함수란?
# 한 단계 전의 숫자와 두 단계 전의 숫자를 더하는 함수

t = int(input())

for i in range(t):
    n = int(input())
    zero = [1,0,1]
    one = [0,1,1]

    if n >= 3:
        for i in range(3, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    
    print(zero[n], one[n])
