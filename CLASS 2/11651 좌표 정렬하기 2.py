import sys
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

array.sort(key = lambda x:(x[1], x[0]))

for i in array:
    print(i[0], i[1])
