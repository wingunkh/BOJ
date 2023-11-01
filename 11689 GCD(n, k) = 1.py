n = int(input())
result = n

for i in range(2, int(n ** 0.5)+1):
    if n % i == 0:
        result -= result / i

        while n % i == 0:
            n /= i

if n > 1: # 반복문에서 제곱근까지만 탐색했으므로 1개의 소인수가 누락되는 케이스 처리
    result -= result / n

print(int(result))
