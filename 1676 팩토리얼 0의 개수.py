def factorial(n): # 팩토리얼 함수 재귀 구현 시 메모리 초과 발생
    result = 1

    for i in range(1, n+1):
        result *= i

    return result

n = int(input())
s = str(factorial(n))
s = s[::-1]
count = 0

for i in s:
    if i == '0':
        count += 1
    else:
        break

print(count)
