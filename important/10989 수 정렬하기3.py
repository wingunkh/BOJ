import sys
input = sys.stdin.readline

# 계수 정렬은 시간복잡도가 O(N)이다.
# 그러므로 데이터의 범위가 작을 때 효율적이다.
n  = int(input())
a = [0 for _ in range(10001)]

for _ in range(n):
    number = int(input())
    a[number] += 1

for i in range(10001):
    if a[i] > 0:
        for j in range(a[i]):
            print(i)
