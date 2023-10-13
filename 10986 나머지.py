import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = []
C = [0 for _ in range(m)]
tmp = 0
result = 0

for i in a:
    tmp += i
    s.append(tmp) 

for i in range(n):
    remainder = s[i] % m # 합 배열의 모든 값에 나머지 연산 수행
    if remainder == 0:
        result += 1 # s[i] = 0일 때 원본 리스트 0부터 i까지의 구간 합이 m으로 나누어떨어짐을 의미
    C[remainder] += 1
    
for i in C:
    if i >= 2:
        result += i * (i-1) // 2
        # a % m = b % m일 때 (a-b) % m = 0
        # 이를 이용하여 변경된 합 배열에서 값이 같은 2개의 원소를 뽑는 모든 경우의 수를 계산
        # nCr = n! / (n-r)! * r!

print(result)
